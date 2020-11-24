from lamp import Lamp
def run():
    lamp = Lamp(is_turned_on = False)
    while True:
        menu = str(input("""
        😁Bienvenido que deseas hacer?😎

            1.- Encender la lampara
            2.- Apagar la lampara
            3.- Salir

            Escribe tu opcion aqui: """))
        if menu == '1':
            lamp.turn_on()
        elif menu == '2':
            lamp.turn_off()
        elif menu == '3':
            print("Haz salido del sistema")
            return False
        else:
            print("Eligue una opcion correcta!")
if __name__ == '__main__':
    run()