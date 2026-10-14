#import os
#import sys


def calcularPromedio(listaNotas):
    totalNotas = 0
    for nota in listaNotas:
        totalNotas = totalNotas + nota
    return totalNotas / len(listaNotas)


class estudiante:
    def __init__(self, nombreCompleto, notas):
        self.nombreCompleto = nombreCompleto
        self.notas = notas


print(calcularPromedio([90, 85, 77]))
