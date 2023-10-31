import pytest
from src.ejercicio1 import darVueltaCadena
from src.ejercicio3 import cuenta
from src.ejercicio4 import cuentaCount

"""from src.ejercicio4 import cuenta"""


#Ejercicio 1


@pytest.mark.parametrize(
    "cadena, sucesion",
    [
        ("Holaa", "a\na\nl\no\nH\n"),
        ("ePepA", "A\np\ne\nP\ne\n")
    ]
)
def test_darVueltaCadena(cadena,sucesion):
    assert darVueltaCadena(cadena) == sucesion


#Ejercicio 3


@pytest.mark.parametrize(
    "cadena, letra, sucesion",
    [
        ("holaaa", "a", 3),
        ("peeeppeeasdp", "p", 4),
        ("Meroasdp", "h", 0)
    ]
)
def test_cuenta(cadena, letra, sucesion):
    assert cuenta(cadena, letra) == sucesion


#Ejercicio 4


@pytest.mark.parametrize(
    "cadena, letra, sucesion",
    [
        ("holaaa", "a", 3),
        ("peeeppeeasdp", "p", 4),
        ("Meroasdp", "h", 0)
    ]
)
def test_cuentaCount(cadena, letra, sucesion):
    assert cuentaCount(cadena, letra) == sucesion
