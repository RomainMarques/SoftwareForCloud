FROM node:alpine
LABEL authors="romainmarques & antoinelachaud"
WORKDIR /app

COPY package*.json ./
RUN npm install
RUN npm rebuild
COPY . .
EXPOSE 3000

CMD ["npm", "start"]