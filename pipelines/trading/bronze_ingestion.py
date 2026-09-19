
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, to_date, col

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("TradingBronzeIngestion")
    .getOrCreate()
)

# Read source CSV
df = (
    spark.read
        .option("header", True)
        .csv("domains/trading/sample-data/trade_execution.csv")
)

# Add audit columns
bronze = (
    df.withColumn("ingestion_time", current_timestamp())
      .withColumn("trade_date", to_date(col("trade_time")))
)

# Save as Delta format
bronze.write \
      .format("delta") \
      .mode("overwrite") \
      .partitionBy("trade_date") \
      .save("output/trading/bronze")

print("Bronze ingestion completed successfully.")
