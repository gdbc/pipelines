FROM oraclelinux:8.1

ARG user=flask
ARG group=flask
ARG uid=1001
ARG gid=1001

ENV FLASK_HOME /home/${user}
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$FLASK_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

COPY api/app.py ${FLASK_HOME}
WORKDIR ${FLASK_HOME}
RUN chown ${user}:${group} app.py
RUN dnf install -y wget && yum clean all
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN rpm -vih epel-release* 
RUN dnf install python3-flask python3-pip nfs-utils -y && yum clean all
RUN pip3 install --upgrade pip


# Standard Flask port
EXPOSE 5000
USER flask 
ENV USER flask
ENTRYPOINT ["python3", "app.py"]


# sudo podman build --no-cache -t docker.io/gra3m3/nfstest:2 .
# sudo podman push docker.io/gra3m3/nfstest:2
