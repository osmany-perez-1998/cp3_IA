# HEX

Osmany Pérez Rodríguez C512
Richard García De la Osa C512

### Juego

El juego consiste en un tablero de tablero de tamaño NxN donde cada casilla es representada por un hexágono que almacena el valor $W$,$B$ o  $.$, si en ella hay una ficha blanca, negra o está vacía respectivamente.

Para explorar los posibles estados del juego se utiliza un árbol dirigido que va representando las jugadas que se realizarán a futuro. La raíz es el tablero actual cada vez que se analiza la jugada óptima dada la heurística que se implementa.

### Nodo

Un nodo es un estado del tablero, o sea representa los detalles actuales del juego, tanto el turno del jugador actual como el mapa de las fichas y que a su vez es el analizado por la heurística.

### Arista

La arista representa la jugada realizada. Es el cambio que se lleva a cabo para ir de un estado a otro, que a su vez son los nodos. Estas transiciones están dadas por la inserción de una ficha en una coordenada específica, tanto blanca como negra en dependencia de a que jugador le toca. Además, es necesario recordar que es un grafo dirigido ya que una jugada no se puede deshacer y no hay forma que un nodo ancestro pueda ser igual que el actual.

### Camino

Un camino es una secuencia de estados que están unidos por aristas cuyo inicio es el nodo inicial del juego y el último es un estado final del mismo. Es una serie de moviminetos que concluye con un ganador.

### Jugada

Una jugada es el movimiento que se realiza una vez que se encuentra el movimiento óptimo cuando se analiza los posibles estados del juego en profundidad y a la vez es la hace el cambio de estado en la partida.

### Jugador

El jugador es el encargado del análisis del tablero actual en busca de la jugada que llevará a cabo en su turno. Despúes de cada jugada cambia el turno al otro jugador.

### Heurística

La heurística es básicamente un recorrido de BFS modifcado para analizar ciertas situaciones del juego. 

Analizar el jugador $W$ (blanco) es análogo a analizar el jugador negro teniendo en cuenta que uno tiene como objetivo insertar un camino que lo lleve de izquierda a derecha en el tablero y el otro de arriba hacia abajo.

Sin pérdida de generalidad se analizará el jugador blanco. 

En un inicio se inserta en la cola del BFS las posiciones de las casillas que están en la extrema izquierda del tablero, asociando a las casillas vacías una distancia con valor 1 ya que insertar una ficha en su posición requiere una jugada y con valor 0 aquellas casillas que están ocupadas por el jugador blanco; toma dicho valor porque en la búsqueda de el camino más corto representa un comodín que avanza sin aumentar la distancia del camino.

Una vez iniciado el ciclo del BFS, se extrae el primer elemento de la cola y se analizan aquellos vecinos vacíos o que tienen su propio color; los cuales van a ser insertados antes ya que no representan un aumneto de distancia con respecto a la columna de la extrema izquierda. Todos estos vecinos se guardan como visitados para no ser analizados en múltiples ocasiones. Y regresa al inicio del ciclo para la próxima iteración.

De esta manera se logra encontrar una distancia mínima de un extremo al otro, que se traduce a la cantidad de jugadas como mínimo necesarias para ganar.

La heurística entonces devuelve 1 - (distancia / $n^2$) ya que de esta forma a menor distancia se le otorga mayor valor. Se toma como denominador $n^2$ para asegurar que el valor es menor que 1, dado que no puede haber una distancia mayor que la cantidad de casillas del tablero. Entonces la métrica retorna valores entre 0 y 1.

### Archivo

madeup_minimax.py