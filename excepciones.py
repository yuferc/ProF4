class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""
    pass

class DatoInvalidoError(Exception):
    """Se lanza cuando un dato ingresado no es válido."""
    pass

class ReservaInvalidaError(ErrorSoftwareFJ):
    """La reserva se creó con datos incorrectos."""

class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """La operación no es válida para el estado actual de la reserva."""
    