import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

x = [0, 1]
w = [-1, -1]
t = 0

print("x w t O")
for i in range(len(x)):
    if (x[i] * w[i]) >= t:
        print(x[i], ' ', w[i], ' ', t, ' ', 1)
    else:
        print(x[i], ' ', w[i], ' ', t, ' ', 0)

# Graph Code
df = pd.DataFrame({'x1': [0, 0, 1, 1], 'x2': [0, 1, 0, 1]})
plt.scatter(df.x1, df.x2)
abline(-1, 0)
plt.show()
