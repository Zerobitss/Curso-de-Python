import random
def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasena = []
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    return contrasena
def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)
    division = 10 / 2 + 5 * 7
    print(division)
    nombre = 'jose'
    edad = 26
    result = nombre * edad
    print(result)
if __name__ == '__main__':
    run()