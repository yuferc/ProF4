# reserva.py - Clase Reserva
from cliente import Cliente
from servicio import Servicio
from excepciones import (DatoInvalidoError, ReservaInvalidaError,
                         OperacionNoPermitidaError)

#Crear clase reserva que une un cliente, un servicio y una duración, y controla su estado.
class Reserva:
    
    PENDIENTE = "pendiente"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"
    PROCESADA = "procesada"

    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("La reserva necesita un cliente válido")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("La reserva necesita un servicio válido")
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatoInvalidoError("La duración debe ser un número mayor a 0")

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = self.PENDIENTE
        self._costo_total = None

    def get_estado(self):
        return self._estado

    def confirmar(self):
        if self._estado != self.PENDIENTE:
            raise OperacionNoPermitidaError(
                f"No se puede confirmar una reserva {self._estado}")
        self._estado = self.CONFIRMADA

    def cancelar(self):
        if self._estado in (self.CANCELADA, self.PROCESADA):
            raise OperacionNoPermitidaError(
                f"No se puede cancelar una reserva {self._estado}")
        self._estado = self.CANCELADA

    def procesar(self):
        if self._estado != self.CONFIRMADA:
            raise OperacionNoPermitidaError(
                "Solo se puede procesar una reserva confirmada")
        try:
            costo = self._servicio.calcular_costo(impuesto=0.19)
        except DatoInvalidoError as e:
            raise ReservaInvalidaError(
                "No se pudo calcular el costo de la reserva") from e
        else:
            self._costo_total = costo
            self._estado = self.PROCESADA
            return costo
        finally:
            print("Intento de procesamiento finalizado")

    def mostrar_reserva(self):
        print("----- RESERVA -----")
        print("Cliente :", self._cliente.get_nombre())
        print("Servicio:", self._servicio.describir())
        print("Duración:", self._duracion)
        print("Estado  :", self._estado)
        if self._costo_total is not None:
            print("Costo   :", self._costo_total)


