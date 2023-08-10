class personaje:
    nombre = "Davi"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa: ", self.defensa)
        print("Vida: ", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa


if __name__ == '__main__':
    mi_personaje = personaje("And",10,7,5,100)
    mi_personaje.atributos()
    #subo de nivel el personaje
    print(mi_personaje.defensa)
    mi_personaje.subir_nivel(3, 5, 8)
    mi_personaje.atributos()