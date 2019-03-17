FROM dhost/jwt

ARG user=flask
ARG group=flask
ARG uid=1000
ARG gid=1000

ENV FLASK_HOME /connexion/examples/openapi3/jwt/

#RUN groupadd -g ${gid} ${group}  \
#  && useradd -d "$FLASK_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

USER root
RUN pip3 uninstall -y connexion
RUN pip3 install connexion flask_sqlalchemy 
RUN pip3 install connexion[swagger-ui]

COPY app.py $FLASK_HOME
COPY openapi.yaml $FLASK_HOME
COPY auth_db2.py $FLASK_HOME

#RUN chown ${user} -R /connexion 

# Standard Flask port
EXPOSE 8080
USER flask 
ENV USER flask
ENTRYPOINT ["python3", "/connexion/examples/openapi3/jwt/app.py"]

