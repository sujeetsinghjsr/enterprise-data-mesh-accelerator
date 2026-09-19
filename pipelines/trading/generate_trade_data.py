
import random
import csv
from datetime import datetime, timedelta

commodities = ["Brent", "WTI", "LNG", "NatGas"]
traders = ["Alice", "Bob", "Charlie", "Diana"]
desks = ["Crude", "Gas"]

start = datetime(2026, 9, 18, 9, 0)

with open("domains/trading/sample-data/trade_execution_large.csv",
          "w",
          newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "trade_id",
        "trade_time",
        "commodity",
        "price",
        "quantity",
        "currency",
        "trader",
        "desk",
        "status"
    ])

    for i in range(100000):

        t = start + timedelta(seconds=i * 5)

        writer.writerow([
            100000 + i,
            t.isoformat(),
            random.choice(commodities),
            round(random.uniform(3, 90), 2),
            random.randint(10, 500),
            "USD",
            random.choice(traders),
            random.choice(desks),
            "NEW"
        ])
