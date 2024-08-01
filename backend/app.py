from flask import Flask, request, jsonify
from flask_cors import CORS
from googleMaps_Scrape import scrape_google_maps

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    keyword = data.get('keyword')
    location = data.get('location')

    # Construct the search query
    search_query = f"{keyword} in {location}"
    
    # Call the scrape_google_maps function
    results = scrape_google_maps(search_query)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
