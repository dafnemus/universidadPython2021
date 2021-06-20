from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, tipo_entrada, marca) -> None:
        super().__init__(tipo_entrada, marca)
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
    
    def __str__(self) -> str:
        return f'ID{self._id_teclado}: [tipo_entrada: {self.tipo_entrada}, Marca: {self.marca}]'


if __name__ == '__main__':
    teclado_1 = Teclado('USB', 'Apple')
    print(teclado_1)
    teclado_2 = Teclado('Bluetooth', 'HP')
    print(teclado_2)
