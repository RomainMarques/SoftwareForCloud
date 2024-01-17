# Project Software For Cloud

## Description

This project is based on the "Bibliotech" project. Link : https://github.com/PlugNPush/BiblioTech

The goal of this project is to deploy the different microservices (the database, the server, the recommendation and the front) 
of the project Bibliotech on kubernetes.

It is not working on Windows as the images are built on macOS.

## Installation

You need to have installed on your computer :
- Docker
- Minikube
- Kubectl
- istio (a service mesh) : https://istio.io/latest/docs/setup/getting-started/
- Helm : https://helm.sh/docs/intro/install/

## Deployment

To deploy the project, you need to run the following command :

```bash
cd ./kubernetes
bash launcher.sh
```

It will launch minikube, then create the different clusters and give you the ip of the front in which it is accessible.

## Description of the project

The project is composed of 4 microservices all communicating through a Rest API :
- The database : it is a MySql database with values already inserted in it.
- The server : it is a node.js server that will communicate with the database.
- The recommendation : it is a python server that will return recommendations.
- The front : it is a React front that will display the books and the recommendations of the user. I communicate with the server and the recommendation services.

So we have four kubernetes files to create the deployments and the services for each microservice.

We also use istio for different reasons :
- To create a gateway to access the different services.
- To create a virtual service to redirect the traffic to the different services and using the same url as basis.
- To solve Cors problems between the front end and the server.

## Helm

Run the following command to install istio on helm :

```bash
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
```