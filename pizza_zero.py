def plato():
    menu_principal = ['Pizzas','Pasta','Ensaladas']
    menu_eleccion = [menu_pizzas(), menu_pasta(), menu_ensalada()]
    opcion_menu = int(input("1.-Pizzas\n2.-Pasta\n3.-Ensaladas\nQue deseas comer hoy: "))
    if (opcion_menu <= len(menu_principal)):
        print(f"Tu eleccion fue: {menu_principal[opcion_menu-1]}")
        iterador(menu_eleccion[opcion_menu-1])
        menu_eleccion = menu_eleccion[opcion_menu-1]
        plato = menu_principal[opcion_menu-1]
        return plato, menu_eleccion
def plato_sabor():
        menu_eleccion = plato()
        iterador(menu_eleccion[1])
        opcion_plato = int(input("Que deseas pedir: "))
        for j in range(len(menu_eleccion[1])):
            if opcion_plato == j:
                print(f"Pediste una {menu_eleccion[0]}, {menu_eleccion[1][opcion_plato-1]}")
        sabor = menu_eleccion[1][opcion_plato-1]
        pedido = menu_eleccion[0]+", "+ sabor
        return pedido
def pedido_extra():
    adicional = extras()
    extra = []
    if adicional is True:
        adicionales = int(input("\n1.-Aperitivos\n2.-Salsas\nQue deseas agregar: "))
        if adicionales == 1:
            extra = menu_extras()
        elif adicionales == 2:
            extra = menu_extra_salsas()
            iterador(extra)
        print("Estos son los ingredientes que puedes agregar: ")
        return extra
    else:
        return extra
def pedido_final():
    pedido = plato_sabor()
    extra = pedido_extra()
    pedido_final = {}
    if any(extra):
        opcion_extra = int(input("Cual deseas agregar: "))
        for k in range(len(extra)):
            if opcion_extra == k:
                suplemento = extra[opcion_extra-1]
        pedido_final[pedido] = suplemento
        for key, value in pedido_final.items():
            print(f"Pediste: {key}, con Extra: {value}")
    else:
            print(f"Su plato es: {pedido}")
def iterador(menu_impresion):
    for i, j in enumerate(menu_impresion,1):
        print(i, j)
def menu_pizzas():
    pizzas = ['Margarita','Napolitana','Roqueford','Tonno','Prosciutto','Funghi','Capricciosa','Roana','Franmy','Quatro Stagioni',
                'Del Padrone','Piamontesa','Vegetal','Pietro','Minano','Quatro Quesos','Speciale','Pazza','Marinera','Picante',
                'Veneciana','Panfli','Brava','Hawaiana','Calzone','Carbonara','Ciao','Serrana','Mediterranea','Barbacoa','Bambino',
                'Mexicana','Cosa Nostra','Antidepresiva']
    return pizzas
def menu_pasta():
    pasta = ['Berenjenas Gratinadas','Lasagna Bolognesa','Tortellini Bolognesa','Tortellini Roquefort','Tortellini Carbonara',
            'Canalones Clasicos','Canalones Carbonara','Macarrones Bolognesa','Macarrones Carbonara','Espaguetis Bolognesa',
            'Espaguetis Carbonara','Espaguetis al Roquefort','Tallarines Carbonara','Tallarines al Roquefort','Ravioli Bolognesa',
            'Ravioli Carbonara','Ravioli al Roquefort']
    return pasta
def menu_ensalada():
    ensaladas = ['Simple','Mixta','Capricciosa','Ciao','Roquefort','Ensalada de Pasta','Tribecca']
    return ensaladas
def menu_extras():
    suplemento_pizza = ['Atún','Anchoa','Aceitunas','Esparragos','Pimiento Verde','Carne Picada','Papas Fritas','Maiz','Mozzarella',
                        'Bacon','Almeja','Alcachofa','Jamón York','Parmesano','Jamón Serrano','Chorizo','Alcaparras','Salami Picante'
                        ,'Huevo','Pimiento Morrón','Pepperoni','Poño','Salsa Barbacoa','Roquefort','Salsa Carbonara',
                        'Piña','Cebolla','Mejillones','Champiñón','Gruyere','Tabasco','Tomate Natural']
    return suplemento_pizza
def menu_extra_salsas():
    salsas = ['Barbacoa','Brava','Roquefort','Mayonesa','Alioli','Rosa','Ketchup', 'Salsa Brava']
    return salsas
def extras():
    extra = str(input("Deseas añadir algun extra a su pedido?: (si/no) "))
    extra = extra.lower()
    if extra == 'si':
        return True
    elif extra == 'no':
        return False
    else:
        print("Escriba una opcion correcta")
def run():
    print("🍕Bienvenido a la pizzeria🍕")
    pedido_final()
if __name__ == "__main__":
    run()
