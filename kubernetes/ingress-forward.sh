#!/bin/sh
echo Open Ingress at http://localhost:4000/server/getuser/c@c
kubectl -n istio-system port-forward deployment/istio-ingressgateway 4000:8080
