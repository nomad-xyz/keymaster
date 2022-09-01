FROM node:18.8.0

ARG GIT_COMMIT
ENV GIT_COMMIT=$GIT_COMMIT

WORKDIR /app

COPY tsconfig.json \
     package.json \
     src \
     ./

RUN apt update -y \
     && apt upgrade -y \
     && yarn install

CMD [ "yarn", "start" ]