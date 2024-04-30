# CI/CD Pipeline for Mini Calculator Interpreter
This repository contains the source code for the Mini Calculator Interpreter along with a CI/CD pipeline implemented using GitHub Actions. The pipeline automates the build, test, and deployment processes for the Mini Calculator Interpreter application.

Features
Automated build process using GitHub Actions.
Automated testing of the application using Python's unittest framework.
Deployment to a production environment using Docker.
Usage
To use the CI/CD pipeline, follow these steps:

Clone the Repository: Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/your-username/MiniCalculatorInterpreter.git
Install Dependencies: Install the necessary dependencies for the project. Make sure you have Python and Docker installed on your machine.
Run Tests: Run the automated tests using the following command:
bash
Copy code
python -m unittest MiniCalculatorInterpreter-master/test.py
Build Docker Image: Build the Docker image for the application using the provided Dockerfile.
bash
Copy code
docker build -t calculator-app .
Run Docker Container: Run the Docker container to deploy the application locally.
bash
Copy code
docker run -d -p 8080:80 calculator-app
Access the Application: Access the application by navigating to http://localhost:8080 in your web browser.
Continuous Integration (CI)
The CI pipeline is triggered automatically on every push to the main branch. It consists of the following stages:

Build: The source code is checked out, and the Docker image for the application is built.
Test: The automated tests are executed to ensure the correctness of the application.
Continuous Deployment (CD)
The CD pipeline is triggered after a successful build and test. It consists of the following stages:

Deployment: The Docker image is deployed to a production environment.
Contributing
Contributions to the Mini Calculator Interpreter project are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
