import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
#este es un comentario
def Suma (serie, factor):
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
def Resta (serie, factor):
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
def Desplazamiento(serie, k):
    for s in serie:
        s = s + k
    print(serie)
    return serie
def Amplifica(serie, factor):
    expande = np.dot(serie, factor)
    return (expande)
def Atenua(serie, factor):
    comprime = np.dot(serie, 1/factor)
    return (comprime)
def reflexion(serie):
    res = serie[::-1]
    return res
def Diezmacion(serie, k):
    np.asarray(serie)
    res = serie[:-k:k]
    return res
def Interpolacion(serie,tipo):
    y = np.arange(0,len(serie))
    res = interp1d(serie, y)
    print(res)
    return res
def convolucion(serie1, serie2):
    res = np.convolve(serie1,serie2,mode="same")
    return res

z=[1,2,1,2,1,2]
x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2]
h = [0.25, 4, 3, 1, 0, 2] 
print("Original",x)
#print("La suma es",Suma(z,2))
#print("La Resta es",Resta(z,2))
#print("El desplazamiento es", Desplazamiento(x, -3))
#print("El reflejo de x es ", reflexion(x))
print("La Amplificacion es",Amplifica(x,2))
print("La atenuacion es",Atenua(x,2))
#print("La Diezmacion es",Diezmacion(x,2))
print("La interpolacion es", Interpolacion(x,"linear"))
print("La convolucion es ", convolucion(x,h))
# INGRESO - tiempo [a,b)
a = -8
b = 8
dt = 0.1
k = 1  # desplazamiento
# PROCEDIMIENTO
