import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import math
import matplotlib.animation as animation

#defining the function for 常微分方程
def mode1(theta,t,g,l):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2 
    dtheta2_dt = - (g/l)*math.sin(theta1)
    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    return dtheta_dt

g=9.8 
l=1 
theta_0 = [0,3] #theta初值
t = np.linspace(0,10,150)


#solving 常微分方程
theta = odeint(mode1,theta_0,t,args = (g,l))


fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(1, 1, 1,facecolor='black')
plt.rcParams['font.size'] = 15

ims = [] #将每一帧都存进去
for i in range(len(theta)):
    ln, = ax.plot([0, np.sin(theta[i, 0])], [0, -np.cos(theta[i, 0])], color='white', lw=2)

    bob, = ax.plot(np.sin(theta[i, 0]), -np.cos(theta[i, 0]),'o',markersize=20,color='yellow')

    tm = ax.text(-0.9, 0.25, 'Time = %.1fs' % t[i])

    ims.append([ln, bob, tm])

ax.set_aspect('equal', 'datalim')
#ax.set_aspect('equal')

ani = animation.ArtistAnimation(fig, ims, interval=50) #生成动画

#保存成gif
ani.save("pendulum.gif", writer='pillow')
