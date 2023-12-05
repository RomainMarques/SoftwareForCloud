# Step 1 : Launch DockerCompose file
docker compose up -d

# Step 2 : Tag the images created and then push it, ex :
#docker tag 336e8f7ed40e azarel9/softwareforcloud-server:0.1
#docker tag 336e8f7ed40e azarel9/softwareforcloud-mysql:0.1
#docker tag azarel9/front-app:0.1

# Step 3 : Push the images, ex :
#docker push azarel9/softwareforcloud-mysql:0.1

# Step 4, se placer dans le dossier kubernetes :
cd ./kubernetes
#kubectl apply -f database_deployment.yaml
#kubectl apply -f database_service.yaml
#kubectl apply -f server_deployment.yaml
#kubectl apply -f server_service.yaml
#minikube service mysql-deployment --url
# Pour se connecter au serveur pour l'instant :
#minikube service server --url

#Step 5 :
#minikube addons enable ingress
#minikube tunnel
#curl --resolve "www.example.com:3000:127.0.0.1" -i http://www.example.com

