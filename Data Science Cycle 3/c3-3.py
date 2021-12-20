import matplotlib.pyplot as plt
import numpy as np


plt.title("Sales Data")
plt.xlabel("Months of Year")
plt.ylabel("Sale of Food")
x = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
y = np.array([173,153,195,147,120,144,148,109,174,130,172,131])
plt.scatter(x,y, color = 'hotpink')

x = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
y = np.array([185,185,126,134,196,153,112,133,200,145,167,110])
plt.scatter(x, y, color = 'yellow')


x = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
y = np.array([189,189,105,112,173,109,151,197,174,145,177,161])
plt.scatter(x, y, color = 'blue')


plt.show()

