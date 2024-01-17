#!/bin/sh

# This script is used for the port forwarding of the ingress gateway and get the url of the front

# Start minikube
#minikube start --memory=5000 --cpus=4

bash ./../kubernetes/ingress-forward.sh &
echo To access the website you can go on the following url :
minikube service front --url