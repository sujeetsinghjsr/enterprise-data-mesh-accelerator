
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.appName("TradingBronzeIngestion").getOrCreate()

df = (
    spark.read
        .option("header", True)
        .csv("domains/trading/sample-data/trade_execution.csv")
)

bronze = (
    df.withColumn("ingestion_time", current_timestamp())
)

bronze.write \
    .format("delta") \
    .mode("overwrite") \
    .save("output/trading/bronze")
