import csv
class Vehiculo:
    
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
####################################################################################################
    def guardar_datos_csv(self):
        try:
            with open('vehiculos.csv', 'a', newline='') as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    @staticmethod
    def leer_datos_csv():
        try:
            vehiculos = {
                "Particular": [],
                "Carga": [],
                "Bicicleta": [],
                "Motocicleta": []
            }
            
            with open('vehiculos.csv', 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                for vehiculo in archivo_csv:
                    # Identificar el tipo de vehículo por la clase
                    tipo = vehiculo[0].split('.')[-1].replace("'>","")
                    # Convertir el string del diccionario a diccionario real
                    datos = eval(vehiculo[1])
                    if tipo in vehiculos:
                        vehiculos[tipo].append(datos)
            
            # Imprimir los vehículos por tipo
            for tipo, lista in vehiculos.items():
                if lista:
                    print(f"\nLista de Vehiculos {tipo}")
                    for vehiculo in lista:
                        print(vehiculo)
                        
        except FileNotFoundError:
            print("El archivo vehiculos.csv no existe.")
        except Exception as e:
            print(f"Error al leer datos: {e}")

####################################################################################################

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Velocidad {self.velocidad} Km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puestos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos
        
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Velocidad {self.velocidad} Km/h, {self.cilindrada} cc, Puestos: {self.numero_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Velocidad {self.velocidad} Km/h, {self.cilindrada} cc, Carga: {self.carga}Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, Tipo: {self.tipo}, Motor: {self.motor}T, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios} "

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2,"Carrera") 
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", 2, "Doble Viga", 21)

particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()

print(particular)
print(carga)
print(bicicleta)
print(motocicleta)

print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))
# Crear una instancia y imprimir
v1 = Automovil("Toyota", "Yaris", 4, 120, 800)
# print(v1)
######

######
def main():
    automoviles = []
    
    n = int(input("Cuantos Vehiculos desea insertar: "))
    
    for i in range(n):
        print(f"\nDatos del automóvil {i+1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        num_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        
        auto = Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)
        automoviles.append(auto)
    
    # Mostrar los automóviles ingresados
    print("Automóviles ingresados:")
    for i, auto in enumerate(automoviles, 1):
        print(f"Automóvil {i}: {auto}")

if __name__ == "__main__":
    main()





