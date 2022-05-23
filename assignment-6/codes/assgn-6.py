import matplotlib.pyplot as plt
import numpy as np

# Define X and Y variable data
x = np.array([0.25,0.5,0.75,1,1.25,1.5,1.75,2])
y = np.array([0.25,0.5,0.75,1,1,1,1,1])

plt.plot(x, y)
plt.xlabel("random variable")  # add X-axis label
plt.ylabel("F(x)")  # add Y-axis label
plt.show()