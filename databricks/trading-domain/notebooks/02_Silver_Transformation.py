
# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

spark = SparkSession.builder.appName("TradingSilverNotebook").getOrCreate()

bronze = spark.read.format("delta").load("../../output/trading/bronze")

silver = (
    bronze
      .filter(col("status") != "CANCEL")
      .dropDuplicates(["trade_id"])
      .withColumn("commodity", upper(col("commodity")))
      .withColumn(
          "trade_value",
          col("price").cast("double") *
          col("quantity").cast("int")
      )
)

silver.write \
      .format("delta") \
      .mode("overwrite") \
      .partitionBy("trade_date") \
      .save("../../output/trading/silver")

print("Silver notebook completed.")
