FROM nginx:latest

WORKDIR /etc/nginx/

RUN apt update -y
RUN rm ./conf.d/default.conf
COPY ./nginx.conf conf.d/