FROM gra3m3/ol-jenkins-yum:1

USER jenkins
ENV JENKINS_HOME /var/lib/jenkins
RUN mkdir -p ${JENKINS_HOME}/users/admin

COPY jenkins_config.xml /var/lib/jenkins/.jenkins/config.xml
COPY jenkins_config.xml /var/lib/jenkins/config.xml
COPY admin_config.xml ${JENKINS_HOME}/users/admin/config.xml
ENV USER jenkins

CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]
