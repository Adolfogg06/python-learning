
def calcular_promedio(lista_notas):
    total_notas = 0
    for nota in lista_notas:
        total_notas = total_notas + nota
    return total_notas / len(lista_notas)


class Estudiante:
    def __init__(self, nombre_completo, notas):
        self.nombre_completo = nombre_completo
        self.notas = notas


print(calcular_promedio([90, 85, 77]))
