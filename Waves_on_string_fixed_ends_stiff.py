#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation   # Importing Animation libraries

#%%


#%%

fig_ps, ax_ps = plt.subplots(1)

for eps in [0,1e-5,2e-5]:
    M = 300
    N=10001

    c=0.03
    Delx = 1/M
    # Delt = Delx/c
    Delt = 0.02

    # eps = 2e-5 # stiffness
    # eps=0
    L=1
    Ml = L/Delx

    r=c*Delt/Delx
    x_i=np.linspace(0,1,M) #Defining an array of x steps from 0 to M. i.e., 0,1,2,3,4,...
    y=np.zeros(shape=(M,N)) #Defining an array of size MxN, used below

    y[0,0]=y[-1,0]=0 #Boundary condition, walls are fixed
    y[:,0]=np.exp(-1000*(x_i-0.45)**2) # Given in equation 6.8

    y[0,1]=y[-1,1]=0 #Boundary condition, walls are fixed
    for i in range(1,M-1): #loop for calucating y values as function of x at time t=1*del_t
        if i==1:
            stiff_term = y[i+2,0]-y[i,0]
        elif i==M-2:
            stiff_term = -y[i,0]+y[i-2,0]
        else:
            stiff_term = y[i+2,0]+y[i-2,0]
        
        y[i,1]= 2*(1-r**2-3*eps*r**2*M**2)*y[i,0] + r**2 *(1+4*eps*M**2)*(y[i+1,0] + y[i-1,0]) - y[i,0] - eps*r**2*M**2 *stiff_term #Equation 6.11 given in book. y(n=1) is one time step ahead of y(n=0).

    for n in range(1,N-1):
        y[0,n+1]=y[-1,n+1]=0 #Boundary condition, walls are fixed

        for i in range(1,M-1):#loop for calucating y values as function of x at time t=2*del_t
            if i==1:
                stiff_term = y[i+2,n]-y[i,n]
            elif i==M-2:
                stiff_term = -y[i,n]+y[i-2,n]
            else:
                stiff_term = y[i+2,n]+y[i-2,n]

            y[i,n+1]= 2*(1-r**2-3*eps*r**2*M**2)*y[i,n] + r**2 *(1+4*eps*M**2)*(y[i+1,n] + y[i-1,n]) - y[i,n-1] - eps*r**2*M**2 *stiff_term #Equation 6.11 given in book. y(n=1) is one time step ahead of y(n=0).


    # def animate(n): #Defining a function which will animate the waves amplitude (y) as function of t.
    #     ax.clear() # Clear the previous plot for animation from screen.
    #     ax.plot(x_i,y[:,n]) #Plotting y3 as a function of x_i. It will show displacement (y) for the string ax a function of x for an instant of time.
    #     ax.set_ylim(-1.1,1.1) # Set y limits between -1.1 to 1.1
    #     ax.set_xlabel('m')
    #     ax.text(0.7,1,f't={n*Delt:.2f} s', fontsize=20)
    #     ax.text(0.7,-1,f'Here r={r:.2f}', fontsize=20)
    #     ax.set_title(f"Waves on a 'stiff' string (fixed ends) with c={c} m/s and $\\epsilon$={eps}", fontsize=22) # Writing some relevant text on the plot.

    # fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True, figsize=(20, 16))
    # plt.subplots_adjust(left=0.1, bottom =0.124, right=0.963, top=0.97, wspace=0, hspace=0)
    # #The above two commands are related to plotting. It is setting the size of figure and spacings in the plot.

    # ani=FuncAnimation(fig, animate, frames=range(0,N,5),interval=100) # Animating the plot 
    # fig.show() #Showing the plot







    data = y[15,:]

    ps = np.abs(np.fft.fft(data))**2

    time_step = 1 / 30
    freqs = np.fft.fftfreq(data.size, time_step)
    idx = np.argsort(freqs)

    ax_ps.plot(freqs[idx], ps[idx])


# %%
from scipy import signal
f, Pxx_spec = signal.welch(data, 1e3, 'flattop', 1024, scaling='spectrum')
plt.figure()
plt.semilogy(f, np.sqrt(Pxx_spec))
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')
plt.title('Power spectrum')
plt.show()
# %%
