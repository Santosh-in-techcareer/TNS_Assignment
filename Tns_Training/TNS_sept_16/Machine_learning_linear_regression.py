from sklearn.linear_model import LinearRegression
import numpy as np 

s = np.array([[1],[2],[3],[4],[5]])
m = np.array([[10],[20],[30],[40],[50]])
model = LinearRegression()
san = model.fit(s,m)
while True:
    a = int(input("enter the hours you studied: "))
    c = model.predict([[a]])
    if c >=100:
        print(100)
    else:
        print(c)
