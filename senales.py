import numpy as np
import matplotlib.pyplot as plt
#serie 1 y 2 iguala posiciones en le plano para suma/resta
def preparacion(serie1,serie2):
    nev_s1=[]
    pos_s1=[]
    nev_s2=[]
    pos_s2=[]
    #divide serie 1 en antes de origen y despues de origen
    flag=0
    for i in range(len(serie1)):
        if serie1[i]=="o":
            flag=1
        elif flag==0:
            nev_s1.append(serie1[i])
        else:
            pos_s1.append(serie1[i])
    a_s1=len(nev_s1)
    b_s1=len(pos_s1)
    #divide serie 1 en antes de origen y despues de origen
    flag=0
    for i in range(len(serie2)):
        if serie2[i]=="o":
            flag=1
        elif flag==0:
            nev_s2.append(serie2[i])
        else:
            pos_s2.append(serie2[i])
    a_s2=len(nev_s2)
    b_s2=len(pos_s2)
    #empata partes positivas
    if b_s1>b_s2:
        c = b_s1-b_s2
        for i in range (0,c):
            pos_s2.append(0)
    elif b_s1<b_s2: 
        c = pos_s2-pos_s1
        for i in range (0,c):
            pos_s1.append(0)
    #empata partes negativa
    if a_s1>a_s2:
        c = a_s1-a_s2
        for i in range (0,c):
            nev_s2.insert(0,0)
    elif a_s1<a_s2: 
        c = a_s2-a_s1
        for i in range (0,c):
            nev_s1.insert(0,0)
    #junta serie1
    for i in range(len(nev_s1)):
        ser1.append(nev_s1[i])
    for i in range(len(pos_s1)):
        ser1.append(pos_s1[i])
    #junta serie2
    for i in range(len(nev_s2)):
        ser2.append(nev_s2[i])
    for i in range(len(pos_s2)):
        ser2.append(pos_s2[i])
def Suma (serie1, serie2):
    ser1 = np.array(serie1)
    ser2 = np.array(serie2)
    sum = ser1 + ser2
    return sum
def Resta (serie1, serie2):
    ser1 = np.array(serie1)
    ser2 = np.array(serie2)
    sum = ser1 - ser2
    return sum
def Desplazamiento(serie, k, t):
    serie = np.sin(t)
    des= np.sin(t+k)
    plt.figure(1)
    plt.plot(t,serie,label='Original x(t)')
    plt.plot(t,des,label='Dezplazamiento x(t+k)')
    plt.axvline(0)
    plt.xlabel('t')
    plt.legend(loc='lower left')
    plt.show()
def Amplifica(serie, factor):
    expande = np.dot(serie, factor)
    return (expande)
def Atenua(serie, factor):
    comprime = np.dot(serie, 1/factor)
    return (comprime)
def Diezmacion(serie, k):
    ser = np.array(serie)
    N = len(ser)
    return ser[0:N:k]
def Interpolacion(serie,k):
    ser = np.array(serie)
    M = len(ser)
    N = M*2
    aux = []
    #ser.reshape(-1,k)
    for i in range (0,M-1):
        new = (ser[i]+ser[i+1])/2
        ant = ser[i]
        aux = np.append(aux, ser[i])
        aux = np.append(aux, new)
        aux = np.append(aux, ser[i+1])
    return aux
y=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,"o",0,1,2]
z=[0.25,"o",4,3,1,0,2]
ser1=[]
ser2=[]

preparacion(z,y)
print("Original",y)
print("Original",z, "principal")
print("Original",ser2)
print("Original",ser1, "principal")
print("La suma es",Suma(ser1,ser2))
print("La Resta es",Resta(ser2,ser1))
print("La Amplificacion es",Amplifica(ser1,2))
print("La atenuacion es",Atenua(ser1,2))
print("La Diezmacion es",Diezmacion(ser1,2))
print("La interpolacion es", Interpolacion(ser1,2))
# INGRESO - tiempo [a,b)
a = -8
b = 8
dt = 0.1
k = 1  # desplazamiento
# PROCEDIMIENTO
t = np.arange(a,b,dt)
ser1 = np.sin(t)
des = Desplazamiento(ser1,k,t)