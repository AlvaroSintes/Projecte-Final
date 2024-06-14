def pex2():
    # Definimos la clase Contacto
    class Contacto:
        def __init__(self, nombre, telefono, email):
            self.nombre = nombre
            self.telefono = telefono
            self.email = email

        def __str__(self):
            return f'Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}'

    # Definimos la clase Agenda
    class Agenda:
        def __init__(self):
            self.contactos = []

        def agregar_contacto(self, contacto):
            self.contactos.append(contacto)
            print(f'Contacto {contacto.nombre} agregado.')

        def mostrar_contactos(self):
            if not self.contactos:
                print('La agenda está vacía.')
            else:
                for contacto in self.contactos:
                    print(contacto)

        def buscar_contacto(self, nombre):
            for contacto in self.contactos:
                if contacto.nombre.lower() == nombre.lower():
                    return contacto
            return None

        def eliminar_contacto(self, nombre):
            contacto = self.buscar_contacto(nombre)
            if contacto:
                self.contactos.remove(contacto)
                print(f'Contacto {nombre} eliminado.')
            else:
                print(f'Contacto {nombre} no encontrado.')

    # Función principal para interactuar con la agenda
    def main():
        agenda = Agenda()

        while True:
            print("\nAgenda de Contactos")
            print("1. Agregar Contacto")
            print("2. Mostrar Contactos")
            print("3. Buscar Contacto")
            print("4. Eliminar Contacto")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                contacto = Contacto(nombre, telefono, email)
                agenda.agregar_contacto(contacto)
            elif opcion == '2':
                agenda.mostrar_contactos()
            elif opcion == '3':
                nombre = input("Nombre del contacto a buscar: ")
                contacto = agenda.buscar_contacto(nombre)
                if contacto:
                    print(contacto)
                else:
                    print(f'Contacto {nombre} no encontrado.')
            elif opcion == '4':
                nombre = input("Nombre del contacto a eliminar: ")
                agenda.eliminar_contacto(nombre)
            elif opcion == '5':
                print("Saliendo de la agenda.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    # Llamamos a la función main para iniciar el programa
    main()

# Ejecutamos la función pex2


    
