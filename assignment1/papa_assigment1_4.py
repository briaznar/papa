
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#Creating an array for sine and cosine
COSIN = list()
SIN = list()

#Creates 10 random numebrs between 1 and 90 and then order them
rand=random.sample(range(1,90),10)
rand.sort()


#Stores the result from sin and cosin values in their correspondant arrays
for val in rand:
    COSIN.append(math.cos(val))
    SIN.append(math.sin(val))

#Plot the sin and cosine values against the random values generated
plt.plot(rand, SIN,'r-')
plt.plot(rand,COSIN,'b-')
plt.ylabel('cosin')
plt.xlabel('sin')
sin_legend = mpatches.Patch(color='red', label='Sin')
cos_legend = mpatches.Patch(color='blue', label='Cosin')
plt.legend(handles=[sin_legend, cos_legend],loc=5)
plt.show()





