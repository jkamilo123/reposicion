class TransporteUrbano:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def presentar_informacion(self):
        print(f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}\n")


bicicleta = TransporteUrbano("Bicicleta", "Shimano", "XTR")
carro= TransporteUrbano("Carro", "Toyota", "Corolla")
transmilenio = TransporteUrbano("Transmilenio", "Holap", "K280 UB 6x2")

bicicleta.presentar_informacion()
carro.presentar_informacion()
transmilenio.presentar_informacion()
