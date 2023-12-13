#!/bin/sh
echo Open Ingress at http://localhost:3000/server/getuser/c@c
kubectl -n istio-system port-forward deployment/istio-ingressgateway 3000:8080
