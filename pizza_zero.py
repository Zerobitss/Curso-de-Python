def menu():
    menu_principal = ['Pizzas','Pasta','Ensaladas','Parilla']
    menu_eleccion = [menu_pizzas(), menu_pasta(), menu_ensalada()]
    opcion_menu = int(input("1.-Pizzas\n2.-Pasta\n3.-Ensaladas\nQue deseas comer hoy: "))
    pedido = {}
    try:
        if (opcion_menu < len(menu_principal)) and (opcion_menu > 0):
            print(f"Tu eleccion fue: {menu_principal[opcion_menu-1]}")
            iterador(menu_eleccion[opcion_menu-1])
            menu_eleccion = menu_eleccion[opcion_menu-1]
            plato = menu_principal[opcion_menu-1]
            opcion_plato = int(input("Que deseas pedir: "))
            for j in range(len(menu_eleccion)):
                if opcion_menu == j:
                    print(f"Pediste una {plato}, {menu_eleccion[opcion_plato-1]}")
            sabor = menu_eleccion[opcion_plato-1]
            adicional = extras()
            if adicional is True:
                adicionales = int(input("\n1.-Aperitivos\n2.-Salsas\nQue deseas agregar: "))
                if adicionales == 1:
                    extra = menu_extras()
                elif adicionales == 2:
                    extra = menu_extra_salsas()
                print("Estos son los ingredientes que puedes agregar: ")
                iterador(extra)
                opcion_extra = int(input("Cual deseas agregar: "))
                plato = plato +", " +sabor
                for k in range(len(extra)):
                    if opcion_extra == k:
                        pedido[plato] = extra[opcion_extra-1]
                for key, value in pedido.items():
                    print(f"Pediste: {key}, con Extra: {value}")
                    print("gracias por venir")
            else:
                pedido = {plato: sabor}
                for key, value in pedido.items():
                    print(f"Su plato es: ({key}) de ({value})")
            return pedido
    except Exception as opcion_menu:
        print(type(opcion_menu).__name__)
        print(f"Su opcion no se encuentra dentro de nuestro menu, porfavor eligue una correcta")
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
    menu()
if __name__ == "__main__":
    run()
