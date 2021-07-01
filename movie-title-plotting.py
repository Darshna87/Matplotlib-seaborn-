import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("./movie_metadata.csv")
print(df.shape)
print(df.head(n=5))
print(df.columns)

titles=list(df.get('movie_title'))
print(titles)

freq_title={}

for title in titles:
    length=len(title)

    if freq_title.get(length) is None:
        freq_title[length]=1
    else:
        freq_title[length] += 1

print(freq_title)

X=np.array(list(freq_title.keys()))
Y=np.array(list(freq_title.values()))

plt.scatter(X,Y)
plt.xlabel("Movie title length")
plt.ylabel("movie frequency")
plt.show()