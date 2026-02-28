# Assignment 6 — Kubernetes Deployment

## Overview
This project deploys an Iris machine learning classification model using Docker and Kubernetes. The model is served through a Flask API and deployed to a local Kubernetes cluster using Minikube.

## Technologies
- Python
- Flask
- Scikit-learn
- Docker
- Kubernetes
- Minikube

## Endpoints

### Health Check
GET /health  
Returns:
{"status":"ok"}

### Predict
POST /predict

Example:
{
 "features":[5.1,3.5,1.4,0.2]
}

Response:
{"prediction":0}

## Docker Run

Build:
docker build -t iris-api:1.0 .

Run:
docker run -p 8080:8080 iris-api:1.0

Test:
curl http://127.0.0.1:8080/health

## Kubernetes Deployment

Start cluster:
minikube start

Build & load image:
docker build -t iris-api:1.0 .
minikube image load iris-api:1.0

Deploy:
kubectl apply -f k8s/

Open service:
minikube service iris-api-svc

## Scaling
kubectl scale deployment iris-api --replicas=3

