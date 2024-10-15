FROM node:16 AS build

ARG WEB_WORKING_DIRECTORY

WORKDIR ${WEB_WORKING_DIRECTORY}

COPY ../package*.json ./

RUN npm install --no-cache

COPY .. .
