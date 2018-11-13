FROM gra3m3/ol-jenkins-base:latest

ENV JENKINS_HOME /var/lib/jenkins
USER jenkins
WORKDIR ${JENKINS_HOME}

RUN mkdir -p ${JENKINS_HOME}/users/admin
RUN mkdir -p ${JENKINS_HOME}/jobs/ol-Jenkins/
RUN mkdir -p ${JENKINS_HOME}/jobs/ol-jenkins-base/
RUN mkdir -p ${JENKINS_HOME}/jobs/ol-slave/
RUN mkdir -p ${JENKINS_HOME}/jobs/rancher-deploy/
RUN mkdir -p ${JENKINS_HOME}/jobs/build-host/
RUN mkdir -p ${JENKINS_HOME}/jobs/getsshkey/

COPY jenkins_config.xml /var/lib/jenkins/config.xml
COPY getsshkey.xml ${JENKINS_HOME}/jobs/getsshkey/config.xml
COPY admin_config.xml ${JENKINS_HOME}/users/admin/config.xml
COPY job_jenkins_config.xml ${JENKINS_HOME}/jobs/ol-Jenkins/config.xml
COPY rancher-deploy.xml ${JENKINS_HOME}/jobs/rancher-deploy/config.xml
COPY ol-jenkins-base.xml ${JENKINS_HOME}/jobs/ol-jenkins-base/config.xml 
COPY ol-slave.xml ${JENKINS_HOME}/jobs/ol-slave/config.xml
COPY build-host.xml ${JENKINS_HOME}/jobs/build-host/config.xml
COPY rke ${JENKINS_HOME}/
RUN ln -s /var/lib/jenkins/war/WEB-INF/jenkins-cli.jar jenkins-cli.jar
ADD http://updates.jenkins-ci.org/latest/git.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/python.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/publish-over-ssh.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/junit.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/scm-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/git-client.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/credentials.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/workflow-scm-step.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/matrix-project.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/structs.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/workflow-step-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/mailer.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/ssh.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/scp.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/ssh-credentials.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/ssh-steps.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/ssh-agent.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/jsch.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/build-pipeline-plugin.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/docker-commons.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/apache-httpcomponents-client-4-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/token-macro.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/bouncycastle-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/ssh-slaves.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/docker-java-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/durable-task.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/tap.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/docker-plugin.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/authentication-tokens.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/credentials-binding.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/workflow-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/script-security.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/jsch.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/display-url-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/jackson2-api.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/plain-credentials.hpi ${JENKINS_HOME}/plugins/
ADD http://updates.jenkins-ci.org/latest/plain-credentials.hpi ${JENKINS_HOME}/plugins/

USER root
RUN chown -R jenkins.jenkins ${JENKINS_HOME}/plugins
RUN chown -R jenkins.jenkins ${JENKINS_HOME}/rke
RUN chmod 755 ${JENKINS_HOME}/rke
COPY scp.py /usr/local/bin/
RUN chmod 755 /usr/local/bin/scp.py

USER jenkins
ENV USER jenkins
CMD ["java", "-jar", "/usr/lib/jenkins/jenkins.war"]
