#!/usr/bin/env python
# coding: utf-8

# In[157]:


import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

plt.style.use('seaborn')


# In[158]:


tab1 = pd.read_csv('table1.csv')


# In[159]:


cp = tab1.concreq.values

c = tab1.stockconc.values

x = tab1.volume.values

xp = x*(c-cp)/cp

tab1['xp'] = xp

tab1 = tab1.astype('int')


# In[160]:


tab2 =  pd.read_csv('tab2.csv')

tab2 = tab2.astype('float64')


# In[161]:


tab2['total'] = tab2.csr + tab2.vsr / 60
x = tab2.total
mean = [np.mean([x[i-1],x[i]]) for i in range(len(x)) if i % 2 == 1]
print(*mean,sep = '\n')


# In[162]:


tab2


# In[178]:


ro = 65 + 15/60
ro = np.array([ro for _ in range(7)])


# In[179]:


angle = mean-ro


# In[188]:


print(*["{0:.2f}".format(x) for x in angle],sep = '\n')


# In[195]:


c = np.array([16,14,12,10,8,6])

l = np.array([20 for x in c])
angle = angle[0:-1]
s = 1000*(angle)/(l*c)
s = list(s)
s = s[0:-1]
print(*s,sep = '\n')


# In[215]:


slope, inter =  np.polyfit(angle,c,1)
plt.plot(angle, slope*angle + inter, 'g--',label = "Best-Fit")
plt.plot(angle,c,':or',alpha = 0.5,label= 'Original')
plt.title('Concentration // Theta')
plt.xlabel('angle')
plt.ylabel('concentration')
plt.legend()

plt.savefig('graph',dpi = 300)
plt.show()

# In[176]:


theta = - ro[0] + 70.5
theta


# In[177]:


1000 * theta/(np.mean(s)*20)


# In[ ]:




