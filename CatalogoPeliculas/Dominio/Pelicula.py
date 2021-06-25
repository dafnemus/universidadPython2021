class Pelicula:
    def __init__(self, titulo) -> None:
        self.titulo = titulo
    
    def __str__(self) -> str:
        return f'Pelicula: {self.titulo}'
