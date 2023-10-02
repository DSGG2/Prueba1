from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, tamanio):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.tamanio = tamanio

    def imprimir_caracteristicas(self):
        super().imprimir_caracteristicas()
        print(f"Tamaño: {self.tamanio}")
