from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test App").getOrCreate()

df = spark.createDataFrame([{"Hello": "World"} for x in range(1000)])
df.show(3)

spark.stop()
