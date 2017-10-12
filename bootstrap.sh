#!/usr/bin/env bash

# Docker install
apt-get -qq purge lxc-docker*
apt-get -qq purge docker.io*
apt-get -qq update
apt-get -qq install apt-transport-https ca-certificates
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list
apt-get -qq update
apt-get -qq install docker-engine curl python-pip cron nano git htop

# Install php 7.0
echo 'deb http://packages.dotdeb.org jessie all' > /etc/apt/sources.list.d/dotdeb.list
apt-get -qq install apt-transport-https
curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -
apt-get -qq update
apt-get -qq install php7.0 php7.0-xml php7.0-mysql


# Downloading and Installing Composer
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

service docker start

# Docker compose
curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo "
alias dc='_(){ docker-compose \$*; }; _'
alias d='_(){ docker \$*; }; _'
" > /root/.bash_profile

echo "
alias dc='_(){ docker-compose \$*; }; _'
alias d='_(){ docker \$*; }; _'
" > /home/vagrant/.bash_profile

chown vagrant: /home/vagrant/.bash_profile
