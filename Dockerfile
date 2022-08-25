FROM node:18.7.0

ARG GIT_COMMIT
ENV GIT_COMMIT=$GIT_COMMIT

WORKDIR /app

COPY tsconfig.json \
     package.json \
     src \
     ./

RUN yarn install

CMD [ "yarn", "start" ]