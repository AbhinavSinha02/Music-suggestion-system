from flask import render_template, request, jsonify
from app import app
from app.model import get_recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)
