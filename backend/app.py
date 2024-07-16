from flask import Flask, request, jsonify
from flask_cors import CORS
from scrapper import login_instagram, search_instagram, get_profiles
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
CORS(app)  # Enable CORS

# Configure Chrome options
options = Options()
options.headless = True
driver_path = '/usr/bin/chromedriver'  # Make sure to set the correct path to the ChromeDriver
service = Service(driver_path)

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('query')
    country = data.get('country')

    if not query or not country:
        return jsonify({"error": "Missing query or country"}), 400

    username = ""  # Replace with your Instagram username
    password = ""  # Replace with your Instagram password

    driver = webdriver.Chrome(service=service, options=options)

    try:
        login_instagram(driver, username, password)
        results = search_instagram(driver, query, country)
        profiles = get_profiles(results)
        return jsonify(profiles), 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
