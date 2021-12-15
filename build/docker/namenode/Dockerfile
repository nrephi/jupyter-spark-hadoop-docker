ARG debian_buster_image_tag=8-jre-slim
FROM openjdk:${debian_buster_image_tag}

# -- Layer: Image Metadata

ARG build_date

LABEL org.label-schema.build-date=${build_date}
LABEL org.label-schema.name="Apache Spark Standalone Cluster on Docker - Cluster Base Image"
LABEL org.label-schema.description="Cluster base image shipped with Python, Scala and a shared workspace folder"
LABEL org.label-schema.url="https://github.com/andre-marcos-perez/spark-cluster-on-docker"
LABEL org.label-schema.schema-version="1.0"



FROM hdfs-base
ENV HADOOP_CONF_DIR=/etc/hadoop
COPY run.sh /run.sh
RUN chmod a+x run.sh

ENTRYPOINT ["sh", "-c", "service ssh restart; ./run.sh; sleep infinity"]