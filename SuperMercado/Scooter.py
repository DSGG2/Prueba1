from Transporte import Transporte
from Tecnologia import Tecnologia

class Scooter(Transporte, Tecnologia):
    def __init__(self, marca, peso, aro, velocidad, eficiencia,precio):
        Transporte.__init__(self, marca, peso)
        Tecnologia.__init__(self, marca, "", eficiencia, precio)
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso


    def calcular_despacho(self):
        if self.__peso <= 10:
            costo_despacho = 4000 + (300 * self.__peso)
        else:
            costo_despacho = 4000 + (400 * self.__peso)
        return costo_despacho


    def imprimir_caracteristicas(self):
        Transporte.imprimir_caracteristicas(self)  
        descuento = Tecnologia.calcular_descuento(self)  
        costo_despacho = self.calcular_despacho()
        print(f"Aro: {self.__aro}")
        print(f"Velocidad (en km/h): {self.__velocidad}")
        print(f"Costo de despacho: ${costo_despacho:}")
        print(f"Descuento aplicado: {descuento}%")
        precio_final = self.precio - (self.precio * (descuento / 100)) + costo_despacho
        print(f"Precio final con descuento y despacho: ${precio_final:}")



