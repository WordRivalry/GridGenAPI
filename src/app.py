import os
import random
from flask import Flask, request, jsonify
from src.config import Config
import json

app = Flask(__name__)

# Load your data here; assuming the file is 'data.json' in the same directory
with open(Config.Paths.grids, 'r') as file:
    data = json.load(file)

@app.route('/get_grid', methods=['GET'])
def get_grid():
    # Get diversity and difficulty from query parameters
    min_diversity = float(request.args.get('min_diversity', 0))  # Default to 0 if not provided
    max_diversity = float(request.args.get('max_diversity', 1))  # Default to 1 if not provided
    min_difficulty = float(request.args.get('min_difficulty', 0))  # Default to 0 if not provided
    max_difficulty = float(request.args.get('max_difficulty', float('inf')))  # Default to infinity if not provided

    # Filter the data based on diversity and difficulty range
    filtered_data = [item for item in data if min_diversity <= item['stats']['diversity_rating'] <= max_diversity and min_difficulty <= item['stats']['difficulty_rating'] <= max_difficulty]

    # If filtered_data is not empty, return one random entry, else return an error message or empty data
    if filtered_data:
        selected_data = random.choice(filtered_data)
        return jsonify(selected_data)
    else:
        return jsonify({"error": "No data found matching the criteria"}), 404


if __name__ == '__main__':        
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=True)