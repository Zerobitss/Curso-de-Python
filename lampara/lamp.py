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