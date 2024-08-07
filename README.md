# inSkrap Project Documentation

## Overview
The inSkrap project is a web application designed to scrape data from Google Maps based on user-provided keywords and locations. The project includes a frontend built with React and a backend built with Flask. This documentation provides a comprehensive guide on the setup, development, and deployment process, including Docker configuration for containerization.

## Backend Setup

### Python Environment Setup

1. **Install Python Packages:**
   - Install the necessary packages listed in `requirements.txt` to set up the Python environment.

2. **Flask Application:**
   - The backend uses Flask to handle API requests. The Flask app is configured to handle scraping requests and return results.

3. **Google Maps Scraper:**
   - The scraper uses Selenium for browser automation to scrape data from Google Maps.

### Docker Configuration for Backend

1. **Dockerfile for Backend:**
   - The backend Dockerfile uses the official Python image.
   - It sets up the working directory, installs required packages, and sets up Chrome and ChromeDriver for Selenium.
   - It exposes the Flask application port for external access.

## Frontend Setup

### React Environment Setup

1. **Install Node Packages:**
   - Install the necessary Node packages listed in `package.json` to set up the React environment.

2. **React Components:**
   - The frontend consists of various components like the search page and loader.
   - The search page handles user inputs for keywords and location and displays results after making API calls to the backend.

### Docker Configuration for Frontend

1. **Dockerfile for Frontend:**
   - The frontend Dockerfile uses the official Node.js image.
   - It sets up the working directory, installs dependencies, and builds the application using Vite.
   - It exposes the port for the frontend application.

## Combined Docker Configuration

### Docker Compose Setup

1. **docker-compose.yml:**
   - The Docker Compose configuration file sets up both the backend and frontend services.
   - It ensures both services are built and run together in a network, making it easy to manage and deploy the entire application.

## Loader Integration

### Loader Component

1. **CSS Styling:**
   - The loader component is styled to appear centered on the search page when data is being fetched from the backend.

2. **Conditional Rendering:**
   - The loader is conditionally rendered based on the loading state, which is toggled when the API call is made and completed.

### Integration in Search Page

1. **Show Loader:**
   - The loader is displayed when the form is submitted and the API call is in progress.
   
2. **Hide Loader:**
   - The loader is hidden once the API call completes and the results are available.

## Running the Docker Containers

### Steps to Build and Run the Docker Containers

1. **Navigate to the Project Directory:**
   - Open a terminal and navigate to the root directory of the project.

2. **Build the Docker Containers:**
   - Run the following command to build the Docker containers for both the frontend and backend:
     ```
     docker-compose build
     ```

3. **Start the Docker Containers:**
   - Run the following command to start the Docker containers:
     ```
     docker-compose up
     ```

4. **Access the Application:**
   - Open a web browser and navigate to the following URLs to access the frontend and backend:
     - Frontend: `http://localhost:3000`
     - Backend: `http://localhost:5001`

### Stopping the Docker Containers

1. **Stop the Containers:**
   - To stop the running Docker containers, press `CTRL+C` in the terminal where the containers are running.

2. **Remove the Containers:**
   - Run the following command to remove the stopped containers:
     ```
     docker-compose down
     ```

By following this documentation, you should be able to set up, develop, and deploy the inSkrap project efficiently. For any issues, ensure to check logs and verify the configuration settings.