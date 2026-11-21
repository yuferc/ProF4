# logger_config.py - Registro de eventos y errores
import logging
import os

CARPETA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
RUTA_LOG = os.path.join(CARPETA, "sistema.log")
_logger = None


def configurar_logger():
    """Crea la carpeta y el archivo de logs (solo la primera vez)."""
    global _logger
    if _logger is not None:
        return _logger

    os.makedirs(CARPETA, exist_ok=True)
    _logger = logging.getLogger("software_fj")
    _logger.setLevel(logging.INFO)

    if not _logger.handlers:
        manejador = logging.FileHandler(RUTA_LOG, encoding="utf-8")
        manejador.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        _logger.addHandler(manejador)
    return _logger


def registrar_evento(mensaje):
    configurar_logger().info(mensaje)


def registrar_error(mensaje):
    configurar_logger().error(mensaje)