import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([2001, 2002,2003,2004,2005,2006,2007])
ypoints = np.array([24000, 22500,19700,17500,14500,10000,5800])
plt.plot(xpoints, ypoints, '*g',ms = 20)
plt.plot(xpoints, ypoints, ':r')

leg = plt.legend(title="Value Depreciation ")
leg._legend_box.align = "left"

plt.show()
