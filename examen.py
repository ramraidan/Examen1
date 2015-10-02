import unittest
# -*- coding:utf-8 -*-


def pruebas():
    """
    >>>contadorcaracteres("hola.com.mx", ".")
    3
    """


def contadorcaracateres(cadena, caracter):
    resultado = {}
    contador = 0
    for caracter in cadena:
        if caracter in cadena:
            contador = contador + 1
            resultado[caracter, contador]
        print caracter, "aparece ", contador, "veces"
    return resultado
    print resultado

    if __name__ == "__main__":
        unittest.main()
