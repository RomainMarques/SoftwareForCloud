FROM node:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY . .

# Install the application dependencies
RUN npm install

# Build the React app
RUN npm run build

# Expose the port that the app will run on
EXPOSE 8100

# Define the command to run your application
CMD ["npm", "start"]