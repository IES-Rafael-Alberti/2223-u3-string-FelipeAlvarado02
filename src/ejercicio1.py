"""Escribe un bucle while que comience con el último carácter en la
cadena y haga un recorrido hacia atrás hasta el primer carácter en
la cadena,imprimiendo cada letra en una línea independiente."""


def darVueltaCadena(cadena: str) -> str:
    """ Recibe una cadena y le da la vuelta. """

    contador = len(cadena)-1

    resultado = ""

    while contador >= 0:

        resultado += cadena[contador]+"\n"
        contador -= 1

    return resultado


if __name__ == "__main__":

    #Entrada

    cadenaEscrita = False
    entradaCadena = ""

    """Sucesión es una variable que almanezará el procesamiento realizado."""

    sucesion = ""

    #Procesamiento

    while not cadenaEscrita:

        try:

            entradaCadena = input("Escriba lo que desee dar la vuelta:\n")

            if entradaCadena.isspace() or entradaCadena == "":
                raise ValueError

            sucesion = darVueltaCadena(entradaCadena)

            cadenaEscrita = True

        except ValueError:  # Si está en blanco.

            if entradaCadena.isspace():
                print("Por favor introduzca un escrito que no esté en blanco.\n")


    #Salida

    print(sucesion)

