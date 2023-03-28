import numpy as np
import matplotlib.pyplot as plt


"""Paramétrages"""

H=1
c=np.sqrt(9.81*H)
w=1.75
k=w/c

T=(np.exp(k*H)-np.exp(-k*H))/(np.exp(k*H)+np.exp(-k*H))
    
a_1=0.5
a_2=1
a_3=1.5 
ac=1/k
a_4=3

t_1=0
t_2=np.pi/(2*w)

x=np.arange(-10,40,0.5)
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
        Z[j][0].append(T*X[j][0]*B)
        X[j][2].append(i-X[j][0]*C)
        Z[j][1].append(T*X[j][0]*D)
    
plt.subplot(2,1,1)
plt.plot(X[0][1],Z[0][0], 'g', label="a=0.5m")
plt.plot(X[1][1],Z[1][0], 'b', label="a=1m")
plt.plot(X[2][1],Z[2][0], 'c', label="a=1.5m")
plt.plot(X[3][1],Z[3][0], 'r', label="ac=1.79m")
plt.plot(X[4][1],Z[4][0], 'k', label="a=3m")
plt.xlim(-2.5,22.5)
plt.grid()
plt.ylabel("z")
plt.title("Surface libre à l'instant pour H=1m à l'instant t=0")
plt.legend()

plt.subplot(2,1,2)
plt.plot(X[0][2],Z[0][1], 'g', label="a=0.5m")
plt.plot(X[1][2],Z[1][1], 'b', label="a=1m")
plt.plot(X[2][2],Z[2][1], 'c', label="a=1.5m")
plt.plot(X[3][2],Z[3][1], 'r', label="ac=1.79m")
plt.plot(X[4][2],Z[4][1], 'k', label="a=3m")
plt.xlim(-2.5,22.5)
plt.grid()
plt.xlabel("x")
plt.ylabel("z")
plt.title("Surface libre à l'instant pour H=1m à l'instant t=pi/(2w)")
plt.legend()

plt.show()
