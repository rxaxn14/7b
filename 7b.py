import random

def evaluar(x):
    return x**2 + 2*x - 1

def crear_poblacion(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

def seleccionar_padres(poblacion):
    return random.sample(poblacion, 2)

def cruzar(padre1, padre2):
    return (padre1 + padre2) / 2

def mutar(hijo):
    return hijo + random.randint(-1, 1)

def algoritmo_genetico():
    tamano_poblacion = 10
    generaciones = 3
    poblacion = crear_poblacion(tamano_poblacion)

    for _ in range(generaciones):
        nueva_poblacion = []
        for _ in range(tamano_poblacion // 2):
            padre1, padre2 = seleccionar_padres(poblacion)
            hijo = cruzar(padre1, padre2)
            if random.random() < 0.2:
                hijo = mutar(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion

    mejor_individuo = max(poblacion, key=evaluar)
    print(f"Mejor individuo: {mejor_individuo} con aptitud {evaluar(mejor_individuo)}")

if __name__ == "__main__":
    algoritmo_genetico()
