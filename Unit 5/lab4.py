
import csv
import matplotlib.pyplot as plt

dates = {}
products = {}

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        date = row["Date"]
        product = row["Product"]
        sales = int(row["Sales"])

        dates[date] = dates.get(date, 0) + sales
        products[product] = products.get(product, 0) + sales

# Line Graph
plt.plot(list(dates.keys()), list(dates.values()),
         marker="o")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart
plt.bar(list(products.keys()), list(products.values()))
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
