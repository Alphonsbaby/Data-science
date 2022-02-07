import numpy as np
import matplotlib.pyplot as plt 
 
#a=np.array('cricket','football','hockey','badminten','swimming','tennis')
b=np.array((80,40,20,30,45,75))
plt.title('SPORTS')
plt.xlabel('No of Students')
plt.ylabel('Sports')
plt.bar(b,color='red',width=.2,height=10)
plt.show()

