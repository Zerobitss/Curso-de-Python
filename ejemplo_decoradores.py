def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        #acciones adicionales que decoraran
        print("Vamos a realizar un calculo: ")
        #ahora llamamos a la funcion parametro para agregar la funcionalidad
        funcion_parametro()
        #acciones adicionales para decorar
        print("Hemos terminado el calculo")
        #ahora debemos retornar la funcion que devuelve la funcion decoradora que es donde se encuentra las acciones en este caso:
    return funcion_interior
#Una vez teniendo el decorador listo ahora lo que necesitamos es especificar en que funcion vamos a colocar el decorador para ello:
@funcion_decoradora #Con esto estamos indicando que al momento de ejecutar suma, le agregamos funcionalidades extras con la funcion decoradora
#la funcion parametro realmente lo que se vuelve a la funcion que queremos decorar en este caso suma asi que dentro del compilador se sustituye
def suma():
    print(15+20)
@funcion_decoradora
def resta():
    print(30-10)
def run():
    suma()
    resta()
if __name__ == '__main__':
    run()