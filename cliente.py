

from excepciones import DatoInvalidoError

class Cliente:
    """Representa un cliente con sus datos personales encapsulados."""

    def __init__(self, nombre, documento, correo):
        # Atributos privados, encapsulados (doble guion bajo)
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
    
# Se asignan con los setters para que se validen desde el inicio, si es invalido, se lanzará una excepción 
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_correo(correo)

#Ingreso de nombre, se valida que no esté vacío y que tenga al menos 3 caracteres
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.validar_nombre(nombre)
        self.__nombre = nombre.strip()

    def validar_nombre(self, nombre):
        if not nombre or len(nombre.strip()) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos 3 caracteres")

#Ingreso de documento de identidad, se valida que sea un número y que tenga una longitud mínima y máxima
    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.validar_documento(documento)
        self.__documento = documento

    def validar_documento(self, documento):
        # TODO: ¿solo números? ¿longitud mínima y máxima? ¿no vacío?
        pass

#Ingreso de correo electrónico, se valida que contenga un "@" y un punto después del "@"
    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.validar_correo(correo)
        self.__correo = correo

    def validar_correo(self, correo):
        # TODO: ¿contiene "@"? ¿tiene un punto después del "@"? ¿no vacío?
        pass

    # ---------- MOSTRAR ----------
    def mostrar_datos(self):
        # TODO: imprimir nombre, documento y correo usando los getters
        pass
    
if __name__ == "__main__":
    # Caso válido
    try:
        c = Cliente("Juan Pérez", "123456789", "juan@correo.com")
        print("ok Cliente válido creado:", c.get_nombre())
    except DatoInvalidoError as e:
        print("ERROR - No debería fallar:", e)

    # Caso inválido
    try:
        c2 = Cliente("Al", "123456789", "juan@correo.com")
        print("ERROR - Debió lanzar la excepción")
    except DatoInvalidoError as e:
        print("ok Excepción capturada correctamente:", e)