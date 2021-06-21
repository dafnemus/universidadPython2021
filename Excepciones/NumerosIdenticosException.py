class NumerosIdenticosException(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
        
