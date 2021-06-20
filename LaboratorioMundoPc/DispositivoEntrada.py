class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca) -> None:
        self._tipo_entrada = tipo_entrada
        self._marca = marca
    
    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, otro):
        self._tipo_entrada = otro

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, otra):
        self._marca = otra

if __name__ == '__main__':
    dispositivo_1 = DispositivoEntrada('Ratón', 'Apple')
    print(dispositivo_1.marca)
    print(dispositivo_1.tipo_entrada)
