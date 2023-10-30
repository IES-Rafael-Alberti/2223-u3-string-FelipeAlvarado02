

#Tienes este código:

"""palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador) """


#Encapsúlalo en una función llamada cuenta, y hazla genérica de
#tal modo que pueda aceptar una cadena y una letra como argumentos.



def cuenta(cadena:str, letra:str)-> int:
    """Función que devuelve el número de la cantidad
     total de una letra seleccionada en una cadena recibida."""

    LetrasRepetidas = 0

    for i in range(0,len(cadena)):

        if cadena[i] == letra:
            LetrasRepetidas += 1

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

            sucesion = cuenta(entradaCadena,entradaLetra)


        except ValueError:  # Si está en blanco.

            if entradaCadena.isspace() or entradaCadena == "":
                print("Por favor introduzca un escrito que no esté en blanco.\n")

            if entradaLetra.isspace() or entradaLetra == "":
                print("Por favor introduzca un escrito que no esté en blanco.\n")


    # Salida

    print(sucesion)