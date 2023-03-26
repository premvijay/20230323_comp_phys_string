#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
# Probability to move up or down
prob = 0.5
 
# statically defining the starting position
start = 0
siz = 10
samp = 100
pos = np.zeros((samp,siz))
 
# creating the random points
# rr = np.random.random((samp,siz))

# do shift at each step based on random points
# shift = (rr > prob).astype('int')*2-1

# shift = np.random.getrandbits((samp,siz))*2-1
shift = np.random.choice([-1,1], size=(samp,siz))

pos = np.cumsum(shift,axis=1)

 
# plotting down the graph of the random walk in 1D
plt.plot(pos[0])
plt.show()

## %%
pos = np.array(pos)
# plt.plot(np.cumsum(pos)/np.arange(100001))
# plt.plot(np.cumsum(pos[0]**2)**(1/2)/np.arange(100001))
plt.plot(np.mean(pos**2,axis=0))
# %%
