from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, marca, peso, aro, precio):
        super().__init__(marca, peso)
        self.__aro = aro
        self.precio = precio  

    def calcular_despacho(self):
        peso_despacho = self.peso * 400
        return Transporte.COSTO_DESPACHO_BASE + peso_despacho

    def imprimir_caracteristicas(self):
        super().imprimir_caracteristicas()
        print(f"Aro: {self.__aro}")
        costo_despacho = self.calcular_despacho()
        print(f"Costo de despacho: ${costo_despacho:}")
        print(f"Precio: ${self.precio:}")  

