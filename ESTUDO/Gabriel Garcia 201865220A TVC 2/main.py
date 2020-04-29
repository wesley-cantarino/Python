# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:10:56 2019

@author: gabriel.garcia
"""

import numpy as np
import matplotlib.pyplot as plt
from lib import equation
from scipy.optimize import fsolve
import math

plt.close('all')

M = np.loadtxt(open("Trajeto8.csv","r"),delimiter=",",skiprows=1,usecols=(3,2))
M[:,0]=M[:,0]*1000

rmin = 8 #Local. ac. pedestres (69 kV)
R = np.array([[299,6.8],[745,12.3],[1149,8.3]])


y_min = M[:,1] + rmin

numlinhasR = np.shape(R)[0]

for i in range(0,numlinhasR):
    indice = np.where(M[:,0]>=R[i,0])[0][0]
    y_min[indice-2:indice+2] = M[indice-2:indice+2,1]+R[i,1]

plt.figure(1) #Repres. relevo, torres e catenária
plt.xlabel("x [m]")
plt.ylabel("y [m]")

plt.plot(M[:,0],M[:,1],'b',M[:,0],y_min,'r')

xt1 = 0   #valor aproximado de xt1
xt2 = 1000 #valor aproximado de xt2
xt3 = 1500 #valor aproximado de xt2
xt4 = 2000 #valor aproximado de xt2
H = 17

i_t1 = np.where(M[:,0]>=xt1)[0][0]
i_t2 = np.where(M[:,0]>=xt2)[0][0]
i_t3 = np.where(M[:,0]>=xt3)[0][0]
i_t4 = np.where(M[:,0]>=xt4)[0][0]

xt1 = M[i_t1,0] #xt1 corrigido
xt2 = M[i_t2,0] #xt2 corrigido
xt3 = M[i_t3,0] #xt2 corrigido
xt4 = M[i_t4,0] #xt2 corrigido

yt1 = M[i_t1,1] + H #coordenada do ponto mais alto da T1
yt2 = M[i_t2,1] + H #coordenada do ponto mais alto da T2
yt3 = M[i_t3,1] + H #coordenada do ponto mais alto da T2
yt4 = M[i_t4,1] + H #coordenada do ponto mais alto da T2

#Representação das torres
T1 = np.array([[xt1,M[i_t1,1]],[xt1,yt1]])
T2 = np.array([[xt2,M[i_t2,1]],[xt2,yt2]])
T3 = np.array([[xt3,M[i_t3,1]],[xt3,yt3]])
T4 = np.array([[xt4,M[i_t4,1]],[xt4,yt4]])

plt.figure(1)
plt.plot(T1[:,0],T1[:,1],'k')
plt.plot(T2[:,0],T2[:,1],'k')
plt.plot(T3[:,0],T3[:,1],'k')
plt.plot(T4[:,0],T4[:,1],'k')

#Definição dos parâmetros da catenária

Tnom = 136.7e3
Tmax = 0.20*Tnom
ms = 117.30*9.81/1000
T0a = 0.19*Tnom
T0b = 0.19*Tnom
T0c = 0.19*Tnom

#Cálculo da catenária T0a
param = (xt1, xt2,yt1,yt2,T0a,ms)
x0a = fsolve(equation,xt1,args=param)[0]
y0a = yt1 - T0a/ms*(math.cosh(ms/T0a*(xt1-x0a))-1)

catenaria1_x = np.arange(xt1-x0a,xt2-x0a,1)
catenaria1_y = np.array([T0a/ms*(math.cosh(ms/T0a*x)-1) for x in catenaria1_x])

catenaria1_x_real = catenaria1_x + x0a
catenaria1_y_real = catenaria1_y + y0a

#Cálculo da catenária T0b
param = (xt2, xt3,yt2,yt3,T0b,ms)
x0b = fsolve(equation,xt2,args=param)[0]
y0b = yt2 - T0b/ms*(math.cosh(ms/T0b*(xt2-x0b))-1)

catenaria2_x = np.arange(xt2-x0b,xt3-x0b,1)
catenaria2_y = np.array([T0b/ms*(math.cosh(ms/T0b*x)-1) for x in catenaria2_x])

catenaria2_x_real = catenaria2_x + x0b
catenaria2_y_real = catenaria2_y + y0b

#Cálculo da catenária T0b
param = (xt3, xt4,yt3,yt4,T0c,ms)
x0c = fsolve(equation,xt4,args=param)[0]
y0c = yt3 - T0c/ms*(math.cosh(ms/T0c*(xt3-x0c))-1)

catenaria3_x = np.arange(xt3-x0c,xt4-x0c,1)
catenaria3_y = np.array([T0c/ms*(math.cosh(ms/T0c*x)-1) for x in catenaria3_x])

catenaria3_x_real = catenaria3_x + x0c
catenaria3_y_real = catenaria3_y + y0c

plt.figure(1)
plt.plot(catenaria1_x_real,catenaria1_y_real,'m')
plt.plot(catenaria2_x_real,catenaria2_y_real,'m')
plt.plot(catenaria3_x_real,catenaria3_y_real,'m')

#Gráfico da tração T0a
T1 = T0a + catenaria1_y*ms
Vtmax1 = Tmax*np.ones(len(catenaria1_x_real))

#Gráfico da tração T0b
T2 = T0b + catenaria2_y*ms
Vtmax2 = Tmax*np.ones(len(catenaria2_x_real))

#Gráfico da tração T0b
T3 = T0c + catenaria3_y*ms
Vtmax3 = Tmax*np.ones(len(catenaria3_x_real))

plt.figure(2)
plt.xlabel("x[m]")
plt.ylabel("Tração [N]")
plt.plot(catenaria1_x_real,T1,'b',catenaria1_x_real,Vtmax1,'r')
plt.plot(catenaria2_x_real,T2,'b',catenaria2_x_real,Vtmax2,'r')
plt.plot(catenaria3_x_real,T3,'b',catenaria3_x_real,Vtmax3,'r')

#Cálculo do comprimento
S1 = T0a/ms*(math.sinh(ms/T0a*(xt2-x0a))-math.sinh(ms/T0a*(xt1-x0a)))
S2 = T0b/ms*(math.sinh(ms/T0b*(xt3-x0b))-math.sinh(ms/T0b*(xt2-x0b)))
S3 = T0c/ms*(math.sinh(ms/T0c*(xt4-x0b))-math.sinh(ms/T0c*(xt3-x0b)))
print("O comprimento da primeira catenaria é:", S1,"metros")
print("O comprimento da primeira catenaria é:", S2,"metros")
print("O comprimento da primeira catenaria é:", S3,"metros")