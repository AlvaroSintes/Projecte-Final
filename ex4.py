def pex4():
    # Classe base per als materials de la biblioteca
    class MaterialBiblioteca:
        def __init__(self, titol, autor, any_publicacio):
            self.titol = titol
            self.autor = autor
            self.any_publicacio = any_publicacio

        def mostrar_informacio(self):
            return f"Títol: {self.titol}, Autor: {self.autor}, Any de publicació: {self.any_publicacio}"

    # Subclasse per als llibres
    class Llibre(MaterialBiblioteca):
        def __init__(self, titol, autor, any_publicacio, nombre_pagines):
            super().__init__(titol, autor, any_publicacio)
            self.nombre_pagines = nombre_pagines

        def mostrar_informacio(self):
            info_basica = super().mostrar_informacio()
            return f"{info_basica}, Nombre de pàgines: {self.nombre_pagines}"

    # Subclasse per a les revistes
    class Revista(MaterialBiblioteca):
        def __init__(self, titol, autor, any_publicacio, numero_edicio):
            super().__init__(titol, autor, any_publicacio)
            self.numero_edicio = numero_edicio

        def mostrar_informacio(self):
            info_basica = super().mostrar_informacio()
            return f"{info_basica}, Número d'edició: {self.numero_edicio}"

    # Subclasse per als diaris
    class Diari(MaterialBiblioteca):
        def __init__(self, titol, autor, any_publicacio, data):
            super().__init__(titol, autor, any_publicacio)
            self.data = data

        def mostrar_informacio(self):
            info_basica = super().mostrar_informacio()
            return f"{info_basica}, Data: {self.data}"

    # Funció per mostrar la informació dels materials de la biblioteca
    def mostrar_informacio_materials(materials):
        for material in materials:
            print(material.mostrar_informacio())

    # Crear alguns exemples de materials
    llibre1 = Llibre("El Quixot", "Miguel de Cervantes", 1605, 1000)
    revista1 = Revista("National Geographic", "Diversos", 2023, 2)
    diari1 = Diari("Marca", "Diversos", 2024, "10 de juny")

    # Llistar els materials en una llista
    materials_biblioteca = [llibre1, revista1, diari1]

    # Mostrar la informació dels materials
    mostrar_informacio_materials(materials_biblioteca)

