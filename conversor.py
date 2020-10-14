bolivares = input("Cuantos bolivares tienes?: ")
bolivares = float(bolivares)
valor_dolar = 400000
dolares = bolivares / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tu cantidad en dolares es: "+ dolares +"$")
dolar = input("Cuantos dolares tienes?: ")
dolar = float(dolar)
cambio = dolar * valor_dolar
cambio = round(cambio, 2)
cambio = str(cambio)
print("Tu cantidad de bolivares es: "+cambio+"Bs")
