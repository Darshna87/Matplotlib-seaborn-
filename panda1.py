import pandas as pd
import numpy as np


marks_dict={
    'marksA' : np.random.randint(1,100,5),
    'marksB' : np.random.randint(30,100,5),
    'marksC' : np.random.randint(20,100,5)
}

print(marks_dict)

df=pd.DataFrame(marks_dict)
print(df)

print(df.head(n=3))
print(df.columns)

df.to_csv("marks.csv")
my_data = pd.read_csv("marks.csv")
print(my_data)

my_data = my_data.drop(columns=['Unnamed: 0'])
print(my_data)

