###### (ES)
# Resuemen de la Documentacion

## Comandos:
- `ps`: Informa sobre los procesos actuales activos.

- `pgrep`: Permite encontrar los ID de proceso de un programa en ejecución basados en el nombre y otros atributos.

- `pkill`: funciona de forma idéntica a `pgrep`, excepto que cada proceso que coincide es señalado como si se tratara de kill(1), (envia la señal SIGTERM), en lugar de imprimir su ID de proceso. Se puede especificar un nombre o número de señal como primera opción de línea de comandos para `pkill`.

- `kill`: terminar un proceso. Si no se especifica ninguna señal, se envía la señal TERM.

- `exit`: causar la terminación normal del proceso. Recibe las siguientes constantes EXIT_SUCCESS y EXIT_FAILURE.

- `trap`: Señales de trampa y otros eventos. 
	- *-l*: imprimir una lista de nombres de señales y sus correspondientes números.
	- *-p*: mostrar los comandos trap asociados a cada SIGNAL_SPEC.

## Conceptos:
### Procesos de Linux

El proceso es una instancia de un programa en ejecucion.

El contexto de un programa es la esencia del proceso, este se defien por el programa, el espacio en memoria que ocupa y los procesos hijos que manda a llamar.

los procesos hijos inician siendo una copia exacta del procedo 'padre' para poder llamar al programa o tarea corespondiente, de esta manera el proceso padre (principal) comparte con sus hijos los recursos del sistema que este consumiendo, sus atributos de seguridad (propietario, permisos de archivo, roles, etc).

Programas y procesos con entidades distintas, cuado se ejecuta un programa 3 veces significa que hay 3 instancias del mismo programa, osea 3 procesos distintos. Cada proceso que se inicia es referenciado con su **Process ID (PID)**.

Practicamente todo lo que se esta ejecutando en el sistema en cualquier momento es un proceso, incluyendo la **shell**, el ambiente grafico, el **stack** deprotocolos de red, etc. La excepcion a lo anterior es el **kernel**, el cual es un conjunto de rutinas que residen en la memoria y que, entre otras cosas, administra el planificador que se encarga de controlar los procesos.


### PID
*(Proces ID)*

Es un numero de identificacion que se asigna automaticamente a acada proceso cuando secrea en el sistema operativo. Cada numero PID es unico, entero, no negativo.
El proceso *init* siempre tendra el mismo PID = 1, ya que siempre es el primer proceso y elantecesor de todos los demas.
Valor maximo permitido para PID  es *32.767*. Este nuemero se puede configurar y dependera de la cantidad de memoria fisica disponible (RAM).

- comandos para encontrar los PID:
	- `ps`.
	- `pstree`.
	- `top`.
	- `pidof`.

### Señales de linux

Las señales son interrupciones de software.

En linux las señales empiezan con los caracteres SIG.
- Ejemplo:
	- SIGINT:Señal que se genera cuando se preciona ctrl+c desde la terminal.
	- SIGABRT: Señal que se genera cuando se llama a la funcion abnorto.

- #### Manejo de señales
Cuando ocurre una señal, el proceso debe deirle al kernel que hacer con ella, exixten tres opciones:

1. *Ignorar*: No hacer nada cuando ocurra la señal. La mayoria de señales se pueden ignorar excepto, señales como SIGKILL y SIGSTOP (estas señales no se pueden captar ni ignorar).

2. *Captar*: capturar la señal y realizar una accion especifica con una funcion, si la señal no es fatal, la funcion puede manejar la cuncion correctamente.

3. Dejar que se aplique la opcion predeterminada.





