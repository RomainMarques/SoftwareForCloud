#!/bin/sh
echo Open Ingress at http://localhost:31758/
kubectl -n istio-system port-forward deployment/istio-ingressgateway 3000:3000
