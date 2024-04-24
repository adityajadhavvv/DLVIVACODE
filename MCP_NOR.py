import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

# NOR Gate
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
w1 = [-1, -1, -1, -1]
w2 = [-1, -1, -1, -1]
t = -1

# Print header for the output table
print("x1 x2 w1 w2 t O")
for i in range(len(x1)):
    if (x1[i] * w1[i] + x2[i] * w2[i]) > t:
        output = 0
    else:
        output = 1
    print(x1[i], ' ', x2[i], ' ', w1[i], ' ', w2[i], ' ', t, ' ', output)

# Graph Code
df = pd.DataFrame({'x1': [0, 0, 1, 1], 'x2': [0, 1, 0, 1]})
plt.scatter(df.x1, df.x2)
abline(1, 1)
plt.show()
