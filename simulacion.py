# simulacion.py - Simulación de operaciones de Software FJ
from cliente import Cliente
from servicio import ReservaSala
from reserva import Reserva
from excepciones import ErrorSoftwareFJ
from logger_config import registrar_evento, registrar_error


def operacion_1():
    """Reserva exitosa: cliente válido + sala + confirmar + procesar."""
    cliente = Cliente("Ana Pérez", "12345678", "ana@correo.com")
    servicio = ReservaSala("Sala A", 50000, 2)
    reserva = Reserva(cliente, servicio, 2)
    reserva.confirmar()
    costo = reserva.procesar()
    reserva.mostrar_reserva()
    registrar_evento(f"Reserva de {cliente.get_nombre()} procesada. Costo: {costo}")


def ejecutar(numero, descripcion, operacion):
    """Ejecuta una operación sin que un error detenga el programa."""
    print(f"\n=== Operación {numero}: {descripcion} ===")
    try:
        operacion()
    except ErrorSoftwareFJ as e:
        print(f"Error controlado: {type(e).__name__} - {e}")
        registrar_error(f"Operación {numero}: {type(e).__name__} - {e}")
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__} - {e}")
        registrar_error(f"Operación {numero}: error inesperado {type(e).__name__} - {e}")
    else:
        registrar_evento(f"Operación {numero} completada")
    finally:
        print(f"Fin de la operación {numero}")


def ejecutar_simulaciones():
    ejecutar(1, "Reserva de sala exitosa", operacion_1)


if __name__ == "__main__":
    ejecutar_simulaciones()