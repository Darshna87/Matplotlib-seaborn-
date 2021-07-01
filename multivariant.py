# Example on Multivariant normal Distribution using scatter plot

import numpy as np
import matplotlib.pyplot as plt

mean=np.array([0.0,0.0])
cov=np.array([[5,2],[2,5]])

mean2=np.array([5.0,5.0])
cov2=np.array([[7,4],[4,7]])


dist=np.random.multivariate_normal(mean,cov,500)
dist2=np.random.multivariate_normal(mean2,cov2,500)
#print(dist.shape)

plt.scatter(dist[:,[0]],dist[:,[1]])
plt.scatter(dist2[:,[0]],dist2[:,[1]])
plt.show()