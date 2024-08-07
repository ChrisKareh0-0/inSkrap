from flask import Flask, request, jsonify
from flask_cors import CORS
from googleMaps_Scrape import scrape_google_maps
import json  # Add this line to import the json module

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    keyword = data.get('keyword', 'lawyer')
    location = data.get('location', '')
    output_file = 'results.json'
    
    # Assuming your scrape_google_maps function takes keyword and output_file as parameters
    scrape_google_maps(f"{keyword} {location}", output_file)
    with open(output_file, 'r', encoding='utf-8') as f:
        results = json.load(f)
        
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
