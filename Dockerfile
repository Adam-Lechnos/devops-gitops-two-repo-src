# Step 1: Use an official lightweight Python runtime as a parent image
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of your local code into the container
COPY . .

# Step 5: Inform Docker that the container listens on port 5000
EXPOSE 5000

# Step 6: Define the command to run your app
CMD ["python", "app.py"]