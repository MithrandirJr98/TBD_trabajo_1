Aquí irán escritas las referencias y demás

- V1
testeo rápido metodo obtener_informacion_basica() clase Deportista

- V2
se completaron los metodos restantes en clase Deportista

- V3
self.cdc += self.cdc cambió a self.cdc += 1
ya que el resultado de esa operación se duplicaba busqué la solución con IA y me corrigió ese mal uso de +=.
también se declaró como abstracta la clase Deportista
referencia: "https://youtu.be/jmFtLwIAWws?si=yoqysX82dgzg-3QH"
finalmente se agregaron las clases (no funcionales) Registro y Competencia

- V4
corrección de sintaxis, cambio de @abstractmethod del __init__ a obtener_informacion_basica() debido a que no se estaba utilizando correctamente.
también se privatizaron e inicializaron en 0 las declaraciones de los atributos puntaje y cdc. Al ser inicializados dentro de __init__ ya no se reciben como argumentos.

- V5
se cambió el nombre de cdc por cantidad_de_competencias y se implementó una comprobación para que la edad y nuevo_puntaje sean números enteros positivos    (La versión 5 del trabajo por un descuido no fue guardada mientras se hicieron los cambios para la versión 6 así que esta es solo una copia de la versión 6. Pero los cambios fueron (vistos desde la versión 6) las lineas 5-8 y 24-27).
Se decidió seguir trabajando con las clases heredadas de Deportista antes de empezar con las otras dos clases, aún así como no molestan se dejarán ahí

- V6
Se creó la clase Futbolista que hereda de la clase padre Deportista. Al haber dejado los atributos de puntaje y cantidad_de_competencias en Deportista como privados ya no puedo llamarlos directamente en Futbolista por lo que hubo que crear dos métodos (uno para cada atributo) extra que retornan el atributo en si, de modo que así puedo llamarlos (sin modificarlos) Este error fue solucionado por la IA, que mencionó que se estaba haciendo "name mangling" cuando intentaba acceder normalmente al atributo cantidad_de_competencias. Finalmente se le asignaron valores a la función abstracta "obtener_informacion_basica()".

- V7
Se hicieron las clases hijas Tenista y Atleta heredadas de Deportista que son prácticamente copias más "sencillas" de Futbolista y ambas con su respectivo método abstracto "obtener_informacion_basica()" que está modificado para el contexto de cada clase. Algo a mencionar es como se agregó el nuevo tiempo a la lista mejores_tiempos, con el uso de append se agrega directamente al final del arreglo sin hacer ningún tipo de filtro, lo mismo con la diciplina, quizá se analice mejor luego.

- V8
Se comenzó a trabajar realmente en la clase Registro, primero se quitó la herencia de Deportista ya que un Registro no es un tipo de Deportista y se dejó como atributo solamente la lista deportistas. Esta lista comienza vacía (selr.deportistas = []) y con añadir_deportista() se agregan los objetos de las clases hijas de Deportista usando append. tambien para testear se añadieron registros de los objeos hechos previamente y se imprimieron por terminal.
También se implementó buscar_deportista(), este recorre con un for todos los objetos guardados en la lista deportistas y compara el nombre de cada uno con el nombre que se está buscando. Si encuentra una coincidencia retorna el objeto deportista completo y si termina de recorrer la lista sin encontrarlo retorna None.

- V9
Se continuó trabajando en la clase Registro, primero se modificó añadir_deportista() para evitar que se puedan agregar deportistas repetidos, para esto se reutiliza buscar_deportista() y solamente se agrega el objeto cuando este método retorna None. También se implementó mostrar_deportistas() que recorre con un for la lista e imprime la información de todos los deportistas registrados.
Finalmente se comenzó mostrar_ranking_por_deporte(), este también recorre la lista pero utiliza un if para comparar el deporte de cada objeto con el deporte ingresado y solamente imprime los que coincidan. Por ahora este método solamente filtra por deporte y todavía no ordena a los deportistas por puntaje, eso se hará en la siguiente versión.

- V10
Se terminó la clase Registro implementando el ordenamiento de los deportistas según su puntaje. Para esto se creó el método extra ordenar_deportistas(), este crea una nueva lista y recorre los deportistas comparando sus puntajes, luego con insert() agrega cada objeto en la posición que corresponda para que queden ordenados de mayor a menor. este ordenamiento se utilizó en mostrar_deportistas() y mostrar_ranking_por_deporte().
Finalmente se implementó mostrar_n_mejores_deportistas(), que primero filtra a los deportistas según el deporte, los ordena y luego utiliza un contador para imprimir solamente los primeros n deportistas.

- V11
Se comenzó a trabajar en la clase Competencia, primero se quitó la herencia de Registro ya que una competencia no es un tipo de registro, en cambio se agregó registro como atributo para poder utilizar desde la competencia los deportistas que ya están registrados. También se cambió participantes para que comience como una lista vacía y se creó resultados como un diccionario vacío.
Se implementó inscribir_participante(), este recibe el nombre de un deportista y utiliza buscar_deportista() del objeto registro para buscarlo. Si el deportista existe se comprueba que su deporte sea el mismo de la competencia y finalmente se agrega el objeto a la lista participantes.

- V12
Se continuó con Competencia implementando registrar_resultado(), este recorre la lista participantes buscando por nombre al deportista y cuando lo encuentra guarda en el diccionario resultados el objeto deportista junto al puntaje que obtuvo. Después se utiliza actualizar_puntaje_y_competencias() para que el resultado de la competencia también actualice el puntaje total y la cantidad de competencias del mismo deportista.
igual se implementó mostrar_resultado(), este recorre los objetos que están guardados en el diccionario resultados e imprime el nombre de cada deportista junto al puntaje que obtuvo en esta competencia.

- V13
Se terminó la funcionalidad principal de Competencia implementando mostrar_n_posiciones(). Para esto se crea una lista resultados_ordenados y se recorren los deportistas que tienen resultados registrados. Se compara el puntaje de cada deportista con los que ya fueron agregados a la nueva lista y con insert() se coloca el objeto en la posición correspondiente para que los resultados queden ordenados de mayor a menor.
Finalmente se utiliza un contador para recorrer los resultados ordenados e imprimir solamente las primeras n posiciones, mostrando la posición, nombre del deportista y el puntaje que obtuvo en la competencia.

- V14
Se hizo un testeo más completo del funcionamiento de las clases juntas, descartando el anterior. Para esto se crearon varios objetos de Futbolista, Tenista y Atleta y se agregaron todos al mismo objeto Registro. Luego se creó una competencia de football utilizando este registro y se inscribieron tres futbolistas que ya estaban registrados. se registraron distintos resultados para los tres participntes y se probaron mostrar_resultado() y mostrar_n_posiciones() para comprobar que los resultados se guardaran y ordenaran correctamente. Finalmente se volvió a mostrar el ranking de football desde Registro para comprobar que registrar los resultados de la competencia también actualizara el puntaje y cantidad de competencias de los objetos originales.
Con esto se comprobó el funcionamiento en conjunto de Deportista y sus clases hijas, Registro y Competencia antes de comenzar con las correcciones y validaciones finales. Pd: se agregó un f-string a las lineas 121 y122 para mejor entendimiento de la respuesta del terminal

- V15 Correcciones finales
Junto con la IA se realizó una revisión final de las clases y se corrigieron varios detalles que habían quedado pendientes durante el desarrollo. Primero se modificaron las clases Futbolista, Tenista y Atleta para que el deporte se establezca automáticamente desde cada clase y ya no sea necesario entregarlo como argumento al crear los objetos.
En Futbolista se agregaron validaciones para que añadir_goles() y añadir_asistencias() solamente reciban números enteros positivos. También se modificó cambiar_de_equipo() para que al cambiar el equipo se utilice reiniciar_puntaje() y se reinicien el puntaje y la cantidad de competencias. En Tenista se agregó la validación del ranking y se modificó actualizar_pareja() para reiniciar el puntaje cuando se cambia de pareja, para esto se agregó en Deportista el método reiniciar_solo_puntaje() ya que reiniciar_puntaje() también reinicia la cantidad de competencias. En Atleta se agregó una validación para comprobar que los nuevos tiempos sean números positivos antes de agregarlos a mejores_tiempos.
Finalmente se hicieron correcciones en Competencia. inscribir_participante() ahora comprueba que el deportista no se encuentre anteriormente en participantes antes de agregarlo y registrar_resultado() comprueba que el puntaje sea un entero positivo y que el deportista no tenga un resultado registrado anteriormente, evitando que una misma competencia pueda aumentar más de una vez su puntaje y cantidad de competencias.
También se modificó la creación de los objetos utilizados en el testeo ya que ahora el deporte es establecido automáticamente por las clases hijas.