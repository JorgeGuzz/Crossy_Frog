# Tarea X: Nombre de la tarea :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Solo se puede entrar o salir de un tronco mediante un salto (funciones moverse y saltar de logica_juego.py)

Caminar hacia un tronco no permite a froggy subirse, pero tampoco lo bota al rio, por lo que sirve para cambiar la direccion a la que froggy esta mirando (linea 213 logica_juego.py)

Las ventanas se diseñaron en QtDesigner y las más grande es de 1600x900 (para mantener la relación 16:9)

Solo se guardan los puntajes al perder (linea 20 logica_post_nivel.py)

Como se explico en una [issue](https://github.com/IIC2233/Syllabus/issues/241), el puntaje se calcula al finalizar el nivel, por lo que el puntaje mostrado en la ventana de juego siempre es 0

Las Calaveras aumentan la velocidad de los proximos troncos que spawneen solo en el nivel actual y su aumento es de 5% sobre el valor al inicio del nivel (linea 105 logica_juego.py)

Como solo se dice que los autos deben atravesar los objetos, pero no se especifica si sus label deben estar por encima o no, se dejó el comportamiento por defecto (el label creado mas recientemente se ve por encima)

Fuente principal de ejemplos fue la [Documentación de modulos Qt para Python](https://doc.qt.io/qtforpython-5/modules.html)

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

- Los posibles spawns de objetos estan divididos por una grilla, al igual que el movimiento de froggy, por lo que si bien los sprites de los objetos parecen estar en cierto lugar su hitbox está en la esquina superior derecha de ese 'cuadrado' de la grilla, lo menciono más que nada por si prueban a cambiarle la velocidad a froggy (de modo que su movimiento dejaria de calzar con esta grilla) podría pasar que atraviese algunos objetos o no recoja alguno que visualmente si tocó. Igualmente mientras no se cambie ese parametro no se tendrian problemas.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventana de Inicio: 4 pts (3%)
##### ❌✅🟠 Ventana de Inicio <explicacion\>
#### Ventana de Ranking: 5 pts (4%)
##### ❌✅🟠 Ventana de Ranking <explicacion\>
#### Ventana de juego: 13 pts (11%)
##### ❌✅🟠 Ventana de juego <explicacion\>
#### Ventana de post-nivel: 5 pts (4%)
##### ❌✅🟠 Ventana post-nivel <explicacion\>
#### Mecánicas de juego: 69 pts (58%)
##### ❌✅🟠 Personaje <explicacion\>
##### ❌✅🟠 Mapa y Áreas de juego <explicacion\>
##### ❌✅🟠 Objetos <explicacion\>
##### ❌✅🟠 Fin de Nivel <explicacion\>
##### ❌✅🟠 Fin del juego <explicacion\>
#### Cheatcodes: 8 pts (7%)
##### ❌✅🟠 Pausa <explicacion\>
##### ❌✅🟠 V + I + D <explicacion\>
##### ❌✅🟠 N + I + V <explicacion\>
#### General: 14 pts (12%)
##### ❌✅🟠 Modularización <explicacion\>
##### ❌✅🟠 Modelación <explicacion\>
##### ❌✅🟠 Archivos  <explicacion\>
##### ❌✅🟠 Parametros.py <explicacion\>
#### Bonus: 10 décimas máximo
##### ❌✅🟠 Ventana de Tienda <explicacion\>
##### ❌✅🟠 Música <explicacion\>
##### ❌✅🟠 Checkpoint <explicacion\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```función() / módulo```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
