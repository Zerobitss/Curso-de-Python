#Listas
menu_principal = ['Pizzas','Pasta','Ensaladas']

pizzas = ['Margarita','Napolitana','Roqueford','Tonno','Prosciutto','Funghi','Capricciosa','Romana','Franmy','Quatro Stagioni',
          'Del Padrone','Piamontesa','Vegetal','Pietro','Minano','Quatro Quesos','Speciale','Pazza','Marinera','Picante',
          'Veneciana','Panfli','Brava','Hawaiana','Calzone','Carbonara','Ciao','Serrana','Mediterranea','Barbacoa','Bambino',
          'Mexicana','Cosa Nostra','Antidepresiva']

pasta = ['Berenjenas Gratinadas','Lasagna Bolognesa','Tortellini Bolognesa','Tortellini Roquefort','Tortellini Carbonara',
        'Canalones Clasicos','Canalones Carbonara','Macarrones Bolognesa','Macarrones Carbonara','Espaguetis Bolognesa',
        'Espaguetis Carbonara','Espaguetis al Roquefort','Tallarines Carbonara','Tallarines al Roquefort','Ravioli Bolognesa',
        'Ravioli Carbonara','Ravioli al Roquefort']


ensaladas = ['Simple','Mixta','Capricciosa','Ciao','Roquefort','Ensalada de Pasta','Tribecca']

suplemento_pizza = ['Atún','Anchoa','Aceitunas','Esparragos','Pimiento Verde','Carne Picada','Papas Fritas','Maiz','Mozzarella',
                   'Bacon','Almeja','Alcachofa','Jamón York','Parmesano','Salsa Brava','Jamón Serrano','Chorizo','Alcaparras',
                   'Salami Picante','Huevo','Pimiento Morrón','Pepperoni','Poño','Salsa Barbacoa','Roquefort','Salsa Carbonara',
                   'Piña','Cebolla','Mejillones','Champiñón','Gruyere','Tabasco','Tomate Natural']

salsas = ['Barbacoa','Brava','Roquefort','Mayonesa','Alioli','Rosa','Ketchup']



def presentacion():
    print ("B I E N V E N I D O\n         A\n  P I Z Z E R I A\n    C H A R L Y\n")

def mostrar_menu():
    global opcion_menu
    print ('\nSeleccione la opción del menu:')
    for i in range(len (menu_principal)):
        print (i+1,menu_principal[i])
    opcion_menu = int(input('¿Qué desea comer?\n'))
    print (f'A elegido {(menu_principal[opcion_menu-1])}') ###.format(menu_principal[opcion_menu-1]))

def mostrar_platos():
    global opcion_menu_2
    print ('\nSeleccione la opción del menu:')
    if opcion_menu == 1:
        for i in range(len (pizzas)):
            print (i+1,pizzas[i])
        opcion_menu_2 = int(input('¿Qué Pizza desea comer?\n'))
        print ('A elegido {}.\n'.format(pizzas[opcion_menu_2-1]))
        
    
    if opcion_menu == 2:
        for i in range(len (pasta)):
            print (i+1,pasta[i])
        opcion_menu_2 = int(input('¿Qué Pasta desea comer?\n'))
        print ('A elegido {}.\n'.format(pasta[opcion_menu_2-1]))
        
        
    if opcion_menu == 3:
        for i in range(len (ensaladas)):
            print (i+1,ensaladas[i])
        opcion_menu_2 = int(input('¿Qué Ensalada desea comer?\n'))
        print ('A elegido {}.\n'.format(ensaladas[opcion_menu_2-1]))
              

def mostrar_suplemento():
    global opcion_menu_3
    print ('\nSeleccione la opción del menu:')
    if opcion_menu == 1:
        for i in range(len (suplemento_pizza)):
            print (i+1,suplemento_pizza[i])
        opcion_menu_3 = int(input('¿Qué ingrediente extra quiere?\n'))
        print ('A elegido {} para su pizza.\n'.format(suplemento_pizza[opcion_menu_3-1], pizzas[opcion_menu_2-1]))
# def navagacion (opcion, resultado):
#     if opcion == 1:
#         #vas a hacer cuestion de pizzas o relacion con pizzas o dependiendo del caso de la funcion en que se aplique
    while opcion_menu == 2:
        for i in range(len (salsas)):
            print (i+1,salsas[i])
        opcion_menu_3 = int(input('¿Qué salsa quiere?\n'))
        print ('A elegido {} para su pasta.\n'.format(salsas[opcion_menu_3-1], pasta[opcion_menu_2-1]))
        
    if opcion_menu == 3:
        for i in range(len (salsas)):
            print (i+1,salsas[i])
        opcion_menu_3 = int(input('¿Qué salsa quiere?\n'))
        print ('A elegido {} para su ensalada {}.\n'.format(salsas[opcion_menu_3-1],ensaladas[opcion_menu_2-1] ))   
    mostra_pedido_con()     
    
def mostra_pedido_con():
    if opcion_menu == 1:
        print ('Su pedido es una Pizza {} con {} extra.\n'.format(pizzas[opcion_menu_2-1],suplemento_pizza[opcion_menu_3-1] ))
    
    if opcion_menu == 2:
        print ('Su pedido es una {} con salsa {} extra.\n'.format(pasta[opcion_menu_2-1],salsas[opcion_menu_3-1]))
    
    if opcion_menu == 3:
        print ('Su pedido es una ensala {} con salsa {} extra.\n'.format(ensaladas[opcion_menu_2-1], salsas[opcion_menu_3-1] )) 

def mostra_pedido_sin():
    if opcion_menu == 1:
        print ('Su pedido es una Pizza {}.\n'.format(pizzas[opcion_menu_2-1]))
    
    if opcion_menu == 2:
        print ('Su pedido es {}.\n'.format(pasta[opcion_menu_2-1]))
    
    if opcion_menu == 3:
        print ('Su pedido es una ensala {}.\n'.format(ensaladas[opcion_menu_2-1]))

def quiere_extra():
        
    opcion_quiere = int(input('¿Quiere un ingrediente o salsa extra?\n1 SI\n2 NO\n'))
    
    if opcion_quiere == 1:
        mostrar_suplemento()
    
    else:
        mostra_pedido_sin()             


 
if __name__ == '__main__':
    presentacion()
    mostrar_menu()
    mostrar_platos()
    quiere_extra()