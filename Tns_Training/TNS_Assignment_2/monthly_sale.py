import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]
sales = [25000, 30000, 28000, 35000, 40000, 45000]

plt.plot(months, sales, marker="o", label="Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

plt.bar(months, sales, label="Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()