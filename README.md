# 🚀 Cloud-Native Flask Application Deployment on AWS EKS

This project demonstrates how to containerize a Flask web application using Docker, push the image to Amazon ECR, and deploy it on Amazon EKS (Elastic Kubernetes Service) using Python automation.
It showcases modern DevOps practices, including containerization, cloud deployment, and Kubernetes orchestration.

---

## 🧩 Project Overview

**Goal:**
To build, containerize, and deploy a Flask-based monitoring application in a cloud-native environment using AWS and Kubernetes.

**Tech Stack:**
- **Backend:** Flask (Python)
- **Containerization:** Docker
- **Cloud Platform:** AWS (ECR & EKS)
- **Orchestration:** Kubernetes
- **Automation:** Python SDKs (`boto3`, `kubernetes`)
- **Visualization:** Plotly, psutil

---

## 🏗️ Part 1: Running the Application Locally

### Step 1: Clone the Repository and cd into it
```
git clone https://github.com/heykirito/monitoring_app.git
cd monitoring_app
```
### Step 2: Install Dependencies
```
pip3 install -r requirements.txt
```

### Step 3: Run the Flask App
```
python3 app.py
```
## 🐳 Part 2: Dockerizing the Application

### Step 1: Create a Dockerfile
### Step 2: Build and Run the Docker Image
```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

## ☁️ Part 3: Push Docker Image to Amazon ECR
### Step 1: Create an ECR Repository (Python)
### Step 2: Push Image to ECR

## ☸️ Part 4: Deploying on Amazon EKS
### Step 1: Create EKS Cluster and Node Group
Use AWS Console or boto3 to create an EKS cluster and node group.

### Step 2: Deploy via Python
## 🔍 Verify Deployment
```
kubectl get deployments -n default
kubectl get pods -n default
kubectl get services -n default


kubectl port-forward service/my-flask-service 5000:5000
```
