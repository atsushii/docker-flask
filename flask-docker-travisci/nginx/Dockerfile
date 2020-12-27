FROM nginx:1.17-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./flask-docker-travisci/nginx/nginx.conf /etc/nginx/conf.d

EXPOSE 80
