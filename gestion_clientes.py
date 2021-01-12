"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que
la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo,
preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una
opción del siguiente menú:

(1) Añadir cliente,
(2) Eliminar cliente,
(3) Mostrar cliente,
(4) Listar todos los clientes
(5) Listar clientes preferentes
(6) Terminar.

En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""
#NIF sera la llave del cliente
#El valor del cliente sera una tupla, nombre direccion, telefono, correo
#Valor true a clientes preferente
def navagacion(opcion):
    pass
def run():
    clientes = {}#Diccionario de datos
    opcion = int(input("Escribe tu opcion: "))#Variable de opcion para navegar entre el menu de los while
    while opcion == 1:
        print("Haz elegido la opcion (1.- Añadir cliente)\n")
        nif = str(input("Ingresa el NIF del cliente, en este caso este sera su ID dentro de la empresa: "))
        nombre = str(input("Ingresa el nombre del cliente: "))
        direccion = str(input("Ingresa la direccion del cliente: "))
        telefono = str(input("Ingresa el telefono del cliente: "))
        correo = str(input("Ingresa el correo del cliente: "))
        preferente = str(input("Es un cliente preferente? (y/n): "))
        if preferente == "y":
            preferente = True
        elif preferente == "n":
            preferente = False
        else:
            print("Escribe una opcion correcta (y/n)")
        opcion(opcion)
        datos_cliente = {
        'nombre': nombre,
        'dirección': direccion,
        'teléfono': telefono,
        'email': correo,
        'preferente': preferente}
        for i in clientes.values(): #ciclo for para imprimir los NIF del diccionario clientes
            print(f"El NIF: ({i}) del cliente ha sido agregado exitosamente\n")
        for j, k in datos_cliente.items():#ciclo for con dos iteraciones para imprimir las llaves y sus valores
            print(f"Sus datos {j} : {k} . Han sido agregados exitosamente\n")
        clientes[nif] = datos_cliente #Asignamos la variable nif como llave y datos_clientes como los valores
        opcion = str(input("Deseas agregar a otro cliente? (y/n): "))#Reinicio del ciclo while, este caso lo veras mucho ya que con el te preguntara de nuevo a donde quieres ir
        if opcion == "y":
            opcion = 1
        elif opcion == "n":
            opcion = int(input("Que deseas hacer ahora?: "))
        else:
            print("Escribe una opcion correcta") #Mensaje de error
    while opcion == 2:
        if any(clientes): #Funcion quep pregunta si existen valores dentro del diccionario, tambien lo veras mucho
            print("Haz elegido la opcion (2.- Eliminar cliente)\n")
            eliminar = str(input("Ingresa el NIF del cliente que vas a eliminar: ")) #Variable para eliminar NIF
            if eliminar in clientes.keys(): #Pregunta si eliminar existe dentro de las llaves del diccionario
                del(clientes[eliminar])#Si existe se utiliza del para eliminar la llave del diccionario y la posicion va a ser igual a eliminar para eliminar la correcta introducida anteriormente
                print(f"El cliente por el NIF {eliminar} ha sido eliminado exitosamente")
                opcion = str(input("Deseas eliminar otro cliente? (y/n): "))#Reinicio del ciclo while
                if opcion == "y":
                    opcion = 2
                elif opcion == "n":
                    opcion = int(input("Que deseas hacer ahora?: "))
            else:
                print(f"El numero de NIF {eliminar} no existe en la base de datos") #Error al escribir el NIF mal
        else:
            print("Actualmente no existen clientes registrados")
            opcion = int(input("Que deseas hacer ahora?: "))
    while opcion == 3:
        #if any(clientes):
            print("Haz eligido la opcion (3.- Mostrar cliente)\n")
            idcliente = str(input("Ingresa el NIF del cliente que desas buscar: ")) #id cliente va a ser igual al nif del cliente
            if idcliente in clientes.keys(): # si id cliente existe dentro de las llaves del diccionario
                print(f"Haz buscado el NIF: {idcliente}") #Imprimir
                for key, value in clientes[idcliente].items(): #Ciclo for con doble iterador añadiendo la llave idcliente como parametro, por que? por que de esta forma al ser el mismo idcliente == nif, vamos a imprimir los valores correctos y no todo el diccionario
                    print(f"{key} : {value}") #Impresion del nif y valores
                opcion = str(input("Deseas buscar otro cliente? (y/n): ")) #Reinicio del ciclo while
                if opcion == "y":
                    opcion = 3
                elif opcion == "n":
                    opcion = int(input("Que deseas hacer ahora?: "))
            else:
                print(f"No se encontro el NIF: {idcliente}")
        #else:
            print("Actualmente no existen clientes registrados")
            opcion = int(input("Que deseas hacer ahora?: "))
    while opcion == 4:
        print("Haz elegido la opcion (4.- Listar todos los clientes) \n")
        for i, j in clientes.items(): #Ciclo for con dos iteradores para recorrer las llaves y valores
            print(f"Su NIF: {i}, {j['nombre']}") #el iterador i sera igual a la llave y j iterara solamente entre los valores de la llave ['nombre']
        opcion = str(input("Que deseas hacer ahora?: ")) #Reinicio del ciclo while
    while opcion == 5:
        print("Haz elegido la opcion (5.- Listar todos los clientes preferentes)\n")
        for key, value in clientes.items(): #Ciclo for con dos iteradores para recorrer llaves y valores
            if value['preferente']: #si el valor preferente == True, entonces solo imprimira a los clientes preferentes anteriormente declarados
                print(f"Su NIF: {key}, Su Nombre: {value['nombre']}")#Imprimir la llave y el valor del ['nombre']
        opcion = str(input("Que deseas hacer ahora?: ")) #Reinicio del while
    while opcion == 6:
        print("Haz elegido la opcion (6.- Terminar)")
        print("Muchas gracias por utilizar el sistema, esperamos verte pronto!") #Esta opcion es simplemente un mensaje de despedida
        return False
if __name__ == "__main__":
    print("""
    🐱‍💻Bienvenido a la gestion de bases de datos de tu empresa 🐱‍👤

    (1) Añadir cliente,
    (2) Eliminar cliente,
    (3) Mostrar cliente,
    (4) Listar todos los clientes
    (5) Listar clientes preferentes
    (6) Terminar
    """)
    run()