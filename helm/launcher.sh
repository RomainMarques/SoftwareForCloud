#!/bin/sh

# This script is used for the port forwarding of the ingress gateway and get the url of the front

# Start minikube
minikube start --memory=5000 --cpus=4

# Install istio
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update

# Launch the different clusters and gateway
helm install cloud ./helm-cloud

# Port forward the ingress gateway and get the url of the front
bash ./../kubernetes/ingress-forward.sh &
echo To access the website you can go on the following url :
minikube service front --url