# Análisis — Tarea 1

**Integrantes:**
1. Mendoza Aragón Edith Alejandra
2. Mondragón Ceballos Evelyn Vianey
3.

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | La expresion numerica que buscamos interpretar | Devuelve la expresion tokenizada, con los tokens en una lista (en el orden que se leyo), es decir, categoriza todo en su respectivo tipo (numero, mas, menos, etc) | De tokenizar la expresion |
| `parser` | La expresion ya tokenizada (es decir, la lista con los tokens) | Un AST que se encarga de definir la jerarquia de la operacion | De que podamos interpretar a la expresion con la jerarquia correcta (que le es indicada), es el encargado del analisis sintatico |
| `ast` | La expresion termino a termino ya organizado | Los nodos que componen a AST | De catogorizar que vemos como numero y que vemos como operacion binaria, de armar los nodos |
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

La resta cuando se resta un numero mayor, la divison donde el residuo no sea cero, si los parentesis estan vacios, un parentesis incompleto, la asociacion (a la izquierda) sin parentesis entre la multiplicacion y la division y la suma y resta, la division entre 0, la resta con 0, la suma con 0, la resta con un mismo numero, lo que sucede si se ingresa un texto o se combina texto con operaciones
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
| test_evaluator::test_precedencia_sin_parentesis_misma_precedencia_mult_div | 3 * 4 / 2 | 6 | Frontera | Cae justo en la regla de que, si se tiene misma precedencia se tome primero pro la izquierda |
| test_evaluator::test_precedencia_sin_parentesis_misma_precedencia_sum_res | 3 * 4 / 2 | 6 | Frontera | Cae justo en la regla de que, si se tiene misma precedencia se tome primero pro la izquierda |
---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

> No basta con "daba mal". Digan contra qué lo están comparando: qué regla,
> qué línea de la semántica declarada del README.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
|---|---|---|---|---|---|
| | | | | | |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

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
