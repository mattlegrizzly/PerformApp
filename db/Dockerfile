FROM debian:latest

#Install Cron
RUN apt-get update
RUN apt-get -y install postgresql-client cron

# Add the script to the Docker Image
ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]