"""Los nodos del arbol de sintaxis abstracta.

Para  3 + 4 * 2  el arbol es:

              OperacionBinaria('+')
              /                   \\
        Numero(3)          OperacionBinaria('*')
                            /                  \\
                      Numero(4)            Numero(2)

Un Numero no contiene nada. Una OperacionBinaria contiene otros nodos, que a
su vez pueden ser numeros u otras operaciones.
"""
from .errores import ErrorDeEvaluacion
import operator

class Nodo:
    """Cualquier cosa que pueda aparecer en el arbol."""

    def evaluar(self):
        raise ErrorDeEvaluacion(f"nodo desconocido: {self!r}")


class Numero(Nodo):
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Numero({self.valor})"

    def __eq__(self, otro):
        if not isinstance(otro, Numero):
            return NotImplemented
        return self.valor == otro.valor

    def evaluar(self):
        return self.valor


class OperacionBinaria(Nodo):

    OPERACIONES = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }


    def __init__(self, operador: str, izquierda: Nodo, derecha: Nodo):
        self.operador = operador
        self.izquierda = izquierda
        self.derecha = derecha

    def __repr__(self):
        return (f"OperacionBinaria({self.operador!r}, "
                f"{self.izquierda!r}, {self.derecha!r})")

    def __eq__(self, otro):
        if not isinstance(otro, OperacionBinaria):
            return NotImplemented
        return (self.operador == otro.operador
                and self.izquierda == otro.izquierda
                and self.derecha == otro.derecha)

    def evaluar(self):
        izquierda = self.izquierda.evaluar()
        derecha = self.derecha.evaluar()

        if self.operador == "/" and derecha == 0:
            raise ErrorDeEvaluacion("division entre cero")

        if self.operador in self.OPERACIONES:
            return self.OPERACIONES[self.operador](izquierda, derecha)

        raise ErrorDeEvaluacion(f"operador desconocido: {self.operador!r}")

