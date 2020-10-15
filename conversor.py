def conversor (moneda, valor_dolar):
    pesos = input("Cuantos "+ moneda +" tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tu cantidad en dolares es: "+ dolares +"$")
    return
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
    conversor( "Pesos colombianos",3900)
elif opcion == 2:
    conversor( "Pesos argentinos",74)
elif opcion == 3:
    conversor("Pesos mexicanos", 21)
elif opcion == 4:
    conversor("Pesos chilenos", 800)
elif opcion == 5:
    conversor("Bolivares", 450000)
else:
    print("Eligue una de las opciones del menu correctamente")
#dolar = input("Cuantos dolares tienes?: ")
#dolar = float(dolar)
#cambio = dolar * valor_dolar
#cambio = round(cambio, 2)
#cambio = str(cambio)
#print("Tu cantidad de bolivares es: "+cambio+"Bs")
