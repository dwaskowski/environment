FROM jenkins:2.7.1
MAINTAINER Dmitrij Waskowski <dymitr@gmail.com>

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

COPY config /root/.ssh/config

ADD ./scripts /home/jenkins/scripts
ADD ./keys /home/jenkins/.ssh
ADD jenkins-crons /etc/cron.d/jenkins-crons

USER root
RUN apt-get -qq update \
    && apt-get -qq upgrade \
    && apt-get -qq install python-pip \
    && apt-get -qq install cron \
    && apt-get -qq install nano

RUN chmod 0644 /etc/cron.d/jenkins-crons \
    && touch /var/log/cron.log \
    && crontab /etc/cron.d/jenkins-crons \
    && cron

RUN pip install python-jenkins
