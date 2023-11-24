FROM mysql:latest
LABEL authors="romainmarques & antoinelachaud"

ENV MYSQL_ROOT_PASSWORD=Azerty123
ENV MYSQL_DATABASE=projet_cloud
# Port sur lequel MySQL écoutera
EXPOSE 3306

# Copier les scripts SQL personnalisés dans le conteneur
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/