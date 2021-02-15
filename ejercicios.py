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
