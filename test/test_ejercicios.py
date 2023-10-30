import pytest
from src.ejercicio1 import sucesionEdad
from src.ejercicio2 import sucesionNumeroImpar
from src.ejercicio3 import cuenta



#Ejercicio 1


@pytest.mark.parametrize(
    "edad, sucesion",
    [
        (2, "1,2,"),
        (4, "1,2,3,4,"),
        (7, "1,2,3,4,5,6,7,")
    ]
)
def test_sucesionEdad(edad,sucesion):
    assert sucesionEdad(edad) == sucesion


def test_sucesionEdadExepciones():
    with pytest.raises(ValueError):
        sucesionEdad(-2)


#Ejercicio 2


@pytest.mark.parametrize(
    "numero, sucesion",
    [
        (2, "1,"),
        (9, "1,3,5,7,9,"),
        (15, "1,3,5,7,9,11,13,15,")
    ]
)
def test_sucesionNumeroImpar(numero,sucesion):
    assert sucesionNumeroImpar(numero) == sucesion



def test_sucesionNumeroImparExepciones():
    with pytest.raises(ValueError):
        sucesionNumeroImpar(-2)


#Ejercicio 3

@pytest.mark.parametrize(
    "numero, sucesion",
    [
        (2, "2,1,0,"),
        (9, "9,8,7,6,5,4,3,2,1,0,"),
        (1, "1,0,")
    ]
)
def test_numerosConsecutivosInversos(numero,sucesion):
    assert cuenta(numero) == sucesion

def test_numerosConsecutivosInversosExepciones():
    with pytest.raises(ValueError):
        cuenta(-2)