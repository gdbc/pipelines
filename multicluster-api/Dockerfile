FROM oraclelinux:8.1

ARG user=flask
ARG group=flask
ARG uid=1001
ARG gid=1001

ENV FLASK_HOME /home/${user}
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$FLASK_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

RUN  mkdir ${FLASK_HOME}/.kube
RUN  mkdir ${FLASK_HOME}/.minikube
COPY api/.kube/config ${FLASK_HOME}/.kube/
COPY api/.minikube/client.key ${FLASK_HOME}/.minikube/ 
COPY api/.minikube/client.crt ${FLASK_HOME}/.minikube/ 
COPY api/.minikube/ca.crt ${FLASK_HOME}/.minikube/ 
COPY api/app.py ${FLASK_HOME}
COPY api/create_pvc.py ${FLASK_HOME}
COPY api/create_pv.py ${FLASK_HOME}
COPY api/delete_pv.py ${FLASK_HOME}
COPY api/delete_pvc.py ${FLASK_HOME}
COPY api/get_pvcs.py ${FLASK_HOME}
COPY api/get_pvs.py ${FLASK_HOME}
COPY api/get_auths.py ${FLASK_HOME}
COPY api/get_tokens.py ${FLASK_HOME}
COPY api/check_pv_rbac.py ${FLASK_HOME}
COPY api/multicluster-listpods.py ${FLASK_HOME}
WORKDIR ${FLASK_HOME}
RUN chown ${user}:${group} app.py
RUN chown ${user}:${group} -R .kube
RUN chown ${user}:${group} -R .minikube
RUN dnf install wget -y && dnf clean all 
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
RUN rpm -vih epel-release* 
RUN dnf install python3-flask python3-pip nfs-utils -y && dnf clean all
RUN pip3 install --upgrade pip
RUN pip3 install kubernetes pick


# Standard Flask port
EXPOSE 5000
USER flask 
ENV USER flask
ENTRYPOINT ["python3", "app.py"]


# sudo podman build --no-cache -t docker.io/gra3m3/nfstest:2 .
# sudo podman push docker.io/gra3m3/nfstest:2
