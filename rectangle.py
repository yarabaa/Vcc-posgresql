import numpy as np
import math


def integrale_rectangle(func, a, b, n):
    # Largeur de chaque rectangle
    dx = (b - a) / n
    # Somme des aires des rectangles
    somme = 0.0
    for i in range(n):
        x = a + i * dx  # x à gauche de chaque rectangle
        somme += func(x) * dx  # Aire du rectangle
    return somme


def f(x):
    return 1 / x if x != 0 else 0  # Éviter la division par zéro


a = float(input("Entrez la borne inférieure de l'intervalle : "))
b = float(input("Entrez la borne supérieure de l'intervalle : "))

n = int(input("Entrez le nombre de subdivisions : "))


# Calcul de l'intégrale
resultat = integrale_rectangle(f, a, b, n)
print(f"L'intégrale de 1/x sur l'intervalle [{a}; {b}] est approximativement {resultat:.6f}")

log = math.log(2)-resultat
print(abs(log))