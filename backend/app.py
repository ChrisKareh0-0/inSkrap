from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import search_instagram

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    country = data.get('country')
    if not query:
        return jsonify({'error': 'Query is required'}), 400
    results = search_instagram(query, country)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
