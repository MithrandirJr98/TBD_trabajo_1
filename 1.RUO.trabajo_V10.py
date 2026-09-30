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



class Tenista(Deportista):
    def __init__(self, nombre, edad, deporte, pareja, ranking_atp):
        super().__init__(nombre, edad, deporte)
        self.pareja = pareja
        self.ranking_atp = ranking_atp
    def obtener_informacion_basica(self):
        return f"Nombre: {self.nombre}\nDeporte: {self.deporte}\nPareja: {self.pareja}\nRanking ATP: {self.ranking_atp}"
    def actualizar_pareja(self, nueva_pareja):
        self.pareja = nueva_pareja
    def actualizar_ranking(self, nueva_posicion):
        if nueva_posicion >= 0:
            self.ranking_atp = nueva_posicion



class Atleta(Deportista):
    def __init__(self, nombre, edad, deporte, disciplina, mejores_tiempos):
        super().__init__(nombre, edad, deporte)
        self.disciplina = disciplina
        self.mejores_tiempos = mejores_tiempos
    def obtener_informacion_basica(self):
        return f"Nombre: {self.nombre}\nDeporte: {self.deporte}\nDisciplina: {self.disciplina}\nMejores tiempos: {self.mejores_tiempos}"
    def agregar_mejores_tiempos(self, tiempo):
        self.mejores_tiempos.append(tiempo)



class Registro:
    def __init__(self):
        self.deportistas = []
    def añadir_deportista(self, deportista):
        if self.buscar_deportista(deportista.nombre) == None:
            self.deportistas.append(deportista)
    def buscar_deportista(self, nombre):
        for deportista in self.deportistas:
            if deportista.nombre == nombre:
                return deportista
        return None
    def ordenar_deportistas(self, deportistas):
        deportistas_ordenados = []
        for deportista in deportistas:
            posicion = 0
            for deportista_ordenado in deportistas_ordenados:
                if deportista.obtener_puntaje() <= deportista_ordenado.obtener_puntaje():
                    posicion += 1
            deportistas_ordenados.insert(posicion, deportista)
        return deportistas_ordenados
    def mostrar_deportistas(self):
        deportistas_ordenados = self.ordenar_deportistas(self.deportistas)
        for deportista in deportistas_ordenados:
            print(deportista.obtener_informacion_basica())
            print(deportista.obtener_estadisticas())
    def mostrar_ranking_por_deporte(self, deporte):
        deportistas_deporte = []
        for deportista in self.deportistas:
            if deportista.deporte == deporte:
                deportistas_deporte.append(deportista)
        deportistas_deporte = self.ordenar_deportistas(deportistas_deporte)
        for deportista in deportistas_deporte:
            print(deportista.obtener_informacion_basica())
            print(deportista.obtener_estadisticas())
    def mostrar_n_mejores_deportistas(self, deporte, n):
        deportistas_deporte = []
        for deportista in self.deportistas:
            if deportista.deporte == deporte:
                deportistas_deporte.append(deportista)
        deportistas_deporte = self.ordenar_deportistas(deportistas_deporte)
        contador = 0
        for deportista in deportistas_deporte:
            if contador < n:
                print(deportista.obtener_informacion_basica())
                print(deportista.obtener_estadisticas())
                contador += 1


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
print(test_2.obtener_informacion_basica())
print(test_2.calcular_rendimiento())

print(f"{'-'*100}")

test_3 = Tenista("pepito", 25, "tenis", "juanito", 15)
print(test_3.obtener_informacion_basica())
test_3.actualizar_ranking(10)
print(test_3.obtener_informacion_basica())

print(f"{'-'*100}")

test_4 = Atleta("pedrito", 23, "Atletismo", "100 metros", [10.8, 10.6])
print(test_4.obtener_informacion_basica())
test_4.agregar_mejores_tiempos(10.5)
print(test_4.obtener_informacion_basica())

print(f"{'-'*100}")

registro = Registro()
registro.añadir_deportista(test_2)
registro.añadir_deportista(test_3)
registro.añadir_deportista(test_4)
for deportista in registro.deportistas:
    print(f"\n{deportista.obtener_informacion_basica()}\n")