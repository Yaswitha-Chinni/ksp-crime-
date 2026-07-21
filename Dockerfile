# Use the official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port from the environment variable (required by Cloud Run)
EXPOSE $PORT

# Run Streamlit on the specified port
CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
