from mini_interprete.cli import interpretar
import pytest
from mini_interprete.errores import ErrorDeEvaluacion
from mini_interprete.errores import ErrorDeSintaxis

def test_suma():
    assert interpretar("3 + 4") == 7

def test_suma_ambos_cero():
    assert interpretar("0 + 0") == 0

def test_suma_cero_y_uno():
    assert interpretar("0 + 1") == 1 

def test_resta():
    assert interpretar("10 - 3") == 7

def test_resta_mismo_numero():
    assert interpretar("3 - 3") == 0

def test_resta_cero_y_uno():
    assert interpretar("0 - 1") == -1 

def test_resta_cero_al_final():
    assert interpretar("1 - 0") == 1

def test_resta_ambos_cero():
    assert interpretar("0 - 0") == 0

def test_resta_el_mayor_al_final():
    assert interpretar("5 - 8") == -3


def test_multiplicacion():
    assert interpretar("6 * 7") == 42

def test_multiplicacion_con_cero():
    assert interpretar("6 * 0") == 0

def test_multiplicacion_ambos_cero():
    assert interpretar("0 * 0") == 0     

def test_division():
    assert interpretar("10 / 2") == 5

def test_division_de_cero():
    assert interpretar("0 / 2") == 0

def test_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion): 
        interpretar("10 / 0")

def test_division_entre_cero():
    with pytest.raises(ErrorDeEvaluacion): 
        interpretar("10 / 0")

def test_division_entre_cero_con_cero():
    with pytest.raises(ErrorDeEvaluacion): 
        interpretar("0 / 0")
        
def test_precedencia_sin_parentesis():
    assert interpretar("3 + 4 * 2") == 11

def test_precedencia_sin_parentesis_misma_precedencia_mult_div():
    assert interpretar("3 * 4 / 2") == 6

def test_precedencia_sin_parentesis_misma_precedencia_sum_res():
    assert interpretar("3 + 4 - 2") == 5

def test_precedencia_con_parentesis():
    assert interpretar("(3 + 4) * 2") == 14

def test_parentesis_vacios():
    with pytest.raises(ErrorDeSintaxis):
        interpretar("()")

@pytest.mark.parametrize("entrada", ["( )", "() / 2", "3 + ()", "() * 2", "(())", "2 / 1 + ()" ])
def test_parentesis_vacios_operaciones(entrada):
    with pytest.raises(ErrorDeSintaxis):
        interpretar(entrada)

@pytest.mark.parametrize("entrada", ["(", ")", "(3 + 1", "3 * 2)", "(4 * 8))"])
def test_parentesis_incompletos(entrada):
    with pytest.raises(ErrorDeSintaxis):
        interpretar(entrada)

def test_asociar_izquierda_resta():
    assert interpretar("1 - 3 - 5") == -7

def test_asociar_izquierda_division():
    assert interpretar("12 / 3 / 2") == 2
