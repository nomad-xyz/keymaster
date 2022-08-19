FROM node:16
# ENV NODE_ENV=production

ARG GIT_COMMIT
ENV GIT_COMMIT=$GIT_COMMIT

WORKDIR /app

COPY tsconfig.json \
     package.json \
     src \
     ./

RUN yarn install

CMD [ "yarn", "start" ]