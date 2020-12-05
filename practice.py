# nombre = str(input("Escribe tu nombre: "))
# print (f"Hola! {nombre.upper()}")
# print("Su nombre tiene una cantidad de letras de: ", len(nombre))
# aritmetica = (((3+2) / (2*5)) ** 2)
# print(aritmetica)
# def run():
#     cost_per_hour = 27800
#     worked = int(input("Escribe la cantidad de horas trabajadas: "))
#     result = worked * cost_per_hour
#     print(f"Su pago por horas trabajadas es: {result}$ Pesos colombianos")
# if __name__ == '__main__':
#     run()
# def run():
#     while True:
#         n = int(input("Escribe un numero entero positivo: "))
#         if n <= 0:
#             print("Escribe un numero entero positivo mayor a 0")
#             return False
#         else:
#             suma = n * (n + 1) / 2
#             print(f"El resultado es: {suma}")
# if __name__ == '__main__':
#     run()
"""
calculo de indice de masa coorporal
Fórmula: peso (kg) / [estatura (m)]2
"""
def indice (kg, metros):
    imc = kg / (metros) **2
    return imc
if __name__ == '__main__':
    kg = float(input("Ingresa tu peso: "))
    metros = float(input("Ingresa tu estatura en metros: "))
    imc = indice(kg,metros)
    print(round(imc, 2))
