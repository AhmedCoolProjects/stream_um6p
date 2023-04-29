FROM python:3.8

COPY requirements.txt .

# Install Streamlit
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the app code to the container
COPY . /app

# Expose the port where the app will run
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

