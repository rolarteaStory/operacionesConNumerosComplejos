import re
import math
import matplotlib.pyplot as plt 

def parteReal(numComplejo):
    real = numComplejo.split()
    return float(real[0])

def parteImaginaria(numComplejo):
    #a - b
    numComplejo = re.sub("i","",numComplejo)
    imaginario = numComplejo.split()
    if(imaginario[1] == "-"):
        return float(imaginario[2])*-1
    else:
        return float(imaginario[2])

def sumaComplejos(r1,r2,i1,i2):
    r3 = r1+r2
    i3 = i1+i2
    if i3 >= 0:
        resultado = str(r3)+" + "+str(i3)+"i"
    else:
        resultado = str(r3) + " - "+str(i3*-1)+"i"
    return resultado

def multiplicacionComplejos(r1,r2,i1,i2):
    #(a + bi)(c + di) = ac + [adi + cbi] + bd(-1)
    # [ac + bc(-1)] + [adi + cbi]
    parte_ac = r1*r2
    parte_bd = i1*i2*-1
    parte_media = (r1*i2) + (r2*i1)
    
    primera_parte = parte_ac + parte_bd
    
    if parte_media >= 0:
        resultado = str(primera_parte)+" + "+str(parte_media)+"i"
    else:
        resultado = str(primera_parte)+" - "+str(parte_media*-1)+"i"

    return resultado
    
def divisionComplejos(r1,r2,i1,i2):
    denominador = (r2*r2) + (i2*i2) #9 + 4 = 13
    numerador = multiplicacionComplejos(r1,r2,i1,i2*-1)
    resultado = numerador+" / "+str(denominador)
    return resultado

def potenciaComplejos(r1,i1,n):
    original = multiplicacionComplejos(r1,1,i1,0)
    if n == 0:
        resultado = "1 + 0i"
    elif n == 1:
        resultado = multiplicacionComplejos(r1,1,i1,0)
    
    while(n != 1):
        cr = int(parteReal(original))
        ci = int(parteImaginaria(original))
        numComplejo = multiplicacionComplejos(r1,cr,i1,ci)
        n -= 1
        original = numComplejo
        resultado = numComplejo
        
    return resultado

def raicesImaginarias(r2,i2,m): 
    respuestaReal = [None]*m
    respuestaImaginaria = [None]*m
    if r2 == 0 and i2 == 1:
        angulo = math.pi/2
        modulo = 1
    elif r2 == 0 and i2 == -1:
        angulo = (3*math.pi)/2
        modulo = 1
    elif r2 == 1 and i2 == 0:
        angulo = 0
        modulo = 1
    elif re == -1 and i2 == 0:
        angulo = math.pi
        modulo = 1
    else:
        angulo = ((math.atan(i2/r2)))
        modulo = math.sqrt((r2*r2)+(i2*i2))

    if r2<0:
        angulo = angulo + math.pi

    for i in range(m):
        respuestaReal[i] = (modulo**(1/m)) * (math.cos((angulo+(2*math.pi*i))/m))
        respuestaImaginaria[i] = (modulo**(1/m)) * (math.sin((angulo+(2*math.pi*i))/m))
    return respuestaReal, respuestaImaginaria

def exponencialComplejo(r1,i1):
    #e^(x+iy) = e^x cos (y) + ie^xseny
    exponencialReal = (math.e**(r1)) * math.cos(i1)
    exponencialImaginario = (math.e**(r1)) * math.sin(i1)
    if exponencialImaginario >= 0:
        resultado = f"{exponencialReal:.2f}"+" + "+f"{exponencialImaginario:.2f}"+"i"
    else:
        resultado = f"{exponencialReal:.2f}"+" - "+f"{exponencialImaginario*-1:.2f}"+"i"
    return resultado

def senoComplejos(r1,i1):
    exp_1 = multiplicacionComplejos(r1,0,i1,1)
    exp_2 = multiplicacionComplejos(r1,0,i1,-1)

    exp_1_ecuacion_r1 = parteReal(exp_1)
    exp_1_ecuacion_i1 = parteImaginaria(exp_1)
    exp_2_ecuacion_r2 = parteReal(exp_2)
    exp_2_ecuacion_i2 = parteImaginaria(exp_2)

    e_1 = exponencialComplejo(exp_1_ecuacion_r1,exp_1_ecuacion_i1)
    e_2 = exponencialComplejo(exp_2_ecuacion_r2,exp_2_ecuacion_i2)

    e_1_r1 = parteReal(e_1)
    e_1_i1 = parteImaginaria(e_1)
    e_2_r2 = parteReal(e_2)
    e_2_i2 = parteImaginaria(e_2)

    numerador = sumaComplejos(e_1_r1,e_2_r2*-1,e_1_i1,e_2_i2*-1)

    numerador_r1 = parteReal(numerador)
    numerador_i1 = parteImaginaria(numerador)

    resultado = divisionComplejos(numerador_r1,0,numerador_i1,2)
    return resultado

def cosenoComplejos(r1,i1):
    exp_1 = multiplicacionComplejos(r1,0,i1,1)
    exp_2 = multiplicacionComplejos(r1,0,i1,-1)

    exp_1_ecuacion_r1 = parteReal(exp_1)
    exp_1_ecuacion_i1 = parteImaginaria(exp_1)
    exp_2_ecuacion_r2 = parteReal(exp_2)
    exp_2_ecuacion_i2 = parteImaginaria(exp_2)

    e_1 = exponencialComplejo(exp_1_ecuacion_r1,exp_1_ecuacion_i1)
    e_2 = exponencialComplejo(exp_2_ecuacion_r2,exp_2_ecuacion_i2)

    e_1_r1 = parteReal(e_1)
    e_1_i1 = parteImaginaria(e_1)
    e_2_r2 = parteReal(e_2)
    e_2_i2 = parteImaginaria(e_2)

    numerador = sumaComplejos(e_1_r1,e_2_r2,e_1_i1,e_2_i2)

    numerador_r1 = parteReal(numerador)
    numerador_i1 = parteImaginaria(numerador)

    resultado = divisionComplejos(numerador_r1,2,numerador_i1,0)
    return resultado

def tangenteComplejos(r1,r2,i1,i2):
    z3 = sumaComplejos(r1,r2,i1,i2)

    z3_real = parteReal(z3)
    z3_imaginario = parteImaginaria(z3)

    numerador = senoComplejos(z3_real,z3_imaginario)
    denominador = cosenoComplejos(z3_real,z3_imaginario)

    numerador_real = parteReal(numerador)
    numerador_imaginario = parteImaginaria(numerador)

    denominador_real = parteReal(denominador)
    denominador_imaginario = parteImaginaria(denominador)

    resultado = divisionComplejos(numerador_real,denominador_real,numerador_imaginario,denominador_imaginario)

    return resultado

def parteReal_especial(ecuacion):
    ecuacion = re.sub("i","",ecuacion)
    x = ecuacion.split()
    resultado = float(x[0])/float(x[4])
    return float(resultado)

def parteImaginaria_especial(ecuacion):
    ecuacion = re.sub("i","",ecuacion)
    x = ecuacion.split()
    if x[1] == "+":
        resultado = float(x[2])/float(x[4])
    else:
        resultado = (float(x[2])*-1)/float(x[4])
    return float(resultado)

def graficas(real_1,real_2,imaginario_1,imaginario_2,suma,multiplicacion,potencia,nuevaDivision,nuevoSeno,nuevoCoseno,nuevoTan,exponencial,raicesR,raicesI,m):
    plt.xlabel('Reales')
    plt.ylabel('Imaginarios')
    plt.scatter(0,0,c="#868686",linewidth=1)
    plt.scatter(real_1,imaginario_1,c="#000000",linewidths=1)
    plt.scatter(real_2,imaginario_2,c="#000000",linewidths=1)
    plt.scatter(parteReal(suma),parteImaginaria(suma),c="r",linewidths=1)
    plt.scatter(parteReal(multiplicacion),parteImaginaria(multiplicacion),c="g",linewidths=1)
    plt.scatter(parteReal(potencia),parteImaginaria(potencia),c="y",linewidths=1)
    plt.scatter(parteReal(nuevaDivision),parteImaginaria(nuevaDivision),c="b",linewidths=1)
    plt.scatter(parteReal(nuevoSeno),parteImaginaria(nuevoSeno),c="#A52A2A",linewidths=1)
    plt.scatter(parteReal(nuevoCoseno),parteImaginaria(nuevoCoseno),c="#A12EE4",linewidths=1)
    plt.scatter(parteReal(nuevoTan),parteImaginaria(nuevoTan),c="#2EE4D1",linewidths=1)
    plt.scatter(parteReal(exponencial),parteImaginaria(exponencial),c="#EB73EF",linewidths=1)
    for i in range(m):
        plt.scatter(raicesR[i],raicesI[i],c="#F6A13F",linewidths=1)
    plt.title("Gris:Origen\nRojo:Suma,Mult:verde,Potencia:amarillo,Division:Azul\nSeno:cafe,Coseno:Morado,tan:azulClaro,\nExponencial:Rosa,Naranja:Raices")
    plt.grid()
    plt.show()

print("Ingresa dos números complejos de la siguiente forma:\na + bi   ó   a - bi\n")
numcomplejo_1 = input("Ingresa el primer numero complejo: ")
numcomplejo_2 = input("Ingresa el segundo numero complejo: ")
numN = input("escribe un numero N entero: ")
numM = input("escribe un numero M entero: ")

real_1 = parteReal(numcomplejo_1)
real_2 = parteReal(numcomplejo_2)
imaginario_1 = parteImaginaria(numcomplejo_1)
imaginario_2 = parteImaginaria(numcomplejo_2)
n = int(numN)
m = int(numM)
print("Del primer numero complejo\nLa partea real: "+str(real_1)+"\tLa parte imaginario: "+str(imaginario_1))
print("Del segundo numero complejo\nLa partea real: "+str(real_2)+"\tLa parte imaginario: "+str(imaginario_2))


suma = sumaComplejos(real_1,real_2,imaginario_1,imaginario_2)
print("La suma de los números es de: "+suma)

multiplicacion = multiplicacionComplejos(real_1,real_2,imaginario_1,imaginario_2)
print("la multiplicacion de los números es de: "+multiplicacion)

Division = divisionComplejos(real_1,real_2,imaginario_1,imaginario_2)
nuevaDivision = multiplicacionComplejos(parteReal_especial(Division),1,parteImaginaria_especial(Division),0)
print("La división del numero es de: "+nuevaDivision)

potencia = potenciaComplejos(real_1,imaginario_1,n)
print("La potencia del numero ("+numcomplejo_1+")^"+str(n)+" es de: "+potencia)

if(m==1 and m>0):
    print("La raiz es la misma ecuación: "+numcomplejo_2)
elif(m>0):
    raicesR,raicesI = raicesImaginarias(real_2,imaginario_2,m)
    print("\n")
    print("La raiz ("+numcomplejo_2+")^(1/"+str(m)+") es de: ")
    for i in range(m):
        print("Las raiz z"+str(i)+f" es: {raicesR[i]:.2f}+({raicesI[i]:.2f}i)")
    print("\n")
     
exponencial = exponencialComplejo(real_1,imaginario_1)
print("la ecuacion e^("+numcomplejo_1+") es de: "+exponencial)

seno = senoComplejos(real_1,imaginario_1)
nuevoSeno = multiplicacionComplejos(parteReal_especial(seno),1,parteImaginaria_especial(seno),0)
print("La ecuacion seno("+numcomplejo_1+") es de: "+nuevoSeno)

coseno = cosenoComplejos(real_2,imaginario_2)
nuevoCoseno = multiplicacionComplejos(parteReal_especial(coseno),1,parteImaginaria_especial(coseno),0)
print("La ecuacion coseno("+numcomplejo_2+") es de: "+nuevoCoseno)

tangente = tangenteComplejos(real_1,real_2,imaginario_1,imaginario_2)
nuevaTan = multiplicacionComplejos(parteReal_especial(tangente),1,parteImaginaria_especial(tangente),0)
print("La tangente tangente("+numcomplejo_1+"+("+numcomplejo_2+")) es de: "+nuevaTan+"\n")
#ecuaciones limpias
#gráficas
graficas(real_1,real_2,imaginario_1,imaginario_2,suma,multiplicacion,potencia,nuevaDivision,nuevoSeno,nuevoCoseno,nuevaTan,exponencial,raicesR,raicesI,m)

print("El programa ha finalizado con éxito")
