import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4])
print("Numpy array:", arr)

students = {"name": ["Ajay", "Ravi"], "marks": [90, 85]}
df = pd.DataFrame(students)
print(df)
print("Average marks:", df["marks"].mean())
