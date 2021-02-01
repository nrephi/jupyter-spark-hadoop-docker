FROM hdfs-base
ENV HADOOP_CONF_DIR=/etc/hadoop
COPY run.sh /run.sh
RUN chmod a+x run.sh

ENTRYPOINT ["sh", "-c", "service ssh restart; ./run.sh; sleep infinity"]