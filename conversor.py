pesos = input("Cuantos pesos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tu cantidad en dolares es: "+ dolares +"$")