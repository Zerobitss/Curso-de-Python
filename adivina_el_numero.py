import random
def run():
    menu = """
🐱‍👓Bienvenido al juego adivina el numero 🐱‍👤:

---------------------------------------------
Es algo sencillo solamente tienes que colocar
tu nombre y seguido de tu nombre, por cierto
solamente tienes 3 intentos que te diviertas!
---------------------------------------------

"""
    print(menu)
    nombre = input("Ingresa tu nombre: ")
    vida = 3
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Escribe un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if vida > 0 :
            if numero_elegido < numero_aleatorio:
                vida -= 1
                print("Elige un numero mas grande "+ nombre +" Tus puntos de vida son: "+str(vida))
                numero_elegido = int(input("Elige otro numero del 1 al 100: "))
            elif numero_elegido > numero_aleatorio:
                vida -= 1
                print("Elige un numero mas pequeño " + nombre + " Tus puntos de vida son: "+str(vida))
                numero_elegido = int(input("Elige otro numero del 1 al 100: "))
            elif numero_elegido == numero_aleatorio:
                print("Ganaste!"+" "+nombre)
        else:
            print("Lo siento tus puntos de vida no son suficientes")
            break
if __name__ == '__main__':
    run()
