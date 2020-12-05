"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
a continuación.

* Ingredientes vegetarianos: Pimiento y tofu.
* Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.


Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con
los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
def run():
    adicional_pizza = 0
    eleccion = ""
    pimenton = 0
    tofu = 0
    peperoni = 0
    jamon = 0
    salmon = 0
    while True:
        menu = int(input("""
    Bienvenido a la pizzeria bella napoli ofrecemos pizzas vegetarinas y pizzas no vegetarianas

    1.- Pizzas vegetarinas
    2.- Pizzas no vegetarinas

    Que deseas pedir?: """))
        if menu == 1:
            menu_vegetariano = int(input("""
        Excelente opcion haz elegido el menu vegetariano, nuestros ingredientes disponibles son:
            1.- Pimenton
            2.- Tofu

            Cual deseas?: """))
            if menu_vegetariano == 1:
                print("Deacuerdo haz escogido primenton en tu pizza")
                pimenton += 1
                menu_vegetariano = int(input("""Deseas agregar un adicional?
                1.- Si
                2.- No deseo terminar la compra

                Escribe tu opcion: """))
                if menu_vegetariano == 1:
                    menu_vegetariano = int(input("""
                    1.- Adicional de pimento
                    2.- Adicional de tofu

                    Cual prefieres: """))
                    if menu_vegetariano == 1:
                        pimenton += 1
                        adicional_pizza += 1
                        print("Perfecto haz agregado un adicional de pimenton")
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {pimenton}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_vegetariano == 2:
                        print("Perfecto haz agregado un adicional de tofu")
                        tofu += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {pimenton} y de tofu {tofu}")
                        print("Enseguida preparamos su pedido!")
                        break
                elif menu_vegetariano == 2:
                    if (pimenton >= 1):
                        eleccion = "Pizza de pimenton"
                        print(eleccion)
                    elif (tofu >= 1):
                        eleccion = "Pizza de tofu"
                    print(f"Ok enseguida preparamos su {eleccion}")
                    break
            elif menu_vegetariano == 2:
                print("Deacuerdo haz escodigo tofu en tu pizza")
                tofu += 1
                menu_vegetariano = int(input("""Deseas agregar un adicional?
                1.- Si
                2.- No deseo terminar la compra

                Escribe tu opcion: """))
                if menu_vegetariano == 1:
                    menu_vegetariano = int(input("""
                    1.- Adicional de pimento
                    2.- Adicional de tofu

                    Cual prefieres: """))
                    if menu_vegetariano == 1:
                        pimenton += 1
                        adicional_pizza += 1
                        print("Perfecto haz agregado un adicional de pimenton")
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {pimenton} y tofu {tofu}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_vegetariano == 2:
                        print("Perfecto haz agregado un adicional de tofu")
                        tofu += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {pimenton} y de tofu {tofu}")
                        print("Enseguida preparamos su pedido!")
                        break
                elif menu_vegetariano == 2:
                    if (pimenton >= 1):
                        eleccion = "Pizza de pimenton"
                        print(eleccion)
                    elif (tofu >= 1):
                        eleccion = "Pizza de tofu"
                    print(f"Ok enseguida preparamos su {eleccion}")
                    break

        if menu == 2:
            menu_no_vegetariano = int(input("""
            Excelente opcion haz elegido el menu no vegetariano, nuestros ingredientes disponibles son:
            1.- Peperoni
            2.- Jamon
            3.- Salmon
            Cual deseas?: """))
            if menu_no_vegetariano == 1:
                print("Deacuerdo haz escogido primenton en tu pizza")
                peperoni += 1
                menu_no_vegetariano = int(input("""Deseas agregar un adicional?
                1.- Si
                2.- No deseo terminar la compra

                Escribe tu opcion: """))
                if menu_no_vegetariano == 1:
                    menu_no_vegetariano = int(input("""
                    1.- Adicional de peperoni
                    2.- Adicional de Jamon
                    3.- Adicional de Salmon

                    Cual prefieres: """))
                    if menu_no_vegetariano == 1:
                        peperoni += 1
                        adicional_pizza += 1
                        print("Perfecto haz agregado un adicional de Peperoni")
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_no_vegetariano == 2:
                        print("Perfecto haz agregado un adicional de Jamon")
                        jamon += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni} y de tofu {jamon}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_no_vegetariano == 3:
                        print("Perfecto haz agregado un adicional de Salmon")
                        salmon += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni} y de tofu {jamon}, y de {salmon}")
                        print("Enseguida preparamos su pedido!")
                        break
                elif menu_no_vegetariano == 2:
                    if (peperoni >= 1):
                        eleccion = "Pizza de de peperoni"
                        print(eleccion)
                    elif (jamon >= 1):
                        eleccion = "Pizza de jamon"
                    elif (salmon >= 1):
                        eleccion = "Pizza de salmon"
                    print(f"Ok enseguida preparamos su {eleccion}")
                    break

            if menu_no_vegetariano == 2:
                print("Deacuerdo haz escogido una pizza de jamon")
                jamon+= 1
                menu_no_vegetariano = int(input("""Deseas agregar un adicional?
                1.- Si
                2.- No deseo terminar la compra

                Escribe tu opcion: """))
                if menu_no_vegetariano == 1:
                    menu_no_vegetariano = int(input("""
                    1.- Adicional de peperoni
                    2.- Adicional de Jamon
                    3.- Adicional de Salmon

                    Cual prefieres: """))
                    if menu_no_vegetariano == 1:
                        peperoni += 1
                        adicional_pizza += 1
                        print("Perfecto haz agregado un adicional de Peperoni")
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_no_vegetariano == 2:
                        print("Perfecto haz agregado un adicional de Jamon")
                        jamon += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni} y de tofu {jamon}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_no_vegetariano == 3:
                        print("Perfecto haz agregado un adicional de Salmon")
                        salmon += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni} y de tofu {jamon}, y de {salmon}")
                        print("Enseguida preparamos su pedido!")
                        break
                elif menu_no_vegetariano == 2:
                    if (peperoni >= 1):
                        eleccion = "Pizza de de peperoni"
                        print(eleccion)
                    elif (jamon >= 1):
                        eleccion = "Pizza de jamon"
                    elif (salmon >= 1):
                        eleccion = "Pizza de salmon"
                    print(f"Ok enseguida preparamos su {eleccion}")
                    break
            if menu_no_vegetariano == 3:
                print("Perfecto haz escogido una pizza de salmon")
                salmon += 1
                menu_no_vegetariano = int(input("""Deseas agregar un adicional?
                1.- Si
                2.- No deseo terminar la compra

                Escribe tu opcion: """))
                if menu_no_vegetariano == 1:
                    menu_no_vegetariano = int(input("""
                    1.- Adicional de peperoni
                    2.- Adicional de Jamon
                    3.- Adicional de Salmon

                    Cual prefieres: """))
                    if menu_no_vegetariano == 1:
                        peperoni += 1
                        adicional_pizza += 1
                        print("Perfecto haz agregado un adicional de Peperoni")
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_no_vegetariano == 2:
                        print("Perfecto haz agregado un adicional de Jamon")
                        jamon += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni} y de tofu {jamon}")
                        print("Enseguida preparamos su pedido!")
                        break
                    elif menu_no_vegetariano == 3:
                        print("Perfecto haz agregado un adicional de Salmon")
                        salmon += 1
                        adicional_pizza += 1
                        print(f"Su pedido tiene una cantidad de adicionales ({adicional_pizza}) las porciones de: {peperoni} y de tofu {jamon}, y de {salmon}")
                        print("Enseguida preparamos su pedido!")
                        break
                elif menu_no_vegetariano == 2:
                    if (peperoni >= 1):
                        eleccion = "Pizza de de peperoni"
                        print(eleccion)
                    elif (jamon >= 1):
                        eleccion = "Pizza de jamon"
                    elif (salmon >= 1):
                        eleccion = "Pizza de salmon"
                    print(f"Ok enseguida preparamos su {eleccion}")
                    break
if __name__ == '__main__':
    run()