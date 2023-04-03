# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /Telecome-churn-dataset

# Copy the current directory contents into the container at /app
COPY . /Telecome-churn-dataset

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the command to start Streamlit when the container launches
CMD ["streamlit", "run", "Tlc_ch_app1.py"]
