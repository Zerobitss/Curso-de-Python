def run ():
    countries = {
        'mexico': 122,
        'colombia': 49,
        'argentina': 43,
        'chile': 18,
        'peru': 31
    }
    while True:
        country = str(input("Escribe un pais: ")).lower()
        try:
            print(f"el pais es: {country}, y la poblacion es: {countries[country]}m")
        except:
            print("No se encuentra ese pais en nuestro listado")
            return False
if __name__ == '__main__':
    run()