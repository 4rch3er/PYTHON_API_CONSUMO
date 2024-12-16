# Importamos la clase AnimeAPI que contiene los métodos para interactuar con la API de animes
from anime_api import AnimeAPI

# Función para mostrar el menú principal
def menu_principal(api):
    while True:
        # Muestra el menú principal con las opciones disponibles
        print("\nMenú Principal:")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        
        # Solicita al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        # Si la opción es "1", intenta iniciar sesión con el nombre de usuario y la contraseña
        if opcion == "1":
            username = input("Ingrese el nombre de usuario: ")
            password = input("Ingrese la contraseña: ")
            if api.login(username, password):  # Si el inicio de sesión es exitoso, se accede al menú de la API
                menu_api(api)
                break
        # Si la opción es "2", registra un nuevo usuario
        elif opcion == "2":
            username = input("Ingrese el nombre de usuario: ")
            email = input("Ingrese su correo: ")
            password = input("Ingrese la contraseña: ")
            api.create_user(username, email, password)  # Crea un nuevo usuario en la API
        # Si la opción es "3", sale del programa
        elif opcion == "3":
            break
        else:
            # Si la opción no es válida, se muestra un mensaje de error
            print("Opción no válida. Intente nuevamente.")

# Función para mostrar el menú de la API, donde se gestionan los animes
def menu_api(api):
    while True:
        print("\nMenú API:")
        print("1. Ver todos los animes")
        print("2. Crear nuevo anime")
        print("3. Actualizar anime")
        print("4. Eliminar anime")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        # Si la opción es "1", muestra la lista de todos los animes
        if opcion == "1":
            api.list_animes()
        # Si la opción es "2", solicita la información de un nuevo anime y lo crea
        elif opcion == "2":
            titulo = input("Ingrese el título del anime: ")
            tipo_anime = input("Ingrese el tipo de anime: ")
            episodios = int(input("Ingrese el número de episodios: "))
            url = input("Ingrese la URL del anime: ")
            fecha = input("Ingrese la fecha de estreno (YYYY-MM-DD): ")
            estado = input("Ingrese el estado del anime: ")
            generos = input("Ingrese los géneros (separados por coma): ")
            sinopsis = input("Ingrese la sinopsis del anime: ")

            anime_data = {  # Crea un diccionario con los datos del nuevo anime
                "titulo": titulo,
                "tipo_anime": tipo_anime,
                "episodios": episodios,
                "url": url,
                "fecha": fecha,
                "estado": estado,
                "generos": generos,
                "sinopsis": sinopsis
            }
            api.create_anime(anime_data)  # Llama al método para crear el anime en la API
        # Si la opción es "3", permite actualizar un anime existente
        elif opcion == "3":
            anime_id = input("Ingrese el ID del anime a actualizar: ")
            titulo = input("Nuevo título: ")
            tipo_anime = input("Nuevo tipo de anime: ")
            episodios = int(input("Nuevo número de episodios: "))
            url = input("Nueva URL: ")
            fecha = input("Nueva fecha de estreno (YYYY-MM-DD): ")
            estado = input("Nuevo estado del anime: ")
            generos = input("Nuevos géneros (separados por coma): ")
            sinopsis = input("Nueva sinopsis: ")

            anime_data = {  # Crea un diccionario con los nuevos datos del anime
                "titulo": titulo,
                "tipo_anime": tipo_anime,
                "episodios": episodios,
                "url": url,
                "fecha": fecha,
                "estado": estado,
                "generos": generos,
                "sinopsis": sinopsis
            }
            api.update_anime(anime_id, anime_data)  # Llama al método para actualizar el anime en la API
        # Si la opción es "4", permite eliminar un anime
        elif opcion == "4":
            anime_id = input("Ingrese el ID del anime a eliminar: ")
            api.delete_anime(anime_id)  # Llama al método para eliminar el anime en la API
        # Si la opción es "5", sale del menú
        elif opcion == "5":
            break
        else:
            # Si la opción no es válida, se muestra un mensaje de error
            print("Opción no válida. Intente nuevamente.")


