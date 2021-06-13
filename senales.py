import numpy as np
import matplotlib.pyplot as plt
#este es un comentario
def Suma (serie1, serie2):
    ser1 = np.array(serie1)
    ser2 = np.array(serie2)
    a = len(ser1)
    b = len(ser2)
    if a>b:
        c = a-b
        for i in range (0,c):
            ser2 = np.append(ser2, 0)
    elif a<b: 
        c = b-a
        for i in range (0,c):
            ser1 = np.append(ser1, 0)
    sum = ser1 + ser2
    return sum
def Resta (serie1, serie2):
    ser1 = np.array(serie1)
    ser2 = np.array(serie2)
    a = len(ser1)
    b = len(ser2)
    if a>b:
        c = a-b
        for i in range (0,c):
            ser2 = np.append(ser2, 0)
    elif a<b: 
        c = b-a
        for i in range (0,c):
            ser1 = np.append(ser1, 0)
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
    ser.reshape(-1,k)
    for i in range (0,M-1):
        new = (ser[i]+ser[i+1])/2
        ant = ser[i]
        aux = np.append(aux, ser[i])
        aux = np.append(aux, new)
        aux = np.append(aux, ser[i+1])
    return aux
y=[1,2,3,4,5,6]
z=[1,2,1,2]
print("Original",y)
print("Original",z, "principal")
print("La suma es",Suma(z,y))
print("La Resta es",Resta(z,y))
print("La Amplificacion es",Amplifica(z,2))
print("La atenuacion es",Atenua(z,2))
print("La Diezmacion es",Diezmacion(z,2))
print("La interpolacion es", Interpolacion(z,2))
# INGRESO - tiempo [a,b)
a = -8
b = 8
dt = 0.1
k = 1  # desplazamiento
# PROCEDIMIENTO
t = np.arange(a,b,dt)
z = np.sin(t)
des = Desplazamiento(z,k,t)
