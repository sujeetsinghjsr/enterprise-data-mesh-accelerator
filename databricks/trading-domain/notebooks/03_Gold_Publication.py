
# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count

spark = SparkSession.builder.appName("TradingGoldNotebook").getOrCreate()

silver = spark.read.format("delta").load("../../output/trading/silver")

gold = (
    silver.groupBy("commodity", "trade_date")
          .agg(
              count("*").alias("trade_count"),
              sum("trade_value").alias("total_trade_value"),
              avg("price").alias("average_price")
          )
)

gold.write \
    .format("delta") \
    .mode("overwrite") \
    .partitionBy("trade_date") \
    .save("../../output/trading/gold")

print("Gold notebook completed.")
