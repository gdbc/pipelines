FROM oraclelinux:7-slim

ARG user=flask
ARG group=flask
ARG uid=1000
ARG gid=1000

ENV FLASK_HOME /home/${user}
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$FLASK_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

COPY rq/app.py ${FLASK_HOME}
COPY rq/sums.py ${FLASK_HOME}
COPY rq/vmcreate.py ${FLASK_HOME}
COPY rq/checksvc.py ${FLASK_HOME}
COPY rq/get_mets.py ${FLASK_HOME}
COPY rq/get_mets.py ${FLASK_HOME}
RUN cd /etc/yum.repos.d/ && sed -i '0,/addons/! {0,/enabled=0/ s/enabled=0/enabled=1/}' public-yum-ol7.repo
WORKDIR ${FLASK_HOME}
RUN chown ${user}:${group} app.py
RUN yum install -y wget && yum clean all
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -vih epel-release* 
RUN yum install python-flask python-redis python2-pip -y && yum clean all
RUN pip install --upgrade pip
RUN pip install rq
RUN pip install paramiko
RUN pip install prometheus_client flask_prometheus


# Standard Flask port
EXPOSE 5000
USER flask 
ENV USER flask
ENTRYPOINT ["python2", "app.py"]
