import random
def run():
    number_found = False
    random_n = random.randint(0, 20)
    while not number_found:
        n = int(input("Intenta un numero: "))
        if n == random_n:
            print("Felicidades. Encontraste el numero ♥")
            number_found = True
        elif n > random_n:
            print("El numero es mas pequeño")
        else:
            print("El numero es mas grande")
if __name__ == '__main__':
    run()