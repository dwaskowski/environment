FROM php:7.0-cli
RUN apt-get update \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install pdo_mysqli 
ADD . /web

