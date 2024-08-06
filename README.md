Music Recommendation System

This project is a music recommendation system that uses machine learning techniques to provide personalized music recommendations.

Features

- User and song data handling
- Collaborative filtering for recommendations
- REST API for accessing recommendations
- Simple front-end interface for user interaction

Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/music-recommendation-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd music-recommendation-system
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python run.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000`.

Data

The `data` directory contains two CSV files:

- `songs.csv`: Contains song information.
- `users.csv`: Contains user listening history.

Usage

1. Enter a user ID in the input field.
2. Click the "Get Recommendations" button to see the recommended songs for that user.
