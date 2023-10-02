class Transporte:
    COSTO_DESPACHO_BASE = 4000

    def __init__(self, marca, peso):
        self.marca = marca
        self.peso = peso

    def calcular_despacho(self):
        return Transporte.COSTO_DESPACHO_BASE
    
    def imprimir_caracteristicas(self):
        print(f"Marca: {self.marca}")
        print(f"Peso (en kg): {self.peso}")
