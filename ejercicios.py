-------------------------------------------------------------------
nA =  float(input('Nota del primer parcial'))
nB =  float(input('Nota del segundo parcial'))
nC =  float(input('Nota del tercer parcial'))
IN =  float(input('Poner el numero de insistencias'))

A = nA * 0.35
B = nB * 0.35
C = nC * 0.30

R = A + B + C

if (R >= 3.0):
    if (IN < 12):
        print("felicidades su nota final fue de " + str(R))
if (R < 3.0):
    print("usted no paso")

if (IN > 12):   
    print("usted perdio por inasistencias")
-------------------------------------------------------------------- 
PR =  int(input('Ingrese el precio de su producto'))

PRI = (PR * 5)/100
R = PR + PRI 

print("el precio de su producto sin IVA es " + str(PR) + " y con IVA " + str(R))
--------------------------------------------------------------------
r =  int(input('Ingrese el radio de el circulo'))

R = r * r
A = 3.1416 * R
 
print("el area de la circunferencia es " + str(A))
--------------------------------------------------------------------
p =  int(input('Ingrese su peso en kilos'))
a =  int(input('Ingrese su altura en centimetros'))
A = a / 100
AF= A * A
imc = p / AF

if (imc < 18.5):
    print("usted esta tan flaco que parece baretero")

if (imc > 18.5):
    if (imc < 24.9):
        print("usted esta normal")

if (imc > 25):
    if (imc < 29.9):
        print("un poquito de Gym no te caeria nada mal para bajar los kilos de mas")

if (imc > 30):
    print("eres mas grasa que persona")             
--------------------------------------------------------------------
pb =  int(input('Ingrese su calificacion del primer bimestre'))
sb =  int(input('Ingrese su calificacion del segundo bimestre'))

t = pb + sb
P = t / 2

if (P >= 3.5):
    print("tu nota es " + str(P) + " felicidades pasaste")              

if (P < 3.5):           
    print("lo siento no pasaste")
--------------------------------------------------------------------
d =  int(input('ingrese la distancia en km'))
a =  int(input('digite 1 si va a ingresar el tiempo en minutos o 2 en horas'))

if (a == 2):
    t =  int(input('ingrese las horas'))
    v = d / t
    print("la velocidad a la que tienes que ir es " + str(v) +"km/h")
if (a == 1):
    t = int(input('ingrese los minutos'))
    T = t * (1 / 60)
    v = d / T 
    print("la velocidad a la que tienes que ir es " + str(v) +"km/h")
--------------------------------------------------------------------- 
nEM =  int(input('ingrese el numero de empleados'))
kHO =  int(input('ingrese el numero de horas'))

k = kHO * 1

print("necesita " + str(nEM) + " empleados para hacer la actividad en " + str(k) + " horas")
---------------------------------------------------------------------       
x =  int(input('ingrese el primer numero'))
y =  int(input('ingrese el segundo numero'))
z =  int(input('ingrese 1 para sumar 2 para restar 3 para multiplicar 4 para dividir 5 para potencia'))

if (z == 1):
   r = x + y
   print(r)

if (z == 2):
   r = x - y
   print(r)

if (z == 3):
   r = x * y 
   print(r)

if (z == 4):
   r = x / y
   print(r)

if (z == 5):
   r = x ** y
   print(r)   
-----------------------------------------------------------------------
m =  int(input('ingrese la masa de el objeto en Kg'))
Us =  float(input('ingrese el coeficiente de rozamiento'))
a = Us * 9.8
F = m * a
print("la fuerza es de " + str(F))
-----------------------------------------------------------------------
c =  int(input('ingrese la temperatura en grados celcios'))

F = (c * (9/5)) + 32
K = c + 273.15 

print("en farenthei son " + str(F) +", y en kelvin son " + str(K)+",") 
-----------------------------------------------------------------------
b =  int(input('ingrese la base del rectangulo'))
a =  int(input('ingrese la altura del rectangulo'))

A = b * a
P = (2*a)+(2*b)

print("el area es " + str(A) + " y el perimetro es " + str(P))
-----------------------------------------------------------------------
from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))

x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")

else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)
------------------------------------------------------------------------
h =  int(input('ingrese el numero de horas'))
vh =  int(input('ingrese el valor de una hora pagada en dolares'))

t = vh * h
T = (t * 10) / 100
Td = t - T

if (Td < 300):
    td2 = (Td * 2) / 100
    print("el sueldo de el empleado es " +str(td2))

else:
    print("el sueldo del empleado es " + td)  
------------------------------------------------------------------------
print("ingrese 3 numeros enteros diferenetes")
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))
a = int(input("ingrese el numero a"))
b = int(input("ingrese el numero b"))
c = int(input("ingrese el numero c"))

if (e == 1):    
    if (a > b):
        if (a > c):
            if(b > c):
               print(a, b, c)
            else:
               print(a, c, b)
    if (c > a):
        if (c > b):
            if(b > a):
               print(c, b, a)
            else:
               print(c, a, b)
    if (b > a):
        if (b > c):
            if(a > c):
               print(b, a, c)
            else:
               print(b, c, a)


if (e == 2):
    if (a < b):
        if (a < c):
            if(b < c):
               print(a, b, c)
            else:
               print(a, c, b)
    if (c < a):
        if (c < b):
            if(b < a):
               print(c, b, a)
            else:
               print(c, a, b)
    if (b < a):
        if (b < c):
            if(a < c):
               print(b, a, c)
            else:
               print(b, c, a)

if (a == b):
    print("b y a son iguales")
    if (a == c):
        print("a y c son iguales")
        if(b == c):
           print(" b y c con iguales")
           if(a == b == c):
              print("todos son iguales")
-------------------------------------------------------------------------------
            
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:43:23 2021

@author: Carlos
"""
print("SISTEMA DE NOTAS DE UN CURSO DE PROGRAMACIÓN")

#Entrada

numeroEstudiantes=int(input("Digite la cantidad de estudiantes del grupo : "))

# Declarar la variable que controla el ciclo
contadorRepeteciones = 0
cantidadEstudiantesAprobaron=0
cantidadEstudiantesReprobaron=0
sumaDefinitivaEstudiantes=0.0
sumaDefinitivaEstudiantesAprobaron=0.0
sumaDefinitivaEstudiantesReprobaron=0.0
promedioDefinitivaEstudiantes=0.0
promedioDefinitivaEstudiantesAprobaron=0.0
promedioDefinitivaEstudiantesReprobaron=0.0
#Proceso
#  Iniciar el ciclo

for contadorRepeteciones in range(numeroEstudiantes):
    #  Lectura de las notas de cada estudiante
    nombreEstudiante   = input("Digite nombre del estudiante : ")
    notaUnoEstudiante  = float(input("Digite la nota del primer parcial del estudiante : "))
    notaDosEstudiante  = float(input("Digite la nota del segundo parcial del estudiante : "))
    notaTresEstudiante = float(input("Digite la nota del tercer parcial del estudiante : "))
    #  Calcular la definitiva de cada estudiante
    notaDefinitiva = (notaUnoEstudiante+notaDosEstudiante+notaTresEstudiante)/3
    #Sumar las definitivas de los estudiantes para calcular el promedio
    sumaDefinitivaEstudiantes=sumaDefinitivaEstudiantes+notaDefinitiva
    print("1.  La definitiva es: ", notaDefinitiva)
    
    if(notaDefinitiva>=3.0):
        cantidadEstudiantesAprobaron=cantidadEstudiantesAprobaron+1
        #  Sumar las notas de los estudiantes que aprobaron
        sumaDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron+notaDefinitiva
    else:
        cantidadEstudiantesReprobaron=cantidadEstudiantesReprobaron+1
        #  Sumar las notas de los estudiantes que reprobaron
        sumaDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron+notaDefinitiva
    #  Incrementar la variable que controla el ciclo
    contadorRepeteciones = contadorRepeteciones+1
    
    #  Fin del ciclo
# Calcular el promedio del grupo
    
promedioDefinitivaEstudiantes=sumaDefinitivaEstudiantes/numeroEstudiantes   

if (cantidadEstudiantesAprobaron>0):
    promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron/cantidadEstudiantesAprobaron 
if (cantidadEstudiantesReprobaron>0):
    promedioDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron/cantidadEstudiantesReprobaron 

print("OTROS CALCULOS")
print("2.  Cantidad de estudiantes que aprobaron : ", cantidadEstudiantesAprobaron)
print("3.  Cantidad de estudiantes que reprobaron : ", cantidadEstudiantesReprobaron)
print(f"4.  Promedio del grupo : {promedioDefinitivaEstudiantes:.2f}")
print("5.  Promedio de estudiantes que aprobaron : ", promedioDefinitivaEstudiantesAprobaron)
print(f"6.  Promedio de estudiantes que reprobaron :{promedioDefinitivaEstudiantesReprobaron:.1f} ")            
----------------------------------------------------------------------------------------------------------------
x =  int(input('ingrese el primer numero'))
y =  int(input('ingrese el segundo numero'))
seleccionOp =  int(input('ingrese 1 para sumar 2 para restar 3 para multiplicar 4 para dividir 5 para potencia'))

if (seleccionOp == 1):
   r = x + y
   print(r)

if (seleccionOp == 2):
   r = x - y
   print(r)

if (seleccionOp == 3):
   r = x * y 
   print(r)

if (seleccionOp == 4):
   r = x / y
   print(r)

if (seleccionOp == 5):
   r = x ** y
   print(r)       
--------------------------------------------------------------
x =  int(input('ingrese el primer numero'))
y =  int(input('ingrese el segundo numero'))
seleccionOp =  int(input('ingrese 1 para sumar 2 para multiplicar 3 para dividir'))

if (seleccionOp == 1):
   r = x + y
   print(r)

if (seleccionOp == 2):
   r = x * y
   print(r)

if (seleccionOp == 3):
   r = x / y 
   print(r)
----------------------------------------------------------------
a = int(input("dime el año"))
m = int(input("dime el mes"))
d = int(input("dime el dia"))

def comprobar_fecha(a, m, d,):
 
    #Array que almacenara los dias que tiene cada mes (si el ano es bisiesto, sumaremos +1 al febrero)
    dias_mes = [31, 28, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
 
 
    if((a%4 == 0 and a%100 != 0) or a%400 == 0):
        dias_mes[1] += 1
 
    if(m < 1 or m > 12):
        return False

    m -= 1
    if(d <= 0 or d > dias_mes[m]):
        return False
 
    return True
 
 
 
 
 
correcta = comprobar_fecha(a, m, d,)
 
#Mostrar el resultado:
if(correcta):
    print("\n\nLa fecha entrada es CORRECTA\n")
 
else:
    print("\n\nLa fecha entrada es FALSA\n")
--------------------------------------------------------------------
boton = int(input("1 para subir 2 para bajar"))


if(boton == 1):
    for i in range(26):
        subir = int(input("1 para subir"))
        if(subir == 1):
            i = i + 1
            print(i)

if(boton == 2):    
    for j in range(25, 1, -1):
        subir = int(input("2 para bajar"))
        if(boton == 2):
            j = j - 1
            print(j)          
---------------------------------------------------------------------
entrar = int(input("para entrar al asensor oprima 1"))


if(entrar == 1):
    for i in range(26):
        boton = int(input("1 para subir 2 para bajar"))
        if(boton == 1):
            i = i + 1
            print(i)
        if(boton == 2):    
            for j in range(i, 1, -1):
                boton = int(input("2 para bajar 1 para subir"))
                if(boton == 2):
                    j = j - 1
                    print(j) 
                if(boton == 1):
                    i = i + 1
                    print(i)                       
---------------------------------------------------------------------------
print("--------calculadora de divisas--------")
print("pesos mexicanos y colombianos")

E = int(input("ingresa 1 si quieres pesos COL a MEX y 2 de MEX a COL"))

if(E == 1):
    pcol = int(input("dime la cantidad de pesos colombianos")) 
    resultado = pcol * 0.0057
    print("el resultado de tu calculo es " + str(resultado))
if(E == 2):
    pmew = float(input("dime la cantidad de pesos mexicanos"))
    resultado = pmew * 176.54 
    print("el resultado de tu calculo es " + str(resultado))
-------------------------------------------------------------------------
nom = str(input('dime tu nombre'))
sexo =  str(input('dime tu sexo escribe M o F'))
years =  int(input('dime tu edad'))

if (years > 18):
    print('hola ' + nom + ' de sexo ' + sexo + ' puedes votar')


else:
    print('lo siento no puedes votar')
--------------------------------------------------------------------------
num =  int(input('dime el numero para imprimir su tabla de multiplicar'))

for i in range(11):
    R = num * i

    print(R)
---------------------------------------------------------------------------
factorial=1
print("Dame un numero")
x=eval (input())
for i in range (1,x+1):
    factorial=factorial*i
 
print(factorial)
