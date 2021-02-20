FROM node:lts-alpine

WORKDIR /app/

COPY ./frontend/package*.json ./

RUN npm cache verify

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "dev"]
