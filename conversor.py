menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos mexicanos
4 - Pesos chilenos
5 - Bolivares

Eligue una opcion: """
opcion = int(input(menu))
if opcion == 1:
    pesoscol = input("Cuantos pesos Colombianos tienes?: ")
    pesoscol = float(pesoscol)
    valor_dolar = 3900
    dolares = pesoscol / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu cantidad en dolares es: "+ dolares +"$")
elif opcion == 2:
    pesosar = input("Cuantos pesos Argentinos tienes?: ")
    pesosar = float(pesosar)
    valor_dolar = 77.41
    dolares = pesosar / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu cantidad en dolares es: "+ dolares +"$")
elif opcion == 3:
    pesosmex = input("Cuantos pesos Mexicanos tienes?: ")
    pesosmex = float(pesosmex)
    valor_dolar = 21
    dolares = pesosmex / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu cantidad en dolares es: "+ dolares +"$")
elif opcion == 4:
    pesoschil = input("Cuantos pesos Chilenos tienes?: ")
    pesoschil = float(pesoschil)
    valor_dolar = 800
    dolares = pesoschil / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu cantidad en dolares es: "+ dolares +"$")
elif opcion == 5:
    bolivares = input("Cuantos bolivares tienes?: ")
    bolivares = float(bolivares)
    valor_dolar = 400000
    dolares = bolivares / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu cantidad en dolares es: "+ dolares +"$")
else:
    print("Eligue una de las opciones del menu correctamente")
#dolar = input("Cuantos dolares tienes?: ")
#dolar = float(dolar)
#cambio = dolar * valor_dolar
#cambio = round(cambio, 2)
#cambio = str(cambio)
#print("Tu cantidad de bolivares es: "+cambio+"Bs")
