def run ():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    # }
    poblacion_paises = {
        'Argentina' : 44_938_712,
        'Brasil' : 210_147_125,
        'Colombia' : 50_372_424,
    }
    # print(poblacion_paises['Argentina'])
    # print(poblacion_paises['Brasil'])
    # print(poblacion_paises['Colombia'])
    # print(poblacion_paises['Venezuela'])
    # for pais in poblacion_paises.keys():
    #     print (pais)
    # for pais in poblacion_paises.values():
    #     print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais + "tiene "+ str(poblacion) + " habitantes")
if __name__ == '__main__':
    run()