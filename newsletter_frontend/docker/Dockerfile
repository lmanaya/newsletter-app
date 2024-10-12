FROM node:16 AS build

ARG WEB_WORKING_DIRECTORY

WORKDIR ${WEB_WORKING_DIRECTORY}

COPY ../package*.json ./

RUN npm install

COPY .. .

RUN npm run build

FROM nginx:alpine

ARG WEB_WORKING_DIRECTORY

COPY --from=build ${WEB_WORKING_DIRECTORY}/dist /usr/share/nginx/html
