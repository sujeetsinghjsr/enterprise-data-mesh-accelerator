
from pyspark.sql.functions import col

def validate_trades(df):
    """
    Validates incoming trade records.

    Returns:
        valid_records
        rejected_records
    """

    valid = (
        df.filter(col("trade_id").isNotNull())
          .filter(col("price").cast("double") > 0)
          .filter(col("quantity").cast("int") > 0)
          .dropDuplicates(["trade_id"])
    )

    rejected = df.subtract(valid)

    return valid, rejected
