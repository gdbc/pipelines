FROM oraclelinux:7-slim
RUN cd /etc/yum.repos.d/ && sed -i '0,/addons/! {0,/enabled=0/ s/enabled=0/enabled=1/}' public-yum-ol7.repo
RUN yum install -y openssh-server git unzip zip wget docker && yum clean all
# update sshd settings, create jenkins user, set jenkins user pw, generate ssh keys
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd \
    && mkdir -p /var/run/sshd \
    && useradd -u 1000 -m -s /bin/bash jenkins \
    && echo "jenkins:jenkins" | chpasswd \
    && /usr/bin/ssh-keygen -A  \
    && echo export JAVA_HOME="/`alternatives  --display java | grep best | cut -d "/" -f 2-6`" >> /etc/environment
RUN echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config
RUN sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config
# install docker compose
#RUN curl -L https://github.com/docker/compose/releases/download/1.9.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

# Standard SSH port
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
