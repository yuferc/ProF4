

# servicio.py - Servicios de Software FJ
from abc import ABC, abstractmethod
from excepciones import DatoInvalidoError   # si aún no existe, usa ValueError


#  clase abstracta Servicio

class Servicio(ABC):
    """Plantilla general para todos los servicios de Software FJ."""

    def __init__(self, nombre, precio_base):
        if not nombre or not str(nombre).strip():
            raise DatoInvalidoError("El nombre del servicio no puede estar vacío")
        if not isinstance(precio_base, (int, float)) or precio_base <= 0:
            raise DatoInvalidoError("El precio base debe ser un número mayor a 0")
        self._nombre = nombre.strip()
        self._precio_base = precio_base
        
    #Metodos necesarios

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        """Calcula el costo. Impuesto y descuento son opcionales (0 a 1)."""
        pass

    @abstractmethod
    def describir(self):
        """Devuelve un texto que describe el servicio."""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida los datos propios de cada servicio."""
        pass

    def _aplicar_ajustes(self, costo, impuesto, descuento):
        """Método de apoyo: aplica descuento e impuesto a un costo base."""
        if not (0 <= descuento <= 1) or not (0 <= impuesto <= 1):
            raise DatoInvalidoError("Impuesto y descuento deben estar entre 0 y 1")
        costo = costo - (costo * descuento)
        costo = costo + (costo * impuesto)
        return costo


#  ReservaSala

class ReservaSala(Servicio):
    """Servicio de reserva de salas, cobrado por horas."""

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)
        self._horas = horas
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self._horas, (int, float)) or self._horas <= 0:
            raise DatoInvalidoError("Las horas deben ser un número mayor a 0")

    def calcular_costo(self, impuesto=0, descuento=0):
        costo = self._precio_base * self._horas
        return self._aplicar_ajustes(costo, impuesto, descuento)

    def describir(self):
        return f"Reserva de sala '{self._nombre}' por {self._horas} hora(s)"



#  AlquilerEquipo

class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos, cobrado por días."""

    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)
        self._dias = dias
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self._dias, int) or self._dias <= 0:
            raise DatoInvalidoError("Los días deben ser un número entero mayor a 0")

    def calcular_costo(self, impuesto=0, descuento=0):
        costo = self._precio_base * self._dias
        return self._aplicar_ajustes(costo, impuesto, descuento)

    def describir(self):
        return f"Alquiler del equipo '{self._nombre}' por {self._dias} día(s)"


#  AsesoriaEspecializada

class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría, cobrado por horas con recargo según el nivel."""

    RECARGOS = {"junior": 1.0, "senior": 1.5, "experto": 2.0}

    def __init__(self, nombre, precio_base, horas, nivel):
        super().__init__(nombre, precio_base)
        self._horas = horas
        self._nivel = str(nivel).lower().strip()
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self._horas, (int, float)) or self._horas <= 0:
            raise DatoInvalidoError("Las horas deben ser un número mayor a 0")
        if self._nivel not in self.RECARGOS:
            raise DatoInvalidoError(
                f"Nivel inválido. Opciones: {', '.join(self.RECARGOS)}"
            )

    def calcular_costo(self, impuesto=0, descuento=0):
        costo = self._precio_base * self._horas * self.RECARGOS[self._nivel]
        return self._aplicar_ajustes(costo, impuesto, descuento)

    def describir(self):
        return (f"Asesoría '{self._nombre}' nivel {self._nivel} "
                f"por {self._horas} hora(s)")


