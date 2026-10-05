import pandas as pd

data = {
    "Product Name": ["Laptop", "Mobile", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 20000, 1500, 800, 12000],
    "Quantity Sold": [20, 60, 80, 100, 30]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Sales:")
print(df)

print("\nProduct with highest sales:")
print(df.loc[df["Total Sales"].idxmax()])

print("\nAverage Product Price:")
print(df["Price"].mean())

print("\nProducts with quantity sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

print("\nProducts sorted by total sales:")
print(df.sort_values("Total Sales"))