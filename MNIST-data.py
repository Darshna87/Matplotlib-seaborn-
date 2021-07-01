import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(".\mnist_train_small.csv")
print(df.shape)

data=df.values
np.random.shuffle(data)

x=data[:,1:]
y=data[:,0]
print(x,y)
print(x.shape,y.shape)

#split the data in training and testing
split=int(0.80*x.shape[0])
print(split)

X_train,Y_train=x[:split,:],y[:split]
X_test,Y_test=x[split:,:],y[split:]

print(np.shape(X_train),np.shape(Y_train))
print(np.shape(X_test),np.shape(Y_test))

#ploting visualisation of first 25 images
plt.figure(figsize=(12,12))

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(X_train[i].reshape(28,28),cmap='gray')
    plt.title(Y_train[i])
    plt.axis("off")
plt.show()
