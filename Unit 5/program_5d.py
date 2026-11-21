"""Program 5D: Retail sales dashboard using CSV and Matplotlib."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

sales_path = Path(__file__).with_name("sales.csv")
daily = {}
product_totals = {}

try:
    with sales_path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            amount = int(row["Sales"])
            daily[row["Date"]] = daily.get(row["Date"], 0) + amount
            product_totals[row["Product"]] = (
                product_totals.get(row["Product"], 0) + amount
            )

    if not daily:
        raise ValueError("Sales data is empty")

    print("RETAIL SALES REPORT")
    for day in sorted(daily):
        print(f"{day}: {daily[day]}")

    print("PRODUCT TOTALS")
    for name in sorted(product_totals):
        print(f"{name}: {product_totals[name]}")

    daily_chart = Path(__file__).with_name("daily_sales.png")
    product_chart = Path(__file__).with_name("product_sales.png")

    plt.figure(figsize=(7, 3.5))
    plt.plot(
        sorted(daily),
        [daily[day] for day in sorted(daily)],
        marker="o",
    )
    plt.title("Daily Retail Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(daily_chart, dpi=160)
    plt.close()

    plt.figure(figsize=(7, 3.5))
    plt.bar(list(product_totals), list(product_totals.values()))
    plt.title("Product Wise Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(product_chart, dpi=160)
    plt.close()

    print("Charts saved: daily_sales.png, product_sales.png")
except (OSError, ValueError, KeyError) as error:
    print("Sales dashboard error:", error)
