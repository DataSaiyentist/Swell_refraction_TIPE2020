import numpy as np
import matplotlib.pyplot as plt

axes=plt.gca()

# Question 9
# v0=a*w
# z=0
# U_1=[]
# W_1=[]
# for i in x: 
#     U_1.append(v0*(np.exp(k*z))*np.cos(k*i-w*t_1))
#     W_1.append(v0*(np.exp(k*z))*np.sin(k*i-w*t_1))
# 
# plt.plot(U_1,W_1)
# plt.grid()
# plt.axhline()
# plt.xlabel("x")
# plt.axvline()
# plt.ylabel("z")
# plt.title("champ de vitesse")
# plt.show()

# Question 13

"""Paramétrages"""
L=20
c=np.sqrt((9.81*L)/(2*np.pi))  #A démontrer
k=2*np.pi/L
w=k*c

a_1=0.5
a_2=1.183
a_3=2 
ac=3.18
a_4=6

# t_1=0
# t_2=np.pi/(2*w)
# 
# x=np.arange(-10,40,1)
# X=[[a_1,[],[]],[a_2,[],[]],[a_3,[],[]],[ac,[],[]],[a_4,[],[]]]
# Z=[[[],[]],[[],[]],[[],[]],[[],[]],[[],[]]]
# 
# """Profil de la houle pour diverses amplitudes et aux instants t=0 et t=pi/(2w)"""
# for i in x:
#     A=np.sin(k*i-w*t_1)
#     B=np.cos(k*i-w*t_1)
#     C=np.sin(k*i-w*t_2)
#     D=np.cos(k*i-w*t_2)
#     for j in range(5):
#         X[j][1].append(i-X[j][0]*A)
#         Z[j][0].append(X[j][0]*B)
#         X[j][2].append(i-X[j][0]*C)
#         Z[j][1].append(X[j][0]*D)
#     
# plt.subplot(2,1,1)
# plt.plot(X[0][1],Z[0][0], 'g', label="a=0.5")
# plt.plot(X[1][1],Z[1][0], 'b', label="a=1.183")
# plt.plot(X[2][1],Z[2][0], 'c', label="a=2")
# plt.plot(X[3][1],Z[3][0], 'r', label="ac=3.18")
# plt.plot(X[4][1],Z[4][0], 'k', label="a=6")
# plt.xlim(-5,30)
# plt.grid()
# plt.xlabel("x")
# plt.ylabel("z")
# plt.title("Surface libre à l'instant pour H infini à l'instant t=0")
# plt.legend()
# 
# plt.subplot(2,1,2)
# plt.plot(X[0][2],Z[0][1], 'g', label="a=0.5")
# plt.plot(X[1][2],Z[1][1], 'b', label="a=1.183")
# plt.plot(X[2][2],Z[2][1], 'c', label="a=2")
# plt.plot(X[3][2],Z[3][1], 'r', label="ac=3.18")
# plt.plot(X[4][2],Z[4][1], 'k', label="a=6")
# plt.xlim(-5,30)
# plt.grid()
# plt.xlabel("x")
# plt.ylabel("z")
# plt.title("Surface libre à l'instant pour H infini à l'instant t=pi/(2w)")
# plt.legend()
# 
# plt.show()

"""AN"""
# np.exp(2*np.pi)
# Out[3]: 535.49165552476461
# 
# 5+0.5*np.exp(np.pi/2)
# Out[7]: 7.4052386904826761
# 
# np.sqrt(2*L*np.pi/9.81)
# Out[8]: 3.5790719436664071
# 
# c
# Out[9]: 5.5880407867722184

# Question 23

def ch(x):
    return (np.exp(x)+np.exp(-x))/2
    
def sh(x):
    return (np.exp(x)-np.exp(-x))/2
    
def th(x):
    return sh(x)/ch(x)
    
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


for i in x_3:
    E=k*H
    F=k*i
    for j in range(5):
        U[j][1].append(np.cos(F)*ch(k*U[j][0]+E))
        W[j].append(np.sin(F)*sh(k*U[j][0]+E)+U[j][0])
    
plt.plot(U[0][1],W[0], label="z=0")
plt.plot(U[1][1],W[1], label="z=-0.5")
plt.plot(U[2][1],W[2], label="z=-0.75")
plt.plot(U[3][1],W[3], label="z=-0.825")
plt.plot(U[4][1],W[4], label="z=-1")

plt.xlabel("u")
plt.ylabel("w")
plt.title("Ellipse à t=0, H fini")
plt.legend()
plt.show()
