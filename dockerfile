# Use the official Python image from Docker Hub
FROM python:3.9-slim
WORKDIR /app
COPY MiniCalculatorInterpreter-master/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
CMD ["python", "calculator.py"]
EXPOSE 8000
