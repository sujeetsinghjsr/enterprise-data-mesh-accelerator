
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("TradingGoldPublish").getOrCreate()

df = spark.read.format("delta").load("output/trading/silver")

gold = (
    df.groupBy("commodity")
      .agg(
          sum("trade_value").alias("total_trade_value"),
          sum("quantity").alias("total_quantity")
      )
)

gold.write \
    .format("delta") \
    .mode("overwrite") \
    .save("output/trading/gold")
