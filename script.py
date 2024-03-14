import json  # Importar el módulo json para trabajar con datos JSON

class Usuario():
    """
    Clase que representa un usuario con nombre, apellido, email y género.
    """
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        """
        Inicializa una instancia de Usuario con los atributos proporcionados.

        Args:
            nombre (str): Nombre del usuario.
            apellido (str): Apellido del usuario.
            email (str): Dirección de correo electrónico del usuario.
            genero (str): Género del usuario.
        """
        self.nombre = nombre  # Asignar el nombre del usuario
        self.apellido = apellido  # Asignar el apellido del usuario
        self.email = email  # Asignar el email del usuario
        self.genero = genero  # Asignar el género del usuario

usuarios_data = []  # Lista para almacenar las instancias de Usuario creadas con éxito

with open('usuarios.txt', 'r') as file:
    # Iterar sobre cada línea del archivo usuarios.txt, usando enumerate para obtener el número de línea
    for line_num, line in enumerate(file, start=1):
        try:
            usuario_json = json.loads(line)  # Convertir la línea JSON en un diccionario Python
            # Crear una instancia de Usuario con los datos del diccionario y agregarla a la lista de usuarios
            usuario = Usuario(usuario_json['nombre'], usuario_json['apellido'], usuario_json['email'], usuario_json['genero'])
            usuarios_data.append(usuario)
        except Exception as e:  # Capturar cualquier excepción
            with open('error.log', 'a') as error_file:  # Abrir el archivo error.log en modo de apéndice
                # Escribir información sobre el error en el archivo error.log
                error_file.write(f"Error en la línea {line_num}: {str(e)}\n")

print("Instancias de Usuario creadas exitosamente.")  # Mensaje de confirmación
