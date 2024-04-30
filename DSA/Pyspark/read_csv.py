from pyspark.sql import *
import os

spark = SparkSession.builder.appName("read csv").getOrCreate()

# print(os.getcwd())


player_df = spark.read.csv("FullData.csv", header=True, inferSchema=True)


