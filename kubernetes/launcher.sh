#!/bin/sh

# This script is used to launch the kubernetes cluster and the gateway

# Start minikube
#minikube start --memory=5000 --cpus=4

# Launch the different clusters and gateway
kubectl apply -f ./gateway.yaml
kubectl apply -f ./database.yaml
kubectl apply -f ./server.yaml
kubectl apply -f ./recommendations.yaml
kubectl apply -f ./front.yaml

bash ./ingress-forward.sh &

# Wait for the ingress to be ready
sleep 1
echo To access the website you can go on the following url :
minikube service front --url