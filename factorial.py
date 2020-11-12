def factorial(n):
    if n == 0: #Caso base
        return True #Devuelve verdadero en caso de llegar a 0
    print(n) #Imprimir el paso del factorial
    return n * factorial(n - 1) #Calculo factorial (n-1) para que encada iteracion vaya bajando el valor
if __name__ == "__main__":
    n = int(input("Escribe un numero: "))
    result = factorial(n)
    print(result )