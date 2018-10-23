FROM oraclelinux:7-slim
RUN yum-config-manager --enable ol7_addons ol7_developer_EPEL ol7_preview

RUN yum -y install openssl-devel python-devel java-1.8.0-openjdk which unzip wget git && \
   wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo && \
   rpm -v --import https://pkg.jenkins.io/redhat/jenkins.io.key && \
    yum -y install jenkins

RUN yum -y install docker-engine kubectl && \
    usermod -aG docker jenkins && \
    yum -y install python2-pip && \
    chown -c jenkins /var/lib/jenkins && \
    chsh -s /bin/bash jenkins && \
    groupmod -g 994 docker

RUN usermod -aG docker jenkins
