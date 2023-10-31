"""Hay un método de cadenas llamado count que es similar a find.
Lee la documentación de este método en: * Métodos en ingles * Métodos
en castellano y escribe el código necesario para invocar a este método y
contar el número de veces que una letra aparece en “banana”."""

def cuentaCount(cadena:str, letra:str)-> int:
    """Función que devuelve el número de la cantidad
     total de una letra seleccionada en una cadena recibida con Count."""

    LetrasRepetidas = cadena.count(letra)

    return LetrasRepetidas


if __name__ == "__main__":

    # Entrada

    EntradaEscrita = False
    entradaCadena = ""

    """Sucesión es una variable que almanezará el procesamiento realizado."""

    sucesion = ""

    # Procesamiento

    while not EntradaEscrita:

        try:

            entradaCadena = input("Escriba la frase a comparar:\n")

            entradaLetra = input("Escriba la letra a comparar:\n")


            if entradaCadena.isspace() or entradaCadena == "":
                raise ValueError


            if entradaLetra.isspace() or entradaLetra == "":
                raise ValueError

            EntradaEscrita = True

            sucesion = cuentaCount(entradaCadena, entradaLetra)


        except ValueError:  # Si está en blanco.

            if entradaCadena.isspace() or entradaCadena == "":
                print("Por favor introduzca un escrito que no esté en blanco.\n")

            if entradaLetra.isspace() or entradaLetra == "":
                print("Por favor introduzca un escrito que no esté en blanco.\n")


    # Salida

    print(sucesion)