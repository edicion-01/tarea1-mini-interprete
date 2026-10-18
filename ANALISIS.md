# Análisis — Tarea 1

**Integrantes:**
1. Mendoza Aragón Edith Alejandra
2. Mondragón Ceballos Evelyn Vianey
3.

**Fork:** https://github.com/edicion-01/tarea1-mini-interprete
**Rama:** main

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | La expresion numérica que buscamos interpretar | Devuelve la expresion tokenizada, con los tokens en una lista (en el orden que se leyo), es decir, categoriza todo en su respectivo tipo (numero, mas, menos, etc) | De tokenizar la expresion |
| `parser` | La expresion ya tokenizada (es decir, la lista con los tokens) | Un AST (mediante nodos) con la jerarquia correcta | De que podamos interpretar a la expresion con la jerarquia correcta (que le es indicada), es el encargado del analisis sintatico (construye el ast) |
| `ast` | Los valores que componen los nodos futuros (en teoria, numeros y operaciones) | Los nodos que componen a AST | Forma los nodos del ast |
| `evaluator` | Los nodos del ast (la expresion separada individualmente por nodos) | La expresion interpretada (resultado) | De evaluar y devolver las expresiones numericas |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | `"Token(PAR_IZQ, (, 0)", "Token(NUMERO, 3, 1)", "Token(MAS, +, 3)", "Token(NUMERO, 4, 5)", Token(PAR_DER, ), 6)", Token(POR, *, 8)", Token(NUMERO, 2, 10) `  |
| AST | <br> `OperacionBinaria(*)` <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`│---Izquierda: OperacionBinaria(+)` <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`│`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`│---Izquierda: 3` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`│`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`│---Derecha: 4` <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`│---Derecha: 2`  |
| resultado | `14` |

> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| test_suma | evaluator | Suma entre dos numeros naturales | 1 | normal |
| test_resta | evaluator | Resta entre dos numeros naturales, donde el primer termino es mayor que el numero que se resta | 1 | normal |
| test_multiplicacion | evaluator | La multiplicacion entre dos numeros naturales | 1 | normal |
| test_division | evaluator | La division entre dos numeros naturales, donde el numerador es mayor que el denominador | 1 | normal |
| test_precedencia_sin_parentesis | evaluator | Que la jeraquia de operaciones se cumpla entre 3 numeros naturales sin la necesidad un parentesis (en este caso, que se cumpla que primero va la multiplicaion, despues la suma) | 2 | normal |
| test_precedencia_con_parentesis | evaluator | Que la jeraquia de operaciones se cumpla entre 3 numeros naturales cuando incluimos parentesis (en este caso, prioritizar el parentesis sobre la multiplicacion) | 2 | normal |
| test_tokeniza_un_numero_solo | lexer | Que la entrada con un solo numero natural sea bien tokenizada | 0 | frontera |
| test_tokeniza_una_suma | lexer | Que la entrada con una suma entre dos numeros naturales sea bien tokenizada | 1 | normal |
| test_los_espacios_no_producen_tokens | lexer | Que los espacios en una entrada, ya sea al inicio, entre elementos, al final o consecutivos, sea ignorado/no influyan la tokenizacion | 1 | normal y frontera |
| test_tokeniza_parentesis | lexer | Que los parentesis que contienen una expresion valida sean bien tokenizados | 0 | normal |
| test_construye_el_arbol_de_una_suma | parser | Que el arbol resultante de una suma de dos numeros naturales sea correcto | 1 | normal |
| test_la_multiplicacion_se_agrupa_antes_que_la_suma | parser | Que el arbol resultante de una operacion con suma y multiplicacion, que inicialmente no lleva parentesis, agrupe correctamente las operaciones (priorizando la multiplicacion), y el arbol muestre correctamente dicha jerarquia de operaciones | 2 | normal |
| test_los_parentesis_cambian_la_agrupacion | parser | Que el arbol resultante de una operacion de suma y multiplicacion con parentesis, se agrupe correctamente (priorizando ahora el parentesis) y el arbol muestre correctamente dicha jerarquia de operaciones | 2 | normal |

> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

### 2.2 ¿Qué comportamientos **no** estaban probados?

La resta cuando se resta un numero mayor, la divison donde el residuo no sea cero, si los parentesis estan vacios, un parentesis incompleto, la asociacion (a la izquierda) sin parentesis entre la multiplicacion y la division y la suma y resta, la division entre 0, la resta con 0, la suma con 0, la resta con un mismo numero, lo que sucede si se ingresa un texto o se combina texto con operaciones.
> Ésta es la pregunta importante de toda la tarea. Tómense su tiempo.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| test_evualator::test_suma_ambos_cero | 0 + 0 | 0 | Frontera | Pues estamos justo en el cero y tenemos que asegura que las reglas del cero se cumplan, es decir, que el 0 no vaya a negativos o positivos |
| test_evualator::test_suma_cero_y_uno | 0 + 1 | 1 | Frontera | Pues es justo despues de que cambie el comportamiento de la suma (de 0 a naturales) |
| test_evualator::test_resta_mismo_numero | 3 - 3 | 0 | Frontera | Pues es justo donde se cambia el comportamiento de la resta (de naturales a 0) |
| test_evualator::test_resta_cero_y_uno | 0 - 1 | -1 | Frontera | Pues es justo antes de que cambie el comportamiento de la resta (de enteros negativos a 0) |
| test_evualator::test_resta_cero_al_final | 1 - 0 | 1 | Frontera | Pues es justo antes de que cambie el comportamiento de la resta (de naturales a 0) |
| test_evualator::test_resta_ambos_cero | 0 - 0 | 0 | Frontera | Pues estamos justo en el 0 y tenemos que asegura que las reglas del cero se cumplan, es decir, que el 0 no vaya a negativos o positivos |
| test_evualator::test_resta_el_mayor_al_final | 5 - 8 | -3 | Normal | Pues no es justo cuando se cambia de regla o cuando se esta apunto de cambair de regla |
| test_evaluator::test_multiplicacion_con_cero | 6 * 0 | 0 | Frontera | Pues es justo cuando se cambia de regla (a la del cero) y debemos verificar su comportamiento |
| test_evaluator::test_multiplicacion_ambos_cero | 0 * 0 | 0 | Frontera | Pues es justo cuando se cambia de regla (a la del cero) y debemos verificar su comportamiento |
| test_evaluator::test_division_de_cero | 0 / 2 | 0 | Frontera | Pues es justo cuando se cambia de regla (a la del cero) y debemos verificar su comportamiento |
| test_evaluator::test_division_entre_cero | 10 / 0 | Error | Invalido | La division en 0 no se puede, debemos checar que este error se cumpla (y este controlado en el programa) |
| test_evaluator::test_division_entre_cero_con_cero | 0 / 0 | Error | Invalido | Esta division no se puede |
| test_evaluator::test_precedencia_sin_parentesis_misma_precedencia_mult_div | 3 * 4 / 2 | 6 | Frontera | Cae justo en la regla de que, si se tiene misma precedencia se tome primero pro la izquierda |
| test_evaluator::test_precedencia_sin_parentesis_misma_precedencia_sum_res | 3 + 4 - 2 | 5 | Frontera | Cae justo en la regla de que, si se tiene misma precedencia se tome primero pro la izquierda |
| test_evaluator::test_parentesis_vacios | () | Error | Invalido | No contiene una operacion valida para evaluar |
| test_evaluator::test_parentesis_vacios_operaciones | ( ), () / 2, 3 + (), () * 2, (()), 2 / 1 + () | Error | Invalido | No se pueden hacer operaciones con parentesis vacios ya que no contienen indicaciones validas para evaluar |
| test_evaluator::test_parentesis_incompletos | (, ), (3 + 1, 3 * 2), (4 * 8)) | Error | Invalido | Los parentesis no estan completos por lo que la operacion ya no se puede evaluar o puede dar errores, ademas los parentesis incompletos por si solos no son una operacion valida |
| test_evaluator::test_asociar_izquierda_resta | 1 - 3 - 5 | -7 | Normal | No es justo cuando el comportamiento cambia, unicamente es un ejemplo de usar la misma operacion y que el resultado sea el correcto |
| test_evaluator::test_asociar_izquierda_division | 12 / 3 / 2 | 2 | Normal | No es justo cuando el comportamiento cambia, unicamente es un ejemplo donde si se asocia a la derecha el resultado es diferente |
| test_lexer::test_no_tokenizar_letras | 1 + a | Error | Invalido | No podemos sumar letras o combinar texto con operaciones |
| test_lexer::test_entradas_invalidas | a, 2 + a, abc, 2 & 1, holaa | Error | Invalido | No se pueden hacer operaciones con texto ni ingresar unicamente texto |
---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?
La prueba de parentesis incompletos y de entradas invalidas revelo que los errores (de entrada) no estaban siendo atrapados por el programa, como se pedia en las reglas, ni indicaban exactamente donde se produjo el error. 

La prueba de asociar a la izquierda de la resta y division revelo que el programa como estaba asociaba por la derecha en vez de la izquierda, como se pide en las regloas.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

Las reglas 8 y 9 del README (en Semantica declarada, seccion 7), se nos indica que el interprete debe de agarrar los errores de sintaxis con el error personalizado, no el de python, cosa que el programa no cumplia antes de las modificaciones (pues saltaba el error de python donde te enseñan en qu eparte de los archivos se dio el error) y se nos pide que cada error nos diga la posicion en que fallo y como el programa, antes de las modificaciones, no nos daba nuestro error perzonalizado no cumplia con la regla

La 6 regla del README (en Semantica declarada, seccion 7), nos pide que en caso de tener dos operacciones de la misma precedencia se asocien por la izquierda, cosa que no estaba haciendo el programa antes de las modificaciones

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| entradas invalidas no las agarraba ErrorDeSintaxis | "(" | Saltaba error de python | (Nuestro error de sintaxis personalizado, en este caso:) final de expresion inesperado (posicion n) | agrega nuevos tests de evaluator y lexer | lexer y parser: validacion de errores de sintaxis |
| entradas invalidas no las agarraba ErrorDeSintaxis | "a" | Saltaba error de python | (Nuestro error de sintaxis personalizado, en este caso:) Caracter invalido 'c' (posicion n) | agrega nuevos tests de evaluator y lexer | lexer y parser: validacion de errores de sintaxis |
| asociatividad por derecha | 1 - 3 - 5 | 3 | -7 | agrega nuevos tests de evaluator y lexer | lexer y parser: validacion de errores de sintaxis |


### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

Podemos decir que es una correcion general pues se hicieron mas de una prueba donde pasa el mismo defecto, pero las entradas son tan diferentes entre si que cubrimos variso casos donde el efecto es visible sin que se e bajo las mismas circustancias. Es decir, verificamos que en todos los casos posibles (que se nos ocurrieron) donde este defecto se pueda el programa ver se comporte como deberia, y no solo lo verificamos en la entrada que nos revelo el defecto


---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?
En la clase evaluator presenciamos demasiados condicionales para poder evaluar las operaciones, lo cual también implica duplicación de código. Ambas señales de mal diseño.

En la clase parser teniamos definidos "termino" y "expresion" los cuales hacian escencialmente lo mismo, solo cambiaban los operadores que buscaban y el método al que pedían sus operandos. Esa duplicación es una señal de mal diseño porque cualquier cambio en la lógica debía hacerse en ambos métodos, y cada nivel de precedencia nuevo exigía copiar otro método.


> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?
Modificamos la clase ast tal que la lógica de evaluar los operadores (y sus errores) recaiga en Nodo, y por lo tanto en Número y OperacionesBinarias, mientras que evaluator solo llama a estos metodos, haciendo así polimorfismo. Esto, además de solucionar los problemas mencionados anteriormente, pasa la responsabilidad de evaluar a ast en vez de evaluator, haciendo que ast maneje lógica y no solo sirva como si fuera una forma de hacer nodos y clasificarlos. 

En este caso se conversa el comportamiento pues la logica sigue siendo la misma (leemos el operador y de ahi evaluamos izq y derecha), solo cambiamos como se hace la logica. Tambien cambiamos la responsabilidad de evaluator a ast, pero como el flujo es ast -> evaluator, ast no tenia responsabilidad logica(mas alla de decir "este nodo tipo..") y la unica logica de evaluator era evaluar (y la pasamos a ast) esto no cambia el comportamiento, solo donde y el orden de lo que hacemos.  

Modificando la clase parser, termino y expresion podian unificarse en uno solo que construyera el arbol para todos los niveles de operaciones para eso se agrego NIVELES el cual agrupa los operadores de acuerdo a su orden de precedencia, con eso se borro termino y se conservo expresion, el cual busca los operadores del nivel que recibe y se llama a si mismo para pedir cada operando al nivel de abajo. Igualmente, se conserva el comportamiento porque cada nivel sigue tomando sus operandos del nivel más prioritario, así que la precedencia es la misma, mantiene la asociatividad a la izquierda y los test que ya estaban siguen pasando.


> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

Ninguno.
Se puede usar ambos, pero solo nos complicariamos de más el codigo.
De usar Factory Method se tendria que usar en Nodo y en las clases que lo heredan, o en Token pues son los unicos objetos en nuestro interprete. Sin embargo como Token esta "solo" como objeto (no hereda de nadie, no tiene hijos o hermanos) aplicar Factory seria sobredescomponer algo que no lo necesita

En Nodo (y demas) si bien si existe una jerarquia, parser ya sabe que va a trabajar con numeros y operaciones, ademas que los isntancia de maner alimpia y sin problemas. De agregar Factory algo sencillo que funciona (parser <-> ast), se el agregrian pasos extra qu eno son realmente necesarios

EL Adapter, por su parte, seria casi inutil pues cada parte esta conciente de con que se esta comunicando (es decir, por ejemplo, el parser sabe que va a recibir y trabajar con tokens) y se definen con base a esto. Agregar un Adapter seria agregar un paso más que no es necesario, lo cual nos sobrecomplicaria el codigo. 

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

Al no usar Factory Method, habria que tocar varias partes del codigo debido a que el comportamiento de los operadores sigue repartido en varios archivos. En lexer habría que agregar el simbolo y el nuevo tipo de token de ese operador. En parser decidir y ubicar correctamente el nivel al que pertenece. En ast agregarlo a sus operaciones, revisar las excepciones de ese operador y capturar sus respectivos errores con ErrorDeEvaluacion o ErrorDeSintaxis (dependiendo el caso) y no con errores de python. Y hacer los test respectivos. Por otra parte, hay que revisar los casos para asociar correctamente ya que operaciones como las potencias se deben asociar a la derecha. En varios casos de operaciones se tendria que ver su respectivo comportamiento (como los casos donde tienen solo una entrada y habria que modificar un poco mas el parser y ast) y en caso de que no sean "similares" a los ya definidos. Es por eso que lo mas dificil seria que se deben modificar varios archivos y revisar en cada uno que cumpla con lo necesario para evaluarlo bien.

> Por ejemplo `%`. ¿Cuántos archivos hay que tocar? ¿Por qué?

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
