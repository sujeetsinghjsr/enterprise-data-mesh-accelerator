
# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, to_date, col

spark = SparkSession.builder.appName("TradingBronzeNotebook").getOrCreate()

print("Reading raw trade data...")

df = (
    spark.read
         .option("header", True)
         .csv("../../domains/trading/sample-data/trade_execution.csv")
)

bronze_df = (
    df.withColumn("ingestion_time", current_timestamp())
      .withColumn("trade_date", to_date(col("trade_time")))
)

bronze_df.write \
    .format("delta") \
    .mode("overwrite") \
    .partitionBy("trade_date") \
    .save("../../output/trading/bronze")

print("Bronze notebook completed.")
