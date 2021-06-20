class Monitor():
    contador_monitores = 0
    def __init__(self, marca, tamaño) -> None:
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamaño = tamaño
    
    @property
    def marca(self):
        return self._marca

    @property
    def tamaño(self):
        return self._tamaño

    def __str__(self) -> str:
        return f'ID{self._id_monitor}: [Tamaño: {self.tamaño}, Marca: {self.marca}]'


if __name__ == '__main__':
    monitor_1 = Monitor('Bangho', 16)
    print(monitor_1)
    monitor_2 = Monitor('Lenovo', 16)
    print(monitor_2)
