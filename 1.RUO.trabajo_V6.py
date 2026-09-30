from abc import ABC, abstractmethod

class Deportista(ABC):
    def __init__(self, nombre, edad, deporte):
        if type(edad) != int:
            raise TypeError("La edad tiene que ser un número")
        if edad <= 0:
            raise ValueError("La edad tiene que ser positiva")
        self.nombre = nombre
        self.edad = edad
        self.deporte = deporte
        self.__puntaje = 0
        self.__cantidad_de_competencias = 0

    @abstractmethod
    def obtener_informacion_basica(self):
        return f"Nombre deportista:: {self.nombre}.\nDeporte que realiza:: {self.deporte}."
    def obtener_estadisticas(self):
        return f"Compretencias participadas:: {self.__cantidad_de_competencias}\nPuntaje total:: {self.__puntaje}"
    def reiniciar_puntaje(self):
        self.__puntaje = 0
        self.__cantidad_de_competencias = 0
    def actualizar_puntaje_y_competencias(self, nuevo_puntaje):
        if type(nuevo_puntaje) != int:
            raise TypeError("El puntaje tiene que ser un número")
        if nuevo_puntaje <= 0:
            raise ValueError("El puntaje tiene que ser positivo")
        self.__puntaje += nuevo_puntaje #suma nuevo_puntaje al puntaje anterior
        self.__cantidad_de_competencias += 1

    #Metodos creados para poder consultar ambos atributos privados
    def obtener_cantidad_de_competencias(self):
        return self.__cantidad_de_competencias
    def obtener_puntaje(self):
        return self.__puntaje

class Futbolista(Deportista):
    def __init__(self, nombre, edad, deporte, equipo, goles, asistencias, posicion):
        super().__init__(nombre, edad, deporte)
        self.equipo = equipo
        self.goles = goles
        self.asistencias = asistencias
        self.posicion = posicion
    def obtener_informacion_basica(self):
        return f"Nombre: {self.nombre}\nDeporte: {self.deporte}\nEquipo: {self.equipo}\nPosición: {self.posicion}"
    def añadir_goles(self, goles):
        self.goles += goles
    def añadir_asistencias(self, asistencias):
        self.asistencias += asistencias
    def calcular_rendimiento(self):
        cantidad = self.obtener_cantidad_de_competencias()
        if cantidad == 0:
            return "El jugador no ha estado en ninguna competencia"
        rendimiento = ((self.goles*2)+(self.asistencias*0.7))/cantidad
        return f"El rendimiento actual del juagador es de:: {rendimiento}"
    def cambiar_de_equipo(self, nuevo_equipo):
        if nuevo_equipo != self.equipo:
            self.equipo = nuevo_equipo



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


test_2 = Futbolista("juanito", 27, "football", "equipo 1", 7, 4, "delantero")

test_2.actualizar_puntaje_y_competencias(30)
test_2.actualizar_puntaje_y_competencias(20)
test_2.actualizar_puntaje_y_competencias(10)



print(test_2.calcular_rendimiento())