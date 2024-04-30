# Use the official Python image from Docker Hub
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python -m unittest test.py
CMD ["python", "calculator.py"]
EXPOSE 8000
