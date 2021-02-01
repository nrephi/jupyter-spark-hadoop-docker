FROM openjdk:8u222-stretch

RUN apt-get update && apt-get install -y software-properties-common ssh net-tools ca-certificates tar rsync sed

# passwordless ssh
RUN ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa
RUN mkdir -p /root/.ssh
COPY config /root/.ssh/
#RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
RUN chmod 0600 ~/.ssh/authorized_keys

RUN wget --no-verbose http://apache-mirror.8birdsvideo.com/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz && tar -xvzf hadoop-2.7.7.tar.gz && mv hadoop-2.7.7 hadoop && rm hadoop-2.7.7.tar.gz && rm -rf hadoop/share/doc/*
RUN ln -s /hadoop/etc/hadoop /etc/hadoop
RUN mkdir -p /logs
RUN mkdir /hadoop-data

ENV HADOOP_CONF_DIR=/etc/hadoop
ENV PATH /hadoop/bin/:$PATH

COPY core-site.xml /etc/hadoop/
COPY hdfs-site.xml /etc/hadoop/
COPY hadoop-env.sh /etc/hadoop/