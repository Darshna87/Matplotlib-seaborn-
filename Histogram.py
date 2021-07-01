import numpy as np
import matplotlib.pyplot as plt


Xsn=np.random.randn(100)

MeanMu=60
sigma=5

X = np.round(Xsn * sigma + MeanMu)
X2=np.round(Xsn*7+40)
print(X)
print(X2)

print(plt.style.available)
plt.style.use("ggplot")
plt.hist(X2, alpha=0.5, label="Physics")
plt.hist(X, alpha=0.7, label="Maths")

plt.xlabel("Marks")
plt.ylabel("prob/Fre of students")
plt.title("Student subject result result")
plt.show()

