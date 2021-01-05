

import requests
# https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/
print('Téléchargement du fichier par département ')

url = 'https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7'
r = requests.get(url)

with open('/opt/workspace/data/status-dep.csv', 'wb') as f:
    f.write(r.content)
print("Téléchargement terminé")



# https://www.data.gouv.fr/fr/datasets/departements-de-france/
print('Téléchargement de la liste des départements ')

url = 'https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254'
r = requests.get(url)

with open('/opt/workspace/data/departements.csv', 'wb') as f:
    f.write(r.content)
print("Téléchargement terminé")



# Création du SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.memory", "512m").\
        getOrCreate()


# Création de la table de départements
departements = spark.read.csv(
    "/opt/workspace/data/departements.csv", header=True, mode="DROPMALFORMED"
)
departements.show()


# Création de la table des infos départements
departements = spark.read.csv(
    "/opt/workspace/data/departements.csv", header=True, mode="DROPMALFORMED"
)
departements.show()


# Création de la table des infos status par département
status_dep = spark.read.csv(
    "/opt/workspace/data/status-dep.csv", header=True, mode="DROPMALFORMED"
)
status_dep.filter((status_dep.dep == 62) | (status_dep.dep == 59) | (status_dep.dep >= 75) | (status_dep.dep <= 95)).show()

nord = status_dep.filter((status_dep.dep == 62) | (status_dep.dep == 59) | ((status_dep.dep >= 75) & (status_dep.dep <= 95)))
nord = nord.groupBy("dep","jour").agg({"hosp": "sum", "rea": "sum", "rad": "sum"})\
  .withColumnRenamed("SUM(hosp)", "hosp") \
  .withColumnRenamed("SUM(rea)", "rea") \
  .withColumnRenamed("SUM(rad)", "rad")

full_info = nord.join(departements, departements.code_departement == nord.dep)
full_info = full_info.orderBy('jour', ascending=True)
full_info.select("jour", "hosp", "rea", "rad").show()


import matplotlib.pyplot as plt
pandas_covid = full_info.toPandas()
pandas_covid.set_index(['jour', 'nom_departement'], inplace=True);
pandas_covid.plot(kind='line',figsize=(22,8));
