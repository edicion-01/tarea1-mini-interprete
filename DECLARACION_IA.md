# Declaración de uso de Inteligencia Artificial

**Actividad:**
**Integrantes:**
**Fecha:**

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [  ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [ * ] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
| Gemini | 3.6 |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Para ayudarnos en la factorizacion del ast, en especifico como hacer el dicionario que guaradara el string de las operaiones y que a la vez guardara como evaluar cada una de estas, pues se tenia la idea pero no exactamente como ejecutarla | commit: refactorizacion de ast y evaluator (repeticion de ifs). En ast.py |
| Para ayudarnos a borrar un commit y ayudarnos a subirlo correctamente. Salia un error debido a que el repositorio tenia mas commits que el local y pedia divergir las ramas y sobreescribir el codigo, al subirse al repositorio hacia commits extra para corregir esos errores y decidimos borrarlos y buscar como subirlo sin necesitar eso | commit::agrega nuevos tests de evaluator y lexer , commit::lexer y parser: validacion de errores de sintaxis , commit:: Refactorizacion de expresion y termino |
| Para unir termino y expresion, teniendo NIVELES y conservando la estructura general que seguian ambos, se añadio un if para verificar correctamente el nivel, sin embargo, al terminar volvio a asociar a la derecha, las pruebas fallaban y no lográbamos identificar si el error estaba en cómo se buscaba el nivel o en que no se llegaba al while, por lo que nos ayudo a ver que olvidamos especificar el nivel en el que estabamos buscando en el while| commit::Refactorizacion de expresion y termino |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
Quiero hacer, en python, un diccionario OPERACIONES tal que cada opercion tenga un simbolo (string) asociado y que al llamarlo pueda evaluarse (tipo if op is in OPERACIONES do (a,b)[operacion])

```
```
Como puedo borrar commits que ya subi a GitHub y volver a subirlos sin que aparezca un commit de merge branch?

Al unificar dos metodos cambio la forma en que asocia una operacion (antes a la izquierda, ahora a la derecha), use un while y recorre una agrupacion de NIVELES (contiene tuplas de suma con resta y multiplicacion con division), es posible que el fallo se deba a como busco el nivel o a como estoy recorriendo la agrupacion?
```
---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
| Un codigo de ejemplo donde nos daba un diccionario y como usarlo en un if simple. Se nos dio dos opciones, usando operator o lambda, y una simplificacion para usar get en vez de if .. in | Modificado | Al no pasarle el codigo, si no la idea, ni el contexto no se podia simplemente aceptar lo que se nos dio, se tenia que modiicar para que fuera compatible con lo que teniamos en ast | commit: refactorizacion de ast y evaluator (repeticion de ifs). En ast.py  |
| Dio tres opciones que podrian dar el error, para la condicion del while sugirio revisar que se especificara a que nivel nos referiamos, que estuviera bien definido NIVELES, y revisar si dentro del while modificaba incorrectamente el nivel| Modificado | las opciones marcaban donde podia darse el error pero al no conocer los archivos habia que revisar mas a detalle cada opcion y se encontro que si faltaba especificar bien el nivel del while y en derecha, por lo que no se uso totalmente lo que dijo | commit::Refactorizacion de expresion y termino |


> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | |
| No aplica | No aplica |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Para ast: una vez se adapto al codigo se volvieorn a hacer las pruebas y todas pasaron, es decir, que si se estaba leyendo el diccionario bien (estaba identificando bien los simbolos y como evaluarlo)

Para parser: con la unificacion se volvieron a hacer las pruebas y las pruebas que antes no pasaban por el error pasaron, lo que nos quiere decir que ascocio correctamente a la izquierda.

> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

Cuando no conoce los archivos puede dar sugerencias o ejemplos de apoyo pero que no dan una respuesta inmediata o puede dar ideas que no tengan tanta relacion con el problema que se tiene y que en cierto punto puedan hacer perder tiempo que puede usarse para identificar y corregir lo que se necesita

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.

### 5.2 ¿Qué harían distinto la próxima vez?

Revisar mas detalladamente nuestras ideas y ubicar mejor lo que necesitamos o lo que puede que nos cause algun problema o error, tratar de ser mas especificas y delimitar un poco mejor nuestras dudas.

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Mendoza Aragón Edith Alejandra | 323238702 |
| Mondragón Ceballos Evelyn Vianey | 323157814 |
