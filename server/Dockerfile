FROM node:latest
LABEL authors="romainmarques & antoinelachaud"
WORKDIR /app

# Install dependencies first
COPY package.json /app
RUN npm install

# Copy the rest of the project
COPY . /app

# Launch the server
CMD ["npm", "run", "start"]

EXPOSE 3000