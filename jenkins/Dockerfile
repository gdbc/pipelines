FROM jenkins/jenkins
WORKDIR /var/jenkins_home
COPY plugins.txt /var/jenkins_home
COPY user_config.xml /var/jenkins_home/users/admin/config.xml
COPY config.xml /var/jenkins_home/config.xml
RUN /usr/local/bin/install-plugins.sh < plugins.txt
