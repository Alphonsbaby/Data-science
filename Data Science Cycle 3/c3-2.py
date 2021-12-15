import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array(['mon', 'tue', 'wed', 'thur','fri'])
y = np.array([300, 450, 150, 400,65])


plt.subplot(1, 2, 1)

plt.title("Sales Data1")
plt.xlabel("Days of week")
plt.ylabel("Sale of Drinks")
plt.plot(x,y,':c')
plt.plot(x,y,'Hm',mec = 'k')

plt.grid(color = 'blue',  linestyle = 'dotted')
#plot 2:
c = np.array(['mon', 'tue', 'wed', 'thur','fri'])
v = np.array([400, 500, 350, 300,500])
plt.subplot(1, 2, 2)
plt.title("Sales Data2")
plt.xlabel("Days of Week")
plt.ylabel("Sale of Food")

plt.plot(c,v,'--y')
plt.plot(c,v,'Dg',mec = 'r')

plt.grid(color = 'blue',  linestyle = 'dotted')
plt.show()
