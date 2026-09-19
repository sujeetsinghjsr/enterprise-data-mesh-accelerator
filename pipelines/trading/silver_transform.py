
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

spark = SparkSession.builder.appName("TradingSilverTransform").getOrCreate()

df = spark.read.format("delta").load("output/trading/bronze")

silver = (
    df
    .dropDuplicates(["trade_id"])
    .filter(col("status") != "CANCEL")
    .withColumn("commodity", upper(col("commodity")))
    .withColumn("trade_value",
                col("price").cast("double") *
                col("quantity").cast("int"))
)

silver.write \
      .format("delta") \
      .mode("overwrite") \
      .save("output/trading/silver")
