#%%
import numpy as np       #Importing numpy libraries
import matplotlib.pyplot as plt  #Importing plotting libraries
from matplotlib.animation import FuncAnimation   # Importing Animation libraries

#%%
M = 300
N=1001
x_i=np.linspace(0,1,M) #Defining an array of x steps from 0 to M. i.e., 0,1,2,3,4,...
y=np.zeros(shape=(M,N)) #Defining an array of size MxN, used below

y[0,0]=y[-1,0]=0 #Boundary condition, walls are fixed
y[:,0]=np.exp(-1000*(x_i-0.3)**2) # Given in equation 6.8

y[0,1]=y[-1,1]=0 #Boundary condition, walls are fixed
for i in range(1,M-1): #loop for calucating y values as function of x at time t=1*del_t
	y[i,1]=y[i+1,0] + y[i-1,0] - y[i,0] #Equation 6.6 for r=1. r=1 is given in book. y(n=1) is one time step ahead of y(n=0).

for n in range(1,1000):
	y[0,n+1]=y[-1,n+1]=0 #Boundary condition, walls are fixed
	for i in range(1,M-1):#loop for calucating y values as function of x at time t=2*del_t
		y[i,n+1]= y[i+1,n] + y[i-1,n] - y[i,n-1] #Equation 6.6 for r=1. y2 is one time step ahead of y1.

#%%
def animate(n): #Defining a function which will animate the waves amplitude (y) as function of t.
	ax.clear() # Clear the previous plot for animation from screen.
	ax.plot(x_i,y[:,n]) #Plotting y3 as a function of x_i. It will show displacement (y) for the string ax a function of x for an instant of time.
	ax.set_ylim(-1.1,1.1) # Set y limits between -1.1 to 1.1
	ax.axis('off') # make the axis invisible (not required)
	ax.set_title('Waves on a string (fixed ends)', fontsize=22) # Writing some relevant text on the plot.

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, figsize=(20, 16))
plt.subplots_adjust(left=0.1, bottom =0.124, right=0.963, top=0.97, wspace=0, hspace=0)
#The above two commands are related to plotting. It is setting the size of figure and spacings in the plot.

ani=FuncAnimation(fig, animate, frames=range(0,1000),interval=100) # Animating the plot 
fig.show() #Showing the plot

# %%















#%%
M = 300
N=3001

c=0.05
Delx = 1/M
# Delt = Delx/c
Delt = 0.02

r=c*Delt/Delx
x_i=np.linspace(0,1,M) #Defining an array of x steps from 0 to M. i.e., 0,1,2,3,4,...
y=np.zeros(shape=(M,N)) #Defining an array of size MxN, used below

y[0,0]=y[-1,0]=0 #Boundary condition, walls are fixed
y[:,0]=np.exp(-1000*(x_i-0.3)**2) # Given in equation 6.8

y[0,1]=y[-1,1]=0 #Boundary condition, walls are fixed
for i in range(1,M-1): #loop for calucating y values as function of x at time t=1*del_t
	y[i,1]= 2*(1-r**2)*y[i,0] + r**2 *(y[i+1,0] + y[i-1,0]) - y[i,0] #Equation 6.6 for r=1. r=1 is given in book. y(n=1) is one time step ahead of y(n=0).

for n in range(1,N-1):
	y[0,n+1]=y[-1,n+1]=0 #Boundary condition, walls are fixed
	for i in range(1,M-1):#loop for calucating y values as function of x at time t=2*del_t
		y[i,n+1]= 2*(1-r**2)*y[i,n] + r**2 *(y[i+1,n] + y[i-1,n]) - y[i,n-1] #Equation 6.6 for r=1. y2 is one time step ahead of y1.

#%%
def animate(n): #Defining a function which will animate the waves amplitude (y) as function of t.
	ax.clear() # Clear the previous plot for animation from screen.
	ax.plot(x_i,y[:,n]) #Plotting y3 as a function of x_i. It will show displacement (y) for the string ax a function of x for an instant of time.
	ax.set_ylim(-1.1,1.1) # Set y limits between -1.1 to 1.1
	ax.set_xlim(0,1)
	ax.text(0.7,1,f't={n*Delt:.2f} s', fontsize=20)
	ax.set_title(f'Waves on a string (fixed ends) with c={c} m/s. Hence r={r}', fontsize=22) # Writing some relevant text on the plot.

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, figsize=(20, 16))
plt.subplots_adjust(left=0.1, bottom =0.124, right=0.963, top=0.97, wspace=0, hspace=0)
#The above two commands are related to plotting. It is setting the size of figure and spacings in the plot.

ani=FuncAnimation(fig, animate, frames=range(0,N,5),interval=100) # Animating the plot 
fig.show() #Showing the plot

# %%
