#imprimir, metodos del comando print
"""print("hola mundo") #salto de linea 

print("mensaje 1", end = "-")
print("mensaje 2", end = "-")
print("mensaje 3", end = "-")

print("hola", "mundo", "curso", "python", sep="")

nombre = "Edu"
edad = 40

print("hola, soy {} y tengo {} años".format(nombre, edad))

print(f"hola, soy {nombre} y tengo {edad} años")

#-------------------------------------------------
#variables
entera = 10
flotante = 12.4
cadena = "texto"
boleana = True

# f-string 
print(f"la variable {boleana} es: ", type(boleana) )

#-------------------------------------------------

nombre = input("Ingresa tu nombre: ")
apellido_paterno = input("Ingresa tu apellido paterno: ")
apellido_materno = input("Ingresa tu apellido materno: ")
print("Tu nombre es:", nombre, apellido_paterno, apellido_materno)



num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))

print(f"la suma de los numeros {num1} y {num2} es: ", (num1 + num2))

#-------------------------------------------------
"""

#operadores matemáticos
"""
suma +
resta -
multiplicación *
división /
division entera //
módulo %
potencia **

hay tres opciones para resolver una potencia
***
pow()
math.pow()

"""

"""
num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresa otro número: "))

resultado = pow(num1,num2)

print(resultado)"""

#-------------------------------------------------

#operadores de asignación matemática
"""
x = 10
print(x)

x += 5
print(x)

x -= 5
print(x)

x *= 5
print(x)
"""
#-------------------------------------------------

# operadores de comparación
"""
igual que            ==
diferente            !=
mayor que             >
menor que             <
mayor o igual que    >=
menor o igual que    <=
"""

#condicion = 9 == 9
"""
num1 = int(input("Ingresa un número "))
num2 = int(input("Ingresa otro número "))


if num1 > num2:
    print("Se cumple")
else:
    print("No se cumple")
"""
#-------------------------------------------------
"""
fisica = float(input("¿Cúal es tu calificación en Física? "))
quimica = float(input("¿Cúal es tu calificación en Química? "))
literatura = float(input("¿Cúal es tu calificación en Literatura? "))

promedio = (fisica + quimica + literatura) / 3

print(promedio)

print(round(promedio, 2))
"""
#-------------------------------------------------
"""
fisica = float(input("¿Cúal es tu calificación en Física? "))
quimica = float(input("¿Cúal es tu calificación en Química? "))
literatura = float(input("¿Cúal es tu calificación en Literatura? "))

promedio = (fisica + quimica + literatura) / 3


if fisica < 6 or quimica < 6 or literatura < 6:
    print("El alumno reprobo una materia")

else:
    print("El alumno aprobo el curso con un promedio de", promedio)

#-------------------------------------listas
#-------------------------------------listas

"""
numeros_enteros = [100,2,355,4,-85,355]

numeros_flotantes = [3.5, 6.7, 12.67]

caracteres= ["A", "B", "x", "/", "@"]

lista_mixta = [12, "F", 12.4, "hola mundo", True]

lista_vacia = []
"""
#función len(), lonitud de una string o lista
print(len("lista"))

# 1 - append(elemento): Agrega un elemento al final de la lista.
print(numeros_enteros)
numeros_enteros.append(50)
print(numeros_enteros)

# 2 - extend
extend(iterable): Extiende la lista agregando todos los 
elementos de otro iterable (por ejemplo, otra lista) al final.
numeros_flotantes.extend(numeros_enteros)
print(numeros_flotantes)

# 3 - insert
insert(posición, elemento): Inserta un elemento en 
una posición específica de la lista.
numeros_flotantes.insert(0, 35)
print(numeros_flotantes)
"""
# 4 - remove
"""remove(elemento): Elimina la primera ocurrencia 
del elemento especificado de la lista.
lista1 = [0,1,0,2,0,3]
lista1.remove(0)
print(lista1)


# 5 - pop(índice): Elimina y devuelve(opcionalmente) el elemento en la posición 
# especificada o el último elemento si no se especifica un índice.
print(numeros_enteros)
indice = numeros_enteros.pop(0)
print(numeros_enteros, indice)

# 6- index(elemento): Devuelve el índice de la primera ocurrencia 
# del elemento especificado en la lista.
indice = numeros_enteros.index(355)
print(indice)


# 7 -count(elemento): Devuelve el número de veces que aparece el 
# elemento especificado en la lista.
repeticiones = numeros_enteros.count(355)
print(repeticiones)

# 8 - sort( reverse = False): Ordena los elementos de la lista 
# en orden ascendente 
print(numeros_enteros)
numeros_enteros.sort(reverse=True)
print(numeros_enteros)

# 9 - clear(): Elimina todos los elementos de la lista, dejándola vacía.
print(numeros_enteros)
numeros_enteros.clear()
print(numeros_enteros)

#10 - copy(): Se utiliza para crear una copia superficial de la lista
copia_lista = numeros_enteros.copy()
print(copia_lista)
"""



"""

#------ciclo while---Adivina el Número:----------------------------------------

import random

numero_aleatorio = random.randint(1, 10)
num_usuario = int(input("Adivina un número del 1 al 10 "))


while numero_aleatorio != num_usuario:
    print("No adivinaste :P")
    print("El número era", numero_aleatorio)
    numero_aleatorio = random.randint(1, 10)
    num_usuario = int(input("Adivina un número del 1 al 10 "))


print("Adivinaste!!! :D")

#---------------------Contador Regresivo:
num = int(input("Ingresa un número: "))

while num > 0:
    num = num - 1
    print(num + 1)
"""
#-------------------------------------------------
"""Suma de Números:
Solicita al usuario que ingrese números enteros positivos 
uno tras otro. Suma los números ingresados y muestra el resultado. 
Pide al usuario que confirme si desea continuar ingresando números.

suma = 0

while True:
    numero = input("Ingresa números a sumar, S para salir")

    if numero == "S":
        print("saliendo... ")
        break

    else:
        numero = int(numero)
        suma += numero

print(suma)
"""

#-------------------------------------------------

"""for for
#-------------------------------------------------
"""
"""
1. Imprimir Números Pares:
Escribe un programa que imprima todos 
los números pares del 1 al 20 utilizando 
un ciclo for.

for i in range(1,21,1):
    par = i % 2
    if par == 0:
        print(i)


#-------------------------------------------------

import time
suma = 0

for i in range(1,51,1):
    par = i % 2
    if par == 1:
        suma += i
        print(suma)

    #time.sleep(1)
#-------------------------------------------------

suma = 0
for numero in range(1, 51, 2):
    suma += numero

print("La suma de números impares del 1 al 50 es:", suma)
#-------------------------------------------------

num1 = int(input("ingresa un número: "))

for i in range(1, 11):
    resultado = num1 * i
    print(f"{num1} X {i} = {resultado}")

#-------------------------------------------------

nombres = ["Eduardo", "Mariana", "Pablo", "Armando", "Pedro"]

for i in nombres:
    print(i)

#-------------------------------------------------

palabra = input("Ingresa una palabra")
contador = 0

for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contador += 1
print(contador)
#-------------------------------------------------

numeros = [1,3,3,5,6]
suma = 0

for i in numeros:
    suma += i
print(suma)


#-------------------------------------------------

print("Números primos del 1 al 100:")
for numero in range(2, 101):
    es_primo = True
    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)

        
En esencia, un algoritmo es una receta o plan que guía la 
resolución de un problema.


#-------------------------------------------------

frase = input("Ingresa una frase: ")
letra = input("¿qué letra quieres contar? ")
conteo = 0

for i in frase:
    if i == letra:
        conteo = conteo + 1

print(conteo)

#-------------------------------------------------

num = int(input("tamaño del triangulo"))

for i in range(num + 1):
    #print(i)
    print(" ")
    for j in range(i):
        print("*", end="")


#-----funciones--------------------------------------------
#-----funciones----Suma de Dos Números---------------------------------------

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

def suma(n1, n2):
    resultado = n1 + n2
    return resultado

print(suma(num1, num2))

#-------Cálculo del Área de un Círculo:------------------------------------------

from math import pi

radio = int(input("Ingresa el radio del círculo: "))

def area(r):
    resultado = pi * r**2
    return resultado

area_circulo = area(radio)

print(area_circulo)

#------ Contador de Palabras-------------------------------------------

frase = input("Escribe una frase: ")

def contador(f):
    palabras = f.split()
    return len(palabras)

print(contador(frase))

#------ Conversión de Temperatura:-------------------------------------------
#  ºF = (ºC · 1,8) + 32

while True:
        
    print("Que desea convertir? ")
    print("F - celsius a fahr")
    print("C - fahr a celsius")
    opcion = input("Ingrese su elección: ")

    if opcion == "F":

        celsius = float(input("Ingrese grados celsius: "))

        def temp(c):
            farh = (c * 1.8) + 32
            return farh

        print(temp(celsius))

    if opcion == "C":
    # °C = (°F – 32) x 5/9
        fahrenheit = float(input("Ingrese grados fahrenheit: "))

        def temp2(f):
            cels = (f - 32) * 5/9
            return cels

        print(temp2(fahrenheit))

#------------------ Encontrar el Máximo y el Mínimo:--------------------------------

numeros  = [7,4,3,8,4,6,2,9,23,76,3,12,97,435,1]


def maxi(lista):
    minimo = numeros[0]

    for i in lista:
        if i < minimo:
            minimo = i
    return minimo

def mini(lista):
    maximo = numeros[0]

    for i in lista:
        if i > maximo:
            maximo = i
    return maximo

print(maxi(numeros))
print(mini(numeros))


#------------------ Contar Dígitos en un Número:

numero = 1234

def dig(num):
    digitos = len(str(num))
    return digitos

print(dig(numero))


##------------------encontrar valores repetidos
lista = [0,0,5,6,7,8,9,0,7,0]
num = int(input("Ingresa numero a buscar repetido en lista: "))
indice =  -1

for i in lista:
    indice = indice + 1

    if i == num:
        print(indice)
#------------------#------------------#------------------#------------------
"""

#Calculadora
#------------------------------------
from math import sqrt

def suma(n1, n2):
    resultado = n1 + n2
    return resultado

def resta(n1, n2):
    resultado = n1 - n2
    return resultado

def multiplicacion(n1, n2):
    resultado = n1 * n2
    return resultado

def division(n1, n2):
    resultado = n1 / n2
    return resultado

def potencia(base, exp):
    resultado = base ** exp
    return resultado

def raiz(n1):
    resultado = sqrt(n1)
    return resultado


while True:
    try:
    
        print("\n\n-------MENÚ--------")
        print("1 - SUMA-----------")
        print("2 - RESTA----------")
        print("3 - MULTIPLICACIÓN-")
        print("4 - DIVISIÓN-------")
        print("5 - POTENCIA-------")
        print("6 - RAÍZ-----------")
        print("7 - SALIR----------")

        modo = int(input("ingresa la opción: "))

        if modo == 7:
            break

        elif modo == 1:
            print("Elegiste suma")
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            print("\n\nEl resultado es:", suma(num1, num2))

        elif modo == 2:
            print("Elegiste resta")
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            print("\n\nEl resultado es:", resta(num1, num2))

        elif modo == 3:
            print("Elegiste multiplicacion")
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            print("\n\nEl resultado es:", multiplicacion(num1, num2))

        elif modo == 4:
            try:
                print("Elegiste división")
                num1 = int(input("Ingresa el primer número: "))
                num2 = int(input("Ingresa el segundo número: "))
                print("\n\nEl resultado es:", division(num1, num2))
            except ZeroDivisionError:
                print("No se puede dividir entre CERO ")

        elif modo == 5:
            print("Elegiste potencia")
            num1 = int(input("Ingresa la base: "))
            num2 = int(input("Ingresa el exponente: "))
            print("\n\nEl resultado es:", potencia(num1, num2))

        elif modo == 6:
            print("Elegiste raíz")
            num1 = int(input("Ingresa el número: "))
            print("\n\nEl resultado es:", raiz(num1))

        else: 
            print("\n\nOpción inválida")

    except ValueError:
        print("Opción no válida ")
