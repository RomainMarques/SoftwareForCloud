FROM mysql:latest
LABEL authors="romainmarques & antoinelachaud"
# Informations d'identification pour la base de données
ARG MYSQL_ROOT_PASSWORD
ARG MYSQL_DATABASE

ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
ENV MYSQL_DATABASE=$MYSQL_DATABASE
# Port sur lequel MySQL écoutera
EXPOSE 3306

# Copier les scripts SQL personnalisés dans le conteneur
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/