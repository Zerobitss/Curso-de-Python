# nombre = input("Escribe tu nombre: ")
# saludo = 'Bienvenido a casa! '
# print(f'{saludo}{nombre}')
# print(len(saludo+nombre))
# usuario1 = input("Escribe tu nombre: ")
# edad1 = int(input("Escribe tu edad: "))
# usuario2 = input("Escribe otro nombre nombre: ")
# edad2 = int(input("Escribe tu edad: "))

# if edad1 > edad2:
#     print(f'{usuario1} es mayor que {usuario2}')
# elif edad1 < edad2:
#     print(f'{usuario1} es menor que {usuario2}')
# else:
#     print(f'Tanto como {usuario1} y {usuario2} tienen la misma edad')
# x = 0.0
# for i in range(10):
#     x += 0.1

# if x == 1.0:
#     print(f'x = {x}')
# else:
#     print(f'x != {x}')
# objetivo = int(input("Escoge un entero: "))
# respuesta = 0
# while respuesta**2 < objetivo :
#     print(respuesta)
#     respuesta +=1
# if respuesta**2 == objetivo:
#     print(f'La raiz cuadrada de {objetivo} es {respuesta}')
# else:
#     print(f'{objetivo} no tiene raiz cuadrada exacta')
# x = "awesome"

# def myfunc():
#   global y
#   y = 'great'
#   print("Python is " + x + y)

# myfunc()
# print(y)
# def suma(a, b):
#     """ Suma dos valores a y b.
#     param int a cualquier entero
#     param int b cualquier entero
#     returns la sumatoria de a y b
#     """
#     total = a + b
#     print('mensaje')
#     return total

# suma()
# def factorial (n):
#     """Calcula el factorial de n.
#     n int > 0.
#     returns n!
#     """
#     print(n)
#     if n == 1:
#         return 1
#     return n * factorial(n - 1 )
# n = int(input("Escribe un entero: "))
# print(factorial(n))
# def suma (n):
#     print(n)
#     if n == 1:
#         return 1
#     else:
#         return n + suma (n - 1)
# n = int(input("Escribe un numero: "))
# print(suma(n))
my_range = range (0, 100)
for i in my_range:
    if i % 2 > 0:
        print(i)