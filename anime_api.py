import requests
from prettytable import PrettyTable

class AnimeAPI:
    # URLs para los endpoints de la API
    BASE_URL = "http://localhost:8000/api/animes/"  # Endpoint para acceder a los animes
    LOGIN_URL = "http://localhost:8000/api/token/"  # Endpoint para obtener el token JWT
    REGISTER_URL = "http://localhost:8000/api/register/"  # Endpoint para registrar un nuevo usuario

    def __init__(self):
        self.token = None  # Variable para almacenar el token de autenticación
        self.username = None  # Variable para almacenar el nombre de usuario del usuario logueado

    def login(self, username, password):
        """Obtiene el JWT usando las credenciales del usuario."""
        # Datos de inicio de sesión del usuario
        data = {
            "username": username,
            "password": password
        }
        # Realizamos la solicitud POST al endpoint de login
        response = requests.post(self.LOGIN_URL, data=data)
        self.handle_response(response)  # Llamada para manejar la respuesta de la API

        # Si la respuesta es exitosa (HTTP 200), guardamos el token y mostramos un mensaje de bienvenida
        if response.status_code == 200:
            self.token = response.json()['access']  # Guardamos el token recibido
            self.username = username  # Guardamos el nombre de usuario
            print(f"\nBienvenido {self.username}!")  # Mensaje de bienvenida
            return True
        # Si las credenciales son incorrectas (HTTP 401), mostramos un mensaje de error
        elif response.status_code == 401:
            print("Error: Credenciales inválidas. Por favor, intente de nuevo.")
        return False

    def create_user(self, username, email, password):
        """Crea un nuevo usuario utilizando el endpoint de registro de la API."""
        # Datos del nuevo usuario
        data = {
            "username": username,
            "email"   : email,
            "password": password
        }
        # Realizamos la solicitud POST para crear el usuario
        response = requests.post(self.REGISTER_URL, data=data)
        self.handle_response(response)  # Llamada para manejar la respuesta de la API

        # Si la creación fue exitosa (HTTP 201), mostramos un mensaje de éxito
        if response.status_code == 201:
            print("Usuario creado exitosamente.")
        # Si hubo un error en los datos proporcionados (HTTP 400), mostramos un mensaje de error
        elif response.status_code == 400:
            print("Error: Datos de usuario inválidos. El nombre de usuario puede existir.")
        return False

    def get_headers(self):
        """Obtiene los encabezados con el token de autorización."""
        # Si hay un token de autenticación, lo añadimos al encabezado
        if self.token:
            return {"Authorization": f"Bearer {self.token}"}
        return {}

    def list_animes(self):
        """Obtiene y muestra todos los animes en formato de tabla."""
        headers = self.get_headers()  # Obtener los encabezados con el token
        response = requests.get(self.BASE_URL, headers=headers)  # Realizamos la solicitud GET para obtener los animes
        self.handle_response(response)  # Llamada para manejar la respuesta de la API

        # Si la respuesta es exitosa (HTTP 200), mostramos los animes en formato de tabla
        if response.status_code == 200:
            animes = response.json()  # Convertimos la respuesta en formato JSON
            if animes:
                # Creamos una tabla con PrettyTable para visualizar los animes
                table = PrettyTable()
                table.field_names = ["ID", "Título", "Tipo", "Episodios", "Fecha", "Estado", "Géneros", "Sinopsis"]

                for anime in animes:
                    # Agregamos cada anime a la tabla
                    table.add_row([anime["id"], anime["titulo"], anime["tipo_anime"], anime["episodios"], anime["fecha"], anime["estado"], anime["generos"], anime["sinopsis"]])

                print("\nLista de Animes:")  # Título de la tabla
                print(table)  # Imprimir la tabla
            else:
                print("No hay animes en la base de datos.")  # Si no hay animes en la respuesta
        return False

    def create_anime(self, anime_data):
        """Crea un nuevo anime en la base de datos."""
        headers = self.get_headers()  # Obtener los encabezados con el token
        response = requests.post(self.BASE_URL, headers=headers, data=anime_data)  # Realizamos la solicitud POST para crear el anime
        self.handle_response(response)  # Llamada para manejar la respuesta de la API

        # Si la creación fue exitosa (HTTP 201), mostramos un mensaje de éxito
        if response.status_code == 201:
            print(f"Anime creado exitosamente: {response.json()}")
        return False

    def update_anime(self, anime_id, anime_data):
        """Actualiza un anime existente."""
        headers = self.get_headers()  # Obtener los encabezados con el token
        # Realizamos la solicitud PUT para actualizar un anime
        response = requests.put(f"{self.BASE_URL}{anime_id}/", headers=headers, data=anime_data)
        self.handle_response(response)  # Llamada para manejar la respuesta de la API

        # Si la actualización fue exitosa (HTTP 200), mostramos un mensaje de éxito
        if response.status_code == 200:
            print(f"Anime actualizado exitosamente: {response.json()}")
        return False

    def delete_anime(self, anime_id):
        """Elimina un anime de la base de datos."""
        headers = self.get_headers()  # Obtener los encabezados con el token
        # Realizamos la solicitud DELETE para eliminar un anime
        response = requests.delete(f"{self.BASE_URL}{anime_id}/", headers=headers)
        self.handle_response(response)  # Llamada para manejar la respuesta de la API

        # Si la eliminación fue exitosa (HTTP 204), mostramos un mensaje de éxito
        if response.status_code == 204:
            print(f"Anime con ID {anime_id} eliminado exitosamente.")
        return False

    def handle_response(self, response):
        """Maneja la respuesta de la API y muestra el código de estado y el mensaje."""
        # Imprimir el código de estado HTTP
        print(f"Código de estado HTTP: {response.status_code}")
        
        # Mostrar un mensaje según el código de estado HTTP de la respuesta
        if response.status_code == 200:
            print("Operación exitosa.")
        elif response.status_code == 400:
            print("Error: Solicitud incorrecta.")
        elif response.status_code == 401:
            print("Error: No autorizado. Credenciales inválidas o sesión expirada.")
        elif response.status_code == 404:
            print("Error: No encontrado. El recurso solicitado no existe.")
        elif response.status_code == 403:
            print("Error: Prohibido. No tiene permiso para realizar esta operación.")
        elif response.status_code >= 500 and response.status_code < 600:
            print("Error del servidor. Por favor, intente más tarde.")
        else:
            print("")
