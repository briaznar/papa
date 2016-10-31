
# coding: utf-8

# In[67]:

import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[81]:

cosin = []
sin = []

rand=random.sample(range(1,90),10)
rand.sort()


# In[82]:

for val in rand:
    cosin.append(math.cos(val))
    sin.append(math.sin(val))


# In[83]:

plt.plot(rand, sin,'r-')
plt.plot(rand,cosin,'b-')
plt.ylabel('cosin')
plt.xlabel('sin')
sin_legend = mpatches.Patch(color='red', label='Sin')
cos_legend = mpatches.Patch(color='blue', label='Cosin')
plt.legend(handles=[sin_legend, cos_legend],loc=5)
plt.show()


# In[ ]:




# In[ ]:



