

class Deportista:
    def __init__(self, nombre, edad, deporte, puntaje, cdc):
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.puntaje = puntaje
        self.cdc = cdc
        #cdc representa el atributo "cantidad_de_competencias"

    def mostrar_info_completa(self): #metodo para testeo
        return f"nombre:    {self.nombre}\nedad:   {self.edad}\ndeporte:    {self.deporte}\npuntaje:    {self.puntaje}\ncdc:   {self.cdc}"
    
    def obtener_informacion_basica(self):
        return f"Nombre deportista::    {self.nombre}.\nDeporte que realiza::  {self.deporte}."
    def obtener_estadisticas(self):
        return f"Compretencias participadas::   {self.cdc}\nPuntaje total::    {self.puntaje}"
    def reiniciar_puntaje(self):
        self.puntaje = 0
        self.cdc = 0
    def actualizar_puntaje_y_competencias(self, nuevo_puntaje):
        self.puntaje = nuevo_puntaje
        self.cdc += self.cdc



#---------------testeo de funcionamiento---------------------

test_1 = Deportista("Kaki", 31, "telas?", 100, 3)

print(test_1.mostrar_info_completa())