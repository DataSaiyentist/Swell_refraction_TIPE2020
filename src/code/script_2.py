import numpy as np
import matplotlib.pyplot as plt


"""Paramétrage"""

a=0.5
L=20
c=np.sqrt((9.81*L)/(2*np.pi))
k=2*np.pi/L
w=k*c

t_1=0
v0=a*w
x=np.arange(-50,50,1)

z0=0
z1=-2
z2=-5

U=[[z0,[]],[z1,[]],[z2,[]]]
W=[[],[],[]]


"""Déplacement des particules en eau profonde"""

for i in x:
    A=k*i
    for j in range(3):
        U[j][1].append(v0*(np.exp(k*U[j][0]))*np.cos(A))
        W[j].append(v0*(np.exp(k*U[j][0]))*np.sin(A)+U[j][0])


plt.plot(U[0][1],W[0], label="z=0m")
plt.plot(U[1][1],W[1], 'c', label="z=-2m")
plt.plot(U[2][1],W[2], label="z=-5m")
plt.xlim(-3.5,3.5)
plt.title("Déplacement des particules en eau profonde")
plt.legend()
plt.show()