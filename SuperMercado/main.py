from Tecnologia import Tecnologia
from Transporte import Transporte
from Tv import Tv
from Consola import Consola
from Scooter import Scooter
from Bicicleta import Bicicleta

tvs = []
consolas = []
scooters = []
bicicletas = []

def menu():
    opcion = ""
    while opcion != '6':
        print("Menú:")
        print("1. Registrar TV")
        print("2. Registrar Consola")
        print("3. Registrar Scooter")
        print("4. Registrar Bicicleta")
        print("5. Cotizar producto")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            registrar_tv()
        elif opcion == '2':
            registrar_consola()
        elif opcion == '3':
            registrar_scooter()
        elif opcion == '4':
            registrar_bicicleta()
        elif opcion == '5':
            cotizar_producto()
        elif opcion == '6':
            print("Saliendo")
        else:
            print("Por favor seleccione una opcion valida")

def cotizar_producto():
    tipo_producto = input("Ingrese el producto a cotizar (TV, Consola, Scooter, Bicicleta): ")

    if tipo_producto.lower() == 'tv':
        cotizar_tv()
    elif tipo_producto.lower() == 'consola':
        cotizar_consola()
    elif tipo_producto.lower() == 'scooter':
        cotizar_scooter()
    elif tipo_producto.lower() == 'bicicleta':
        cotizar_bicicleta()
    else:
        print("Por favor ingrese un tipo válido.")

def cotizar_tv():
    if not tvs:
        print("No hay TVs registradas.")
        return

    print("Seleccione una TV para cotizar:")
    for a, tv in enumerate(tvs):
        print(f"{a + 1}. Marca: {tv.marca}, Precio: ${tv.precio:}")

    respuesta = input("Ingrese el número de la TV que desea cotizar: ")

    try:
        respuesta = int(respuesta)
        if 1 <= respuesta <= len(tvs):
            tv = tvs[respuesta - 1]
            tv.imprimir_caracteristicas()
            descuento = tv.calcular_descuento()
            precio_final = tv.precio - (tv.precio * (descuento / 100))
            print(f"Descuento aplicado: {descuento}%")
            print(f"Precio final con descuento: ${precio_final:}")
        else:
            print("Seleccion no valida")
    except :
        print("Ingrese un numero")

def cotizar_consola():
    if not consolas:
        print("No hay Consolas registradas.")
        return

    print("Seleccione una Consola para cotizar:")
    for a, consola in enumerate(consolas):
        print(f"{a + 1}. Marca: {consola.marca}, Precio: ${consola.precio:}")

    respuesta = input("Ingrese el número de la Consola que desea cotizar: ")

    try:
        respuesta = int(respuesta)
        if 1 <= respuesta <= len(consolas):
            consola = consolas[respuesta - 1]
            consola.imprimir_caracteristicas()
            descuento = consola.calcular_descuento()
            precio_final = consola.precio - (consola.precio * (descuento / 100))
            print(f"Descuento aplicado: {descuento}%")
            print(f"Precio final con descuento: ${precio_final:}")
        else:
            print("Seleccion no valida")
    except :
        print("Ingrese un numero")

def cotizar_scooter():
    if not scooters:
        print("No hay Scooters registrados")
        return

    print("Seleccione un Scooter para cotizar:")
    for a, scooter in enumerate(scooters):
        print(f"{a + 1}. Marca: {scooter.marca}, Peso: {scooter.peso} kg, Precio: ${scooter.precio:}")

    respuesta = input("Ingrese el número del Scooter que desea cotizar: ")

    try:
        respuesta = int(respuesta)
        if 1 <= respuesta <= len(scooters):
            scooter = scooters[respuesta - 1]
            scooter.imprimir_caracteristicas()
            costo_despacho = scooter.calcular_despacho()
            descuento = Tecnologia.calcular_descuento(scooter)
            precio_final = scooter.precio - (scooter.precio * (descuento / 100)) + costo_despacho
        else:
            print("Seleccion no valida")
    except :
        print("Ingrese un número")

def cotizar_bicicleta():
    if not bicicletas:
        print("No hay Bicicletas registradas.")
        return

    print("Seleccione una Bicicleta para cotizar:")
    for a, bicicleta in enumerate(bicicletas):
        print(f"{a + 1}. Marca: {bicicleta.marca}, Peso: {bicicleta.peso} kg, Precio: {bicicleta.precio} $")

    respuesta = input("Ingrese el número de la Bicicleta que desea cotizar: ")

    try:
        respuesta = int(respuesta)
        if 1 <= respuesta <= len(bicicletas):
            bicicleta = bicicletas[respuesta - 1]
            bicicleta.imprimir_caracteristicas()
            costo_despacho = bicicleta.calcular_despacho()
            precio_final = bicicleta.precio + costo_despacho 
            print(f"Precio final (con despacho): ${precio_final:}")
        else:
            print("Seleccion no valida")
    except :
        print("Ingrese un numero")


def registrar_tv():
    marca = input("Marca: ")
    voltaje = input("Voltaje: ")
    eficiencia = input("Eficiencia (a,b,c,d,e,f): ").lower()
    precio = float(input("Precio: $"))
    tamanio = input("Tamaño: ")

    tv = Tv(marca, voltaje, eficiencia, precio, tamanio)
    tvs.append(tv)

    print("TV registrada con éxito.")

def registrar_consola():
    marca = input("Marca: ")
    voltaje = input("Voltaje: ")
    eficiencia = input("Eficiencia (a,b,c,d,e,f): ").lower()
    precio = float(input("Precio: $"))
    nombre = input("Nombre de la Consola: ")
    version = input("Version (Pro o normal): ")
    consola = Consola(marca, voltaje, eficiencia, precio, nombre, version)
    consolas.append(consola)
    print("Consola registrada con exito.")

def registrar_scooter():
    marca = input("Marca: ")
    peso = float(input("Peso (en kg): "))
    aro = int(input("Aro: "))
    velocidad = int(input("Velocidad (en km/h): "))
    eficiencia = input("Eficiencia (a,b,c,d,e,f): ").lower()
    precio = float(input("Precio: $"))
    scooter = Scooter(marca, peso, aro, velocidad, eficiencia, precio)
    scooters.append(scooter)
    print("Scooter registrado con exito.")

def registrar_bicicleta():
    marca = input("Marca: ")
    peso = float(input("Peso (en kg): "))
    aro = int(input("Aro: "))
    precio = float(input("Precio: $"))
    bicicleta = Bicicleta(marca, peso, aro, precio)  
    bicicletas.append(bicicleta)
    print("Bicicleta registrada con exito.")

menu()
