FROM php:5.6-cli
RUN apt-get update \
    && docker-php-ext-install mysql \
    && docker-php-ext-install pdo_mysql \
    && echo "upload_max_filesize = 10M;" >> /usr/local/etc/php/conf.d/uploads.ini
ADD . /web
