FROM gra3m3/ssh-slave
RUN echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config
RUN apt-get update
RUN apt-get install apt-transport-https software-properties-common curl ca-certificates -y
#RUN apt-key adv --keyserver https://download.docker.com/linux/debian/gpg --recv
RUN add-apt-repository "deb http://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install docker-ce -y --allow-unauthenticated 
