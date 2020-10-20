def es_primo (numero):
    contador = 0
    for i in range (2, numero + 1):       
        if numero % i == 0:#es par (no es primo)
            contador += 1
        if contador == 0:# es primo( por eso no incremento el contador)
            return True
    else:
        return False
def run ():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")
if __name__ == "__main__":
    run()
""" Hey ! 

simplemente borre unas lineas que no eran necesarias y empece el rango desde 2
para poder hacer la validacion y que no me tome 1 como primo (cuando no es asi) y asi
el ejercicio quedo un poco mas corto y facil de leer """