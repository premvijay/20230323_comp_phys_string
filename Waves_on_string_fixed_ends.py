#! /usr/bin/env python
#%%
import numpy as np       #Importing numpy libraries
import matplotlib.pyplot as plt  #Importing plotting libraries
from matplotlib.animation import FuncAnimation   # Importing Animation libraries

#%%
M = 300
x_i=np.linspace(0,1,M) #Defining an array of x steps from 0 to 99. i.e., 0,1,2,3,4,...
y0=np.zeros(M) #Defining an array of size M, used below
y1=np.zeros(M) #Defining an array of size M, used below
y2=np.zeros(M) #Defining an array of size M, used below
y3=np.zeros(M) #Defining an array of size M, used below

y0[0]=y0[-1]=0 #Boundary condition, walls are fixed
for i in range(M): #loop for calucating y values as function of x at time t=0
	y0[i]=np.exp(-1000*(x_i[i]-0.3)**2) # Given in equation 6.8

y1[0]=y1[-1]=0 #Boundary condition, walls are fixed
for i in range(1,M-1): #loop for calucating y values as function of x at time t=1*del_t
	y1[i]=y0[i+1] + y0[i-1] - y0[i] #Equation 6.6 for r=1. r=1 is given in book. y1 is one time step ahead of y0.


def animate(j): #Defining a function which will animate the waves amplitude (y) as function of t.
	y2[0]=y2[99]=0 #Boundary condition, walls are fixed
	for i in range(1,M-1):#loop for calucating y values as function of x at time t=2*del_t
		y2[i]= y1[i+1] + y1[i-1] - y0[i] #Equation 6.6 for r=1. y2 is one time step ahead of y1.
	y3[0]=y3[99]=0 #Boundary condition, walls are fixed
	for i in range(1,M-1): #loop for calucating y values as function of x at time t=3*del_t
		y3[i]= y2[i+1] +y2[i-1]  - y1[i] #Equation 6.6 for r=1. y3 is one time step ahead of y2.
	for i in range(M): # this will put the values of y0,y1,y2,y3 in a loop so that you can predict the y as a function of t knowing the initial values, boundary conditions, and equation of motion.
		y0[i]=y1[i] # replacing y0 by y1
		y1[i]=y2[i] # replacing y1 by y2
		y2[i]=y3[i] # replacing y2 by y3
	ax.clear() # Clear the previous plot for animation from screen.
	ax.plot(x_i,y3) #Plotting y3 as a function of x_i. It will show displacement (y) for the string ax a function of x for an instant of time.
	ax.set_ylim(-1.1,1.1) # Set y limits between -1.1 to 1.1
	ax.axis('off') # make the axis invisible (not required)
	# plt.text(50,0.9, 'Waves on a string (fixed ends)', fontsize=22) # Writing some relevant text on the plot.
	ax.set_title('Waves on a string (fixed ends)', fontsize=22) # Writing some relevant text on the plot.

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, figsize=(20, 16))
plt.subplots_adjust(left=0.1, bottom =0.124, right=0.963, top=0.97, wspace=0, hspace=0)
#The above two commands are related to plotting. It is setting the size of figure and spacings in the plot.

ani=FuncAnimation(fig, animate, interval=100) # Animating the plot 

fig.show() #Showing the plot

# %%
