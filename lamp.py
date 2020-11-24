class Lamp:
    #VARIABLE DE CLASE
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
    def __init__(self, is_turned_on):
        self._is_turned_on = False
    def turn_on(self, ):#metodo encendido
        self._is_turned_on = True
        self._display_image()
    def turn_off(self):#metodo apagado
        self._is_turned_on = False
        self._display_image()
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])#Encendido
        else:
            print(self._LAMPS[1])#Apagado
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