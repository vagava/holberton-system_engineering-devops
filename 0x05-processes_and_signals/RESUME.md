###### (ES)
# Resuemen de la Documentacion

### Comandos:
- `ps`: Informa sobre los procesos actuales activos.

- `pgrep`: Permite encontrar los ID de proceso de un programa en ejecución basados en el nombre y otros atributos.

- `pkill`: funciona de forma idéntica a `pgrep`, excepto que cada proceso que coincide es señalado como si se tratara de kill(1), (envia la señal SIGTERM), en lugar de imprimir su ID de proceso. Se puede especificar un nombre o número de señal como primera opción de línea de comandos para `pkill`.

- `kill`: terminar un proceso. Si no se especifica ninguna señal, se envía la señal TERM.

- `exit`: causar la terminación normal del proceso. Recibe las siguientes constantes EXIT_SUCCESS y EXIT_FAILURE.

- `trap`: Señales de trampa y otros eventos. 
	- *-l*: imprimir una lista de nombres de señales y sus correspondientes números.
	- *-p*: mostrar los comandos trap asociados a cada SIGNAL_SPEC.

### Conceptos:

- **PID**:
Es un numero de identificacion que se asigna automaticamente a acada proceso cuando secrea en el sistema operativo. Cada numero PID es unico, entero, no negativo.
El proceso *init* siempre tendra el mismo PID = 1, ya que siempre es el primer proceso y elantecesor de todos los demas.
Valor maximo permitido para PID  es *32.767*. Este nuemero se puede configurar y dependera de la cantidad de memoria fisica disponible (RAM).

- comandos para encontrar los PID:
	- `ps`.
	- `pstree`.
	- `top`.
	- `pidof`.

- **Linux Processes**:
