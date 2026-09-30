

class Deportista:
    def __init__(self, nombre, edad, deporte, puntaje, cdc):
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.puntaje = puntaje
        self.cdc = cdc
        #cdc representa el atributo "cantidad_de_competencias"
    #def mostrar_info_completa(self): #metodo para testeo
        #return f""
    def obtener_informacion_basica(self):
        return f"Nombre deportista:: {self.nombre}.\nDeporte que realiza:: {self.deporte}."




#---------------testeo de funcionamiento---------------------

test_1 = Deportista("Kaki", 31, "telas?", 100, 3)

print(test_1.obtener_informacion_basica())