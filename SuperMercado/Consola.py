from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, marca, voltaje, eficiencia, precio, nombre, version):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__nombre = nombre
        self.__version = version

    def calcular_descuento(self):
        descuento_eficiencia = super().calcular_descuento()
        if self.__version.lower() == "pro":
            return descuento_eficiencia + 5
        return descuento_eficiencia

    def imprimir_caracteristicas(self):
        super().imprimir_caracteristicas()
        print(f"Nombre: {self.__nombre}")
        print(f"Versión: {self.__version}")
