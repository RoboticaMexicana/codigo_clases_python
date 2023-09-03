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
