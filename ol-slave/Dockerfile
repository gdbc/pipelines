FROM oraclelinux:7-slim

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

ENV JENKINS_HOME /home/${user}
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk
ENV JRE_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.181-3.b13.el7_5.x86_64/jre

# Jenkins is run with user `jenkins`, uid = 1000
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

RUN chown -R ${user}:${user} /home/${user}

# install docker compose
#RUN curl -L https://github.com/docker/compose/releases/download/1.9.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose


RUN cd /etc/yum.repos.d/ && sed -i '0,/addons/! {0,/enabled=0/ s/enabled=0/enabled=1/}' public-yum-ol7.repo
RUN yum install -y openssh-server git unzip zip docker java-1.8.0-openjdk.x86_64 java-1.8.0-openjdk.i686 && yum clean all
# update sshd settings, create jenkins user, set jenkins user pw, generate ssh keys
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd \
    && mkdir -p /var/run/sshd \
    && /usr/bin/ssh-keygen -A  
COPY setup-sshd /usr/local/bin/
RUN chmod 777 /usr/local/bin/setup-sshd
RUN mkdir /home/jenkins/jdk/bin/ -p
RUN mkdir /root/jdk/bin/ -p
RUN ln -s /usr/lib/jvm/jre-1.8.0-openjdk/bin/java /home/jenkins/jdk/bin/java
RUN ln -s /usr/lib/jvm/jre-1.8.0-openjdk/bin/java /root/jdk/bin/java
RUN echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config
RUN echo "AcceptEnv LANG LC_*" >> /etc/ssh/sshd_config
RUN echo "PrintMotd no" >> /etc/ssh/sshd_config
RUN sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config


# Standard SSH port
EXPOSE 22
#CMD ["/usr/sbin/sshd", "-D", "-e"]
ENTRYPOINT ["setup-sshd"]
