def enumeracion():
    objetivo = int(input("Escoge un entero: "))
    respuesta = 0
    while respuesta**2 < objetivo :
        print(respuesta)
        respuesta +=1
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')
def aproximacion():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')
def busqueda_binaria():
    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
            respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
menu = """
🙌Bienvenido Con este programa podras hacer busqueda de raices cuadradas con los siguientes 3 metodos🐱‍👓:

1 - Enumeracion
2 - Aproximacion
3 - Busqueda binaria

Eligue una opcion: """
opcion = int(input(menu))
if opcion == 1:
    print("Haz eleguido el metodo Enumeracion exhaustiva")
    enumeracion()
elif opcion == 2:
    print("Haz eleguido el numero aproximacion")
    aproximacion()
elif opcion == 3:
    print("Haz eleguido el metodo busqueda binaria")
    busqueda_binaria()
else:
    print("Elige una opcion correcta porfavor!")
