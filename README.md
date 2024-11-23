# Health Calculator Microservice

This project was created using a template developed by **Ali Mokh**. It is a Python-based microservice that calculates health metrics like **BMI (Body Mass Index)** and **BMR (Basal Metabolic Rate)** using a REST API. It is containerized with Docker, managed with Makefile commands, and includes a CI/CD pipeline for deployment to Azure.

---

## Features

- **Flask REST API Endpoints**:
  - `/bmi`: Calculate BMI using height (meters) and weight (kilograms).
  - `/bmr`: Calculate BMR using height (cm), weight (kg), age, and gender.
- **Containerized with Docker** for easy deployment and scaling.
- **Makefile** for automation of tasks like building, running, and testing.
- **CI/CD Pipeline** using GitHub Actions for automated testing and deployment.
- **Deployed to Azure App Service** for hosting.

---

## API Endpoints

### `/bmi`

- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "height": 1.75,
    "weight": 70
  }
  ```
- **Response**:
  ```json
  {
    "bmi": 22.86
  }
  ```

### `/bmr`

- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "height": 175,
    "weight": 70,
    "age": 25,
    "gender": "male"
  }
  ```
- **Response**:
  ```json
  {
    "bmi": 1705.54
  }
  ```

---

## Running the App

### Access the App Locally

- **Build the Docker Image**:
  Make sure Docker is installed and running on your system, then run:

  ```bash
  docker build -t health-calculator .
  ```

- **Run the Docker Container**:
  Start the container using:

  ```bash
  docker run -p 5000:5000 health-calculator
  ```

- **Access the App**:
  Open your browser and go to http://localhost:5000

### Access the Deployed App

Open your browser and go to https://health-calculator-brgxgggqg8btfahf.westeurope-01.azurewebsites.net/
