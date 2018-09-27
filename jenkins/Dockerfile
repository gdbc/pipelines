FROM jenkins/jenkins
WORKDIR /var/jenkins_home
COPY plugins.txt /var/jenkins_home
RUN /usr/local/bin/install-plugins.sh < plugins.txt
