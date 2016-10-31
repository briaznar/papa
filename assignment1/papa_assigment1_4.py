
# coding: utf-8

# In[9]:

import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# In[10]:

cosin = list()
sin = list()

rand=random.sample(range(1,90),10)
rand.sort()


# In[11]:

for val in rand:
    cosin.append(math.cos(val))
    sin.append(math.sin(val))


# In[12]:

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



