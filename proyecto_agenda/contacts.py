import csv
class Contact:#Contenedor de variables ingresadas
    def __init__(self,name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
class ContactBook:
    def __init__(self):
        self._contacts = []#Lista vacia donde se guardaran los contactos
    def add (self, name, phone, email):#Metodo de guardar contactos
        contact = Contact(name,phone,email) #instancia para almacenar contactos
        self._contacts.append(contact) #Ingresar contactos a la lista
        self._save()
    def show_all(self):#Metodo para imprimir contactos
        for contact in self._contacts:
            self._print_contact(contact)#Metodo para imprimir contacto
    def _print_contact(self, contact):#Creacion de metodo que imprime contactos
        print('---* ---* ---* ---* ---* ---* ---* ')
        print(f'Nombre: {contact.name}')
        print(f'Telefono: {contact.phone}')
        print(f'Email: {contact.email}')
        print('---* ---* ---* ---* ---* ---* ---*')
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):#Agregar indice a la lista de contactos
            if contact.name.lower() == name.lower():#Colocar los nombres en minusculas
                del self._contacts[idx]#Eliminar contacto deacuerdo al indice
                print("Se ha eliminado satisfactoriamente el usuario")
                self._save() #Guardar nueva lista de contacto luego de eliminar un contacto
                break #Fin del ciclo
    def update(self, name):
        for idx, contact in enumerate(self._contacts): #Doble iterador uno para verificar el nombre contacto otro para el indice de la lista
            update = str(input("Ingrese nombre de contacto a cambiar: "))
            if update == name:
                contact.name = str(input('Ingrese un nuevo nombre: '))
                contact.phone = str(input('Ingrese un nuevo telefono: '))
                contact.email = str(input('Ingrese un nuevo email: '))
                self._contacts[idx] = contact
                self._save()
                break
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email')) #Identificador de colomnas
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))#Escribir
    def search (self, name):
        for contact in self._contacts: #Iteracion en lista de contactos
            if contact.name.lower() == name.lower(): #Comparacion en minusculas para evitar errores
                self._print_contact(contact) #Imprimir nombre
                break
        else:
                self._not_found()
    def _not_found(self):
        print('---* ---* ---* ---* ---* ---* ---*')
        print("El usuario no fue encontrado")
        print('---* ---* ---* ---* ---* ---* ---*')
def run():
    contact_book = ContactBook()#Creacion de instancia
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            elif len(row) == 0:
                continue
            contact_book.add(row[0],row[1],row[2])
    while True:
        command = str(input('''
            ¿Qué deseas hacer?
            1.- añadir contacto
            2.- actualizar contacto
            3.- buscar contacto
            4.- eliminar contacto
            5.- listar contactos
            6.- salir

            Ingresa tu opcion: '''))
        if command == '1':
            print('añadir contacto')
            name = str(input("Escribe el nombre del contacto: "))
            phone = str(input("Telefono celular del contacto: "))
            email = str(input("Escribe el email del contacto: "))
            contact_book.add(name, phone, email)
        elif command == '2':
            print('actualizar contacto')
            contact_book.update(name)
        elif command == '3':
            print('buscar contacto')
            name = str(input("Escribe el nombre del contacto a buscar: "))
            contact_book.search(name)
        elif command == '4':
            print('eliminar contacto')
            name = str(input("Escribe el nombre del contacto a eliminar: "))
            contact_book.delete(name)
        elif command == '5':
            print('listar contactos')
            contact_book.show_all()
        elif command == '6':
            return False
        else:
            print('Comando no encontrado.')
if __name__ == '__main__':
    print('🤖Bienvenid@ a la agenda Platzi👾')
    run()