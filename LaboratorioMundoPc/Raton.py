from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, tipo_entrada, marca) -> None:
        super().__init__(tipo_entrada, marca)
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
    
    def __str__(self) -> str:
        return f'ID{self._id_raton}: [tipo_entrada: {self.tipo_entrada}, Marca: {self.marca}]'


if __name__ == '__main__':
    raton_1 = Raton('USB', 'Apple')
    print(raton_1)
    raton_2 = Raton('Bluetooth', 'HP')
    print(raton_2)
