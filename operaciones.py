import numpy as np
import matplotlib.pyplot as plt
#este es un comentario
def Suma (serie1, p1, serie2, p2):
    
    len_total_s1 = len(serie1)
    len_total_s2 = len(serie2)
    len_inter_s1 = len(serie1[:p1])
    len_inter_s2 = len(serie2[p2:])
    
    print('tamaño de serie1 hasta su interseccion: ', len_inter_s1)
    print('tamaño de serie2 hasta su interseccion: ', len_inter_s2)
    
    tam_total = len_inter_s1 + len_inter_s2
    
    print('tamaño de la nueva serie: ', tam_total)
        
    

def Resta (serie, factor):
    ser = np.array(serie)
    sum = ser - factor
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
z=[1,2,1,2,1,2]
z1 = [1,2,3,0,3]
print("Original",z)
print("La suma es: ",Suma(z,2,z1,1))
print("La Resta es",Resta(z,2))
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