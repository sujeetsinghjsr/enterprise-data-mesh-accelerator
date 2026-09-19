
import pandas as pd

def test_trade_value():

    df = pd.DataFrame({

        "price": [10, 20],
        "quantity": [5, 2]

    })

    df["trade_value"] = df["price"] * df["quantity"]

    assert df["trade_value"].iloc[0] == 50
    assert df["trade_value"].iloc[1] == 40
