FROM oraclelinux:7-slim

ARG user=flask
ARG group=flask
ARG uid=1000
ARG gid=1000

ARG SSH_USER=test
ARG SSH_PASS=test

ENV FLASK_HOME /home/${user}
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$FLASK_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

COPY app/app.py ${FLASK_HOME}
COPY app/sums.py ${FLASK_HOME}
COPY app/ssh_lib.py ${FLASK_HOME}
COPY app/sshgroup.py ${FLASK_HOME}
COPY app/convert_hname.py ${FLASK_HOME}
COPY app/update_sshgroup.py ${FLASK_HOME}
COPY app/git_pull.py ${FLASK_HOME}
COPY app/git_push.py ${FLASK_HOME}
COPY app/get_vars.py ${FLASK_HOME}
COPY config.json ${FLASK_HOME}
COPY app/get_mets.py ${FLASK_HOME}
RUN cd /etc/yum.repos.d/ && sed -i '0,/addons/! {0,/enabled=0/ s/enabled=0/enabled=1/}' public-yum-ol7.repo
WORKDIR ${FLASK_HOME}
RUN chown ${user}:${group} app.py
RUN yum install -y wget && yum clean all
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -vih epel-release* 
RUN yum install python-flask python-redis python2-pip git -y && yum clean all
RUN pip install --upgrade pip
RUN pip install rq fabric2 prometheus_client flask_prometheus gitpython ruamel.yaml pathlib


# Standard Flask port
EXPOSE 5000
USER flask 
ENV USER flask
ENTRYPOINT ["python2", "app.py"]
