
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    upper
)

from utils.data_quality import validate_trades

spark = (
    SparkSession.builder
    .appName("TradingSilverTransformation")
    .getOrCreate()
)

# Read Bronze data
bronze_df = (
    spark.read
         .format("delta")
         .load("output/trading/bronze")
)

# Apply reusable validation
valid_df, rejected_df = validate_trades(bronze_df)

# Business transformations
silver_df = (
    valid_df
      .filter(col("status") != "CANCEL")
      .withColumn("commodity", upper(col("commodity")))
      .withColumn(
          "trade_value",
          col("price").cast("double") *
          col("quantity").cast("int")
      )
)

# Save Silver
silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .partitionBy("trade_date") \
    .save("output/trading/silver")

print("Silver transformation completed successfully.")
