import numpy as np
import matplotlib.pyplot as plt

"""Paramétrage"""    
x_3=np.arange(-15,15,1)
z0=0
z1=-0.25
z2=-0.5
z3=-0.825
z4=-0.975

H=1
k=0.56

U=[[z0,[]],[z1,[]],[z2,[]],[z3,[]],[z4,[]]]
W=[[],[],[],[],[]]

"""Déplacement des particules en eau peu profonde"""
def ch(x):
    return (np.exp(x)+np.exp(-x))/2
    
def sh(x):
    return (np.exp(x)-np.exp(-x))/2
    
def th(x):
    return sh(x)/ch(x)
    
for i in x_3:
    E=k*H
    F=k*i
    for j in range(5):
        U[j][1].append(np.cos(F)*ch(k*U[j][0]+E))
        W[j].append(np.sin(F)*sh(k*U[j][0]+E)+U[j][0])
    
plt.plot(U[0][1],W[0], label="z=0m")
plt.plot(U[1][1],W[1], label="z=-0.5m")
plt.plot(U[2][1],W[2], label="z=-0.75m")
plt.plot(U[3][1],W[3], label="z=-0.825m")
plt.plot(U[4][1],W[4], label="z=-1m")

plt.title("Déplacement des particules en eau peu profonde à t=0s, H=1m")
plt.legend()
plt.show()




