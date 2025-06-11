FROM python:3.11

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files to the container
COPY . .

# Open the port
EXPOSE 5000


# Run the app.py

CMD [ "python", "app.py" ]