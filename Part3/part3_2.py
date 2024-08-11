import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    return y.astype(np.int32)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()

def sigmoid(x):
    return 1/(1 + np.exp(-x)) 

y2 = sigmoid(x)

plt.plot(x,y2)
plt.ylim(-0.1, 1.1)
plt.show()