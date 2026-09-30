from abc import ABC, abstractmethod

class Deportista(ABC):
    def __init__(self, nombre, edad, deporte):
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.__puntaje = 0
        self.__cdc = 0
        #cdc representa el atributo "cantidad_de_competencias"

    def mostrar_info_completa(self): #metodo para testeo
        return f"nombre: {self.nombre}\nedad: {self.edad}\ndeporte: {self.deporte}\npuntaje: {self.__puntaje}\ncdc: {self.__cdc}"

    @abstractmethod
    def obtener_informacion_basica(self):
        return f"Nombre deportista:: {self.nombre}.\nDeporte que realiza:: {self.deporte}."
    def obtener_estadisticas(self):
        return f"Compretencias participadas:: {self.__cdc}\nPuntaje total:: {self.__puntaje}"
    def reiniciar_puntaje(self):
        self.__puntaje = 0
        self.__cdc = 0
    def actualizar_puntaje_y_competencias(self, nuevo_puntaje):
        self.__puntaje += nuevo_puntaje #suma nuevo_puntaje al puntaje anterios, si se quisiera sustituir eliminar l +
        self.__cdc += 1

class Registro(Deportista):
    def __init__(self, nombre, edad, deporte, puntaje, cdc, deportistas):
        super().__init__(nombre, edad, deporte, puntaje, cdc)
        self.deportistas = deportistas
    def añadir_deportista(self, deportista):
        pass
    def mostrar_deportistas(self):
        pass
    def mostrar_ranking_por_deporte(self, deporte):
        pass
    def mostrar_n_mejores_deportistas(self, deporte, n):
        pass
    def buscar_deportista(self, nombre):
        pass

class Competencia(Registro):
    pass
    def __init__(self, nombre, fecha, participantes, resultado, deporte, registro):
        self.nombre = nombre
        self.fecha = fecha
        self.participantes = participantes
        self.resultado = resultado
        self.deporte = deporte
        self.registro = registro
    def inscribir_participante(self, deportista):
        pass
    def registrar_resultado(self, resultado):
        pass
    def mostrar_resultado(self):
        pass
    def mostrar_n_posiciones(self, n):
        pass
    


#---------------testeo de funcionamiento---------------------

#test_1 = Deportista("Kaki", 31, "telas?", 100, 3)

#print(test_1.mostrar_info_completa())