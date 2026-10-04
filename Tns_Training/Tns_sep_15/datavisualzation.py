import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

san = np.array([[81,92,73,74,85],[56,65,45,76,88],[45,67,89,90,78]])
seen = pd.DataFrame(san,columns=["santosh","raj","hema","kaviya","sathveeka"],index=["maths","science","social"])
average = np.mean(san,axis = 0)
print(seen)
sana= []
print(average)
for i in range(len(average)):
    if average[i] >65:
        sana.append(average[i])
print(sana)
print(seen["santosh"])
print(seen.loc[seen["kaviya"]==seen["kaviya"].max(),"kaviya"])
print(seen.max(axis=1))
seen.plot(kind='bar',figsize=(10,5))
plt.xlabel('subject')
plt.ylabel('students')
plt.title('Students Report')
plt.show()

#heat map which finds a relationship between 2 variable 
#pair plot isused to find the relationship between multiple variable
