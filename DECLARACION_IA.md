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

- [ * ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [ ] **Sí.** Contesten los cinco puntos.

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

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
Quiero hacer, en python, un diccionario OPERACIONES tal que cada opercion tenga un simbolo (string) asociado y que al llamarlo pueda evaluarse (tipo if op is in OPERACIONES do (a,b)[operacion])

```

```
(prompt 2)
```

---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
| Un codigo de ejemplo donde nos daba un diccionario y como usarlo en un if simple. Se nos dio dos opciones, usando operator o lambda, y una simplificacion para usar get en vez de if .. in | Modificado | Al no pasarle el codigo, si no la idea, ni el contexto no se podia simplemente aceptar lo que se nos dio, se tenia que modiicar para que fuera compatible con lo que teniamos en ast | commit: refactorizacion de ast y evaluator (repeticion de ifs). En ast.py  |


> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Para ast: una vez se adapto al codigo se volvieorn a hacer las pruebas y todas pasaron, es decir, que si se estab aleyendo el diccionario bien (estaba identificando bien los simbolos y como evaluarlo)

> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.

### 5.2 ¿Qué harían distinto la próxima vez?

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Mendoza Aragón Edith Alejandra | 323238702 |
