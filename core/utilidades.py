import pygame
import math
import random

def lerp(inicio, fin, t):
    """
    Interpolación lineal entre dos valores
    
    No utilizada en el proyecto, se deja para uso futuro.
    """
    return inicio + (fin - inicio) * t

def distancia(pos1, pos2):
    """
    Calcula la distancia entre dos puntos
    
    No utilizada en el proyecto, se deja para uso futuro.
    """
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return math.sqrt(dx * dx + dy * dy)

def normalizar_vector(vector):
    """
    Normaliza un vector 2D
    
    No utilizada en el proyecto, se deja para uso futuro.    
    """
    magnitud = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
    if magnitud == 0:
        return (0, 0)
    return (vector[0] / magnitud, vector[1] / magnitud)

def generar_color_aleatorio():
    """Genera un color aleatorio"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
