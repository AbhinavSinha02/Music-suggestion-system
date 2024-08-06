import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load data
songs = pd.read_csv('data/songs.csv')
users = pd.read_csv('data/users.csv')

# Create user-item matrix
user_item_matrix = users.pivot(index='user_id', columns='song_id', values='listen_count').fillna(0)

# Normalize the data
scaler = StandardScaler()
user_item_matrix_normalized = scaler.fit_transform(user_item_matrix)

# Compute similarity
similarity_matrix = cosine_similarity(user_item_matrix_normalized)

# Convert back to DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index)

def get_recommendations(user_id, n=5):
    similar_users = similarity_df[user_id].sort_values(ascending=False).index[1:n+1]
    recommended_songs = pd.DataFrame()

    for similar_user in similar_users:
        user_songs = users[users['user_id'] == similar_user]
        recommended_songs = recommended_songs.append(user_songs)
    
    recommended_songs = recommended_songs.drop_duplicates(subset='song_id', keep='first')
    recommended_songs = recommended_songs.merge(songs, on='song_id')
    recommended_songs = recommended_songs.head(n)

    return recommended_songs[['song_name', 'artist']].to_dict(orient='records')
