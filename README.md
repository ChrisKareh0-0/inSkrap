
---

# inSkrap

A web application that scrapes data from Google Maps based on a given keyword and location, and displays the results. Users can export the results to PDF and Excel formats.

## Table of Contents

- [Google Maps Scraper](#google-maps-scraper)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Features](#features)
  - [Setup Instructions](#setup-instructions)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
  - [Usage](#usage)
  - [Technologies Used](#technologies-used)


## Project Description

This project is a web application that allows users to scrape data from Google Maps based on a specified keyword and location. The application displays the results in a table and provides options to export the data to PDF and Excel formats. 

## Features

- Search and scrape data from Google Maps based on keyword and location.
- Display results in a table format.
- Export results to PDF.
- Export results to Excel.
- Interactive neural noise background effect.

## Setup Instructions

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/google-maps-scraper.git
   cd google-maps-scraper
   ```

2. **Set up a virtual environment:** // **Or you can simply just run app.py**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install Flask selenium webdriver-manager
   ```

4. **Run the Flask application:**
   ```bash
   export FLASK_APP=app.py
   flask run
   ```

### Frontend Setup

1. **Navigate to the frontend directory (if applicable):**
   ```bash
   cd frontend
   ```

2. **Install the required packages:**
   ```bash
   npm install
   ```

3. **Start the React application:**
   ```bash
   npm start
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:3000` to access the React frontend.
2. Enter the keyword and location in the search form and click "Search".
3. View the results displayed in the table.
4. Use the "Export to PDF" and "Export to Excel" buttons to save the results.

## Technologies Used

- Flask
- React
- Selenium
- Webdriver-Manager


