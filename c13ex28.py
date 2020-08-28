# Créé par Jean Michel et Christophe, le 23/05/2020 en Python 3.4

from matplotlib import pyplot as plt
import numpy as np

v = .../...
alpha = .../...
g = .../...
dt = 0.05
N = 100
H= .../...

t=[]
x=[]
y1=[]
y2=[]
portee = v*v*np.sin(2*alpha*3.14/180)/g
fleche = v*np.sin(alpha*3.14/180)*v*np.sin(alpha*3.14/180)/(2*g)

for i in range (0,N):
    t.append(i*dt)
    x.append(v*np.cos(alpha*3.14/180)*t[i])
    y1.append(-0.5*g*t[i]*t[i]+v*np.sin(alpha*3.14/180)*t[i])
    y2.append(H)

plt.plot(x,y1,'b+')
plt.plot(x, y2,'r-')
plt.xlim(0,1.1*portee)
plt.ylim(0,1.1*fleche)
plt.xlabel("x(m)")
plt.ylabel("y(m)")

plt.show()