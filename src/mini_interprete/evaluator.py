"""Del AST a un numero.

Recorre el arbol de abajo hacia arriba: para evaluar una operacion hay que
evaluar primero sus dos lados.
"""

from .ast import Numero, OperacionBinaria


def evaluar(nodo):
    """Evalua un nodo del AST y regresa su valor."""
    return nodo.evaluar()
