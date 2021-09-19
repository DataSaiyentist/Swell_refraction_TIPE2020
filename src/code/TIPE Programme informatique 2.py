import numpy as np
import matplotlib.pyplot as plt

"""Paramétrage"""
L=20
c=np.sqrt((9.81*L)/(2*np.pi))
k=2*np.pi/L
w=k*c

a_1=0.5
a_2=1.183
a_3=2 
ac=3.18
a_4=6

t_1=0
t_2=np.pi/(2*w)

x=np.arange(-10,60,1)
X=[[a_1,[],[]],[a_2,[],[]],[a_3,[],[]],[ac,[],[]],[a_4,[],[]]]
Z=[[[],[]],[[],[]],[[],[]],[[],[]],[[],[]]]

"""Profil de la houle pour diverses amplitudes et aux instants t=0 et t=pi/(2w)"""
for i in x:
    A=np.sin(k*i-w*t_1)
    B=np.cos(k*i-w*t_1)
    C=np.sin(k*i-w*t_2)
    D=np.cos(k*i-w*t_2)
    for j in range(5):
        X[j][1].append(i-X[j][0]*A)
        Z[j][0].append(X[j][0]*B)
        X[j][2].append(i-X[j][0]*C)
        Z[j][1].append(X[j][0]*D)
    
plt.subplot(2,1,1)
plt.plot(X[0][1],Z[0][0], 'g', label="a=0.5m")
plt.plot(X[1][1],Z[1][0], 'b', label="a=1.183m")
plt.plot(X[2][1],Z[2][0], 'c', label="a=2m")
plt.plot(X[3][1],Z[3][0], 'r', label="ac=3.18m")
plt.plot(X[4][1],Z[4][0], 'k', label="a=6m")
plt.xlim(-5,40)
plt.grid()
plt.ylabel("z")
plt.title("Surface libre à l'instant pour H infini à l'instant t=0")
plt.legend()

plt.subplot(2,1,2)
plt.plot(X[0][2],Z[0][1], 'g', label="a=0.5m")
plt.plot(X[1][2],Z[1][1], 'b', label="a=1.183m")
plt.plot(X[2][2],Z[2][1], 'c', label="a=2m")
plt.plot(X[3][2],Z[3][1], 'r', label="ac=3.18m")
plt.plot(X[4][2],Z[4][1], 'k', label="a=6m")
plt.xlim(-5,40)
plt.grid()
plt.xlabel("x")
plt.ylabel("z")
plt.title("Surface libre à l'instant pour H infini à l'instant t=pi/(2w)")
plt.legend()

plt.show()












