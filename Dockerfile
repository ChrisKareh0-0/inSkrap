# # Stage 1: Build Backend
FROM python:3.8-slim as backend-app-builder

# Set the working directory
WORKDIR /app

# Copy only the requirements file initially to leverage Docker cache
COPY backend-app/requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend-app application code
COPY backend-app/ .

# Stage 2: Build Frontend
FROM node:18-alpine as frontend-builder

# Set the working directory
WORKDIR /app/inskrap-frontend

# Copy frontend package.json and package-lock.json files
COPY inskrap-frontend/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the frontend source code
COPY inskrap-frontend/ .

# Build the frontend application using Vite with additional logging
RUN echo "Running npm run build" && npm run build && echo "Build completed successfully" || (echo "Build failed" && exit 1)

# Debug step to list all directories and files after build
RUN echo "Listing /app/inskrap-frontend contents:" && find /app/inskrap-frontend -type d -print && ls -la /app/inskrap-frontend

# Verify the content of the dist directory after build
RUN echo "Checking dist directory contents:" && ls -la /app/inskrap-frontend/dist

# Stage 3: Final Image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy backend-app code from backend-app-builder stage
COPY --from=backend-app-builder /app /app

# Copy frontend build from frontend-builder stage
COPY --from=frontend-builder /app/inskrap-frontend/dist /app/inskrap-frontend/dist

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (adjust as needed)
EXPOSE 80

# Command to run the application (adjust as needed)
CMD ["python", "app.py"]
