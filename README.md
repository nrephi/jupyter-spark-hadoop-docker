# Apache Spark Standalone Cluster on Docker

> The project was featured on an **[article](https://www.mongodb.com/blog/post/getting-started-with-mongodb-pyspark-and-jupyter-notebook)** at **MongoDB** official tech blog! :scream:

> The project just got its own **[article](https://towardsdatascience.com/apache-spark-cluster-on-docker-ft-a-juyterlab-interface-418383c95445)** at **Towards Data Science** Medium blog! :sparkles:

## Introduction

This project gives you an **Apache Spark** cluster in standalone mode with a **JupyterLab** interface built on top of **Docker**.
Learn Apache Spark through its **Scala**, **Python** (PySpark) and **R** (SparkR) API by running the Jupyter [notebooks](build/workspace/) with examples on how to read, process and write data.

<p align="center"><img src="docs/image/cluster-architecture.png"></p>

## TL;DR

```bash
curl -LO https://raw.githubusercontent.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker/master/docker-compose.yml
docker-compose up
```

## Contents

- [Quick Start](#quick-start)
- [Tech Stack](#tech-stack)
- [Metrics](#metrics)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [Support](#support)

## <a name="quick-start"></a>Quick Start

### Cluster overview

| Application     | URL                                      | Description                                                |
| --------------- | ---------------------------------------- | ---------------------------------------------------------- |
| JupyterLab      | [localhost:8888](http://localhost:8888/) | Cluster interface with built-in Jupyter notebooks          |
| Spark Driver    | [localhost:4040](http://localhost:4040/) | Spark Driver web ui                                        |
| Spark Master    | [localhost:8080](http://localhost:8080/) | Spark Master node                                          |
| Spark Worker I  | [localhost:8081](http://localhost:8081/) | Spark Worker node with 1 core and 512m of memory (default) |
| Spark Worker II | [localhost:8082](http://localhost:8082/) | Spark Worker node with 1 core and 512m of memory (default) |

### Prerequisites

 - Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/), check **infra** [supported versions](#tech-stack)

### Download from Docker Hub (easier)

1. Download the [docker compose](docker-compose.yml) file;

```bash
curl -LO https://raw.githubusercontent.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker/master/docker-compose.yml
```

2. Edit the [docker compose](docker-compose.yml) file with your favorite tech stack version, check **apps** [supported versions](#tech-stack);
3. Start the cluster;

```bash
docker-compose up
```

4. Run Apache Spark code using the provided Jupyter [notebooks](build/workspace/) with Scala, PySpark and SparkR examples;
5. Stop the cluster by typing `ctrl+c` on the terminal;
6. Run step 3 to restart the cluster.

### Build from your local machine

> **Note**: Local build is currently only supported on Linux OS distributions.

1. Download the source code or clone the repository;
2. Move to the build directory;

```bash
cd build
```

3. Edit the [build.yml](build/build.yml) file with your favorite tech stack version;
4. Match those version on the [docker compose](build/docker-compose.yml) file;
5. Build up the images;

```bash
chmod +x build.sh ; ./build.sh
```

6. Start the cluster;

```bash
docker-compose up
```

7. Run Apache Spark code using the provided Jupyter [notebooks](build/workspace/) with Scala, PySpark and SparkR examples;
8. Stop the cluster by typing `ctrl+c` on the terminal;
9. Run step 6 to restart the cluster.

## <a name="tech-stack"></a>Tech Stack

- Infra

| Component      | Version |
| -------------- | ------- |
| Docker Engine  | 1.13.0+ |
| Docker Compose | 1.10.0+ |

- Languages and Kernels

| Spark | Hadoop | Scala   | [Scala Kernel](https://almond.sh/) | Python | [Python Kernel](https://ipython.org/) | R     | [R Kernel](https://irkernel.github.io/) |
| ----- | ------ | ------- | ---------------------------------- | ------ | ------------------------------------- | ----- | --------------------------------------- |
| 3.x   | 3.2    | 2.12.10 | 0.10.9                             | 3.7.3  | 7.19.0                                 | 3.5.2 | 1.1.1                                   |
| 2.x   | 2.7    | 2.11.12 | 0.6.0                              | 3.7.3  | 7.19.0                                 | 3.5.2 | 1.1.1                                   |

- Apps

| Component      | Version                 | Docker Tag                                           |
| -------------- | ----------------------- | ---------------------------------------------------- |
| Apache Spark   | 2.4.0 \| 2.4.4 \| 3.0.0 | **\<spark-version>**                                 |
| JupyterLab     | 2.1.4 \| 3.0.0          | **\<jupyterlab-version>**-spark-**\<spark-version>** |

## <a name="metrics"></a>Metrics

| Image                                                          | Size                                                                                           | Downloads                                                                 |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |