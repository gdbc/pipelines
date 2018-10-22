FROM jenkins/jenkins
WORKDIR /var/jenkins_home
ENV JAVA_OPTS -Dhudson.plugins.sshslaves.SSHLauncher.trackCredentials=false 
COPY plugins.txt /var/jenkins_home
COPY user_config.xml /var/jenkins_home/users/admin/config.xml
COPY config.xml /var/jenkins_home/config.xml
USER root
RUN mkdir -p /var/jenkins_home/jobs/jenkins
RUN mkdir -p /var/jenkins_home/jobs/ssh-slave
RUN mkdir -p /var/jenkins_home/jobs/ol-ssh-slave
COPY jenkins_config.xml /var/jenkins_home/jobs/jenkins/config.xml
COPY  ssh-slave_config.xml /var/jenkins_home/jobs/ssh-slave/config.xml
COPY  ol-slave_config.xml /var/jenkins_home/jobs/ol-ssh-slave/config.xml
RUN chown -R jenkins:jenkins /var/jenkins_home/jobs/jenkins
RUN chown -R jenkins:jenkins /var/jenkins_home/jobs/ssh-slave
RUN chown -R jenkins:jenkins /var/jenkins_home/jobs/ol-ssh-slave
RUN /usr/local/bin/install-plugins.sh < plugins.txt
