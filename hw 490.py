#!/usr/bin/env python
# coding: utf-8

# In[6]:


nums=range(1,6)
print(list(nums))
print(list(map(str,nums)))


# In[8]:


nums=range(0,7)
print(list(nums))
print(list(map(str,nums)))


# In[15]:


for x in range(7):
    print(x,end='')


# In[17]:


for x in range(7):
    print(x)


# In[32]:


for x in range(1):
    for y in[6,5,4,3,2,1,0]:
        b=x+y
        print(b)
    


# In[69]:


import math
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

x= np.linspace[-20,20,0.1]:
    plt.plot(x,x**2,label='y')
        plt.legend()
        plt.show()
         


# In[51]:


import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

x=numpy.arange(0,20,0.1):
    y=x.^2:
        plt.plot(x,y)
        plt.show
    


# In[ ]:




