#%%
import numpy as np
import matplotlib.pyplot as plt


#%%
x =0



#%%
randoms = np.random.choice([-1,1], 10000)

#%%

x=0

for i in range(10000):
    x = x+randoms[i]



#%%



#%%
x = np.zeros(400)
y = np.zeros(400)


for i in range(10000):
    random_walk_x = np.random.choice([-1,1], 400)
    random_walk_y = np.random.choice([-1,1], 400)

    x = x+ random_walk_x
    y = y+ random_walk_y

plt.scatter(x,y)

#%%

x = np.zeros(400)
y = np.zeros(400)

# randoms_x = np.random.choice([-1,1], (400,10000))
# randoms_y = np.random.choice([-1,1], (400,10000))

for i in range(100000):
    x = x+ np.random.choice([-1,1], 400)
    y = y+ np.random.choice([-1,1], 400)

plt.scatter(x,y)


#%%
x = np.zeros(400)
y = np.zeros(400)

# randoms_x = np.random.choice([-1,1], (400,10000))
# randoms_y = np.random.choice([-1,1], (400,10000))

for i in range(1000000):
    x = x+ np.random.choice([-1,1], 400)
    y = y+ np.random.choice([-1,1], 400)

plt.scatter(x,y)




#%%

x = np.zeros(400)
y = np.zeros(400)

for i in range(20):
    for j in range(20):
        x[i*20+j] = i
        y[i*20+j] = j

plt.scatter(x,y)
plt.xlim(-200,200)
plt.ylim(-200,200)

#%%
for i in range(10000):
    random_walk_x = np.random.choice([-0.01,0.01], 400)
    random_walk_y = np.random.choice([-0.01,0.01], 400)

    x = x+ random_walk_x
    y = y+ random_walk_y

plt.scatter(x,y)
plt.xlim(-200,200)
plt.ylim(-200,200)



















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
