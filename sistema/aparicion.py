# -*- coding: utf-8 -*-
"""
Sistema de aparición automática de partículas.

Este módulo controla la generación automática de partículas en la simulación,
incluyendo la velocidad de aparición, el área donde aparecen las partículas,
el tamaño de los clusters y la posición donde se generan.
"""

import random
from core.constantes import (
    VELOCIDAD_APARICION_POR_DEFECTO, VELOCIDAD_APARICION_MAXIMA, VELOCIDAD_APARICION_MINIMA,
    INCREMENTO_VELOCIDAD, ANCHO_APARICION_POR_DEFECTO, TAMANO_CLUSTER_POR_DEFECTO, 
    TAMANO_CLUSTER_MAXIMO
)

class SistemaAparicion:
    """
    Controla la aparición automática de partículas en la simulación.
    
    Este sistema maneja todos los aspectos relacionados con la generación
    automática de partículas: cuándo aparecen, dónde aparecen, cuántas
    aparecen y en qué configuración (clusters).
    
    Atributos:
        habilitado (bool): Si la aparición automática está activada
        velocidad (float): Velocidad actual de aparición (partículas por frame)
        ancho_area (int): Ancho del área donde aparecen las partículas
        tamaño_cluster (int): Tamaño del cluster de partículas a generar
    """
    
    def __init__(self):
        """
        Inicializa el sistema de aparición automática.
        
        Configura los valores iniciales para todos los parámetros de aparición
        usando las constantes definidas en el archivo de configuración.
        """
        self.habilitado = True                                     # Estado inicial: aparición activada
        self.velocidad = VELOCIDAD_APARICION_POR_DEFECTO           # Velocidad inicial de aparición
        self.ancho_area = ANCHO_APARICION_POR_DEFECTO              # Ancho inicial del área de aparición
        self.tamaño_cluster = TAMANO_CLUSTER_POR_DEFECTO           # Tamaño inicial de clusters
    
    def calcular_apariciones(self):
        """
        Calcula cuántas partículas generar en el frame actual.
        
        Utiliza un sistema híbrido que combina apariciones garantizadas
        (parte entera de la velocidad) con apariciones probabilísticas
        (parte decimal de la velocidad) para permitir velocidades fraccionarias.
        
        Retorna:
            int: Número de partículas a generar en este frame
            
        Algoritmo:
            1. Si está deshabilitado, retorna 0
            2. Extrae la parte entera (apariciones garantizadas)
            3. Extrae la parte decimal (probabilidad de aparición adicional)
            4. Usa la parte decimal como probabilidad para una aparición extra
            
        Ejemplo:
            - Velocidad 2.3: Genera 2 partículas + 30% probabilidad de una tercera
            - Velocidad 0.5: 50% probabilidad de generar 1 partícula
        """
        if not self.habilitado:                    # Si está deshabilitado
            return 0                               # No generar partículas
            
        # Separar parte entera y decimal de la velocidad
        apariciones_base = int(self.velocidad)     # Apariciones garantizadas por frame
        parte_decimal = self.velocidad - apariciones_base  # Probabilidad de aparición adicional
        
        # Comenzar con las apariciones garantizadas
        apariciones_este_frame = apariciones_base
        
        # Agregar aparición probabilística basada en la parte decimal
        if random.random() < parte_decimal:
            apariciones_este_frame += 1
            
        return apariciones_este_frame
    
    def calcular_posicion(self, columnas_grilla):
        """
        Calcula la posición horizontal donde aparecerá una nueva partícula.
        
        Determina la columna donde debe aparecer la partícula basándose en
        el ancho del área de aparición configurado. Puede usar todo el ancho
        dela grilla o solo una porción central.
        
        Parámetros:
            columnas_grilla (int): Número total de columnas disponibles en la grilla
            
        Retorna:
            int: Número de columna donde debe aparecer la partícula (0-indexado)
            
        Comportamiento:
            - Si ancho_area >= columnas_grilla: Usa todo el ancho disponible
            - Si ancho_area < columnas_grilla: Usa área centrada del tamaño especificado
        """
        # Si el ancho de área es mayor o igual al ancho total, usar todo el campo
        if self.ancho_area >= columnas_grilla:
            return random.randint(0, columnas_grilla - 1)
        else:
            # Calcular área centrada de aparición
            centro_columna = columnas_grilla // 2              # Columna central de la grilla
            rango_aparicion = self.ancho_area // 2           # Mitad del ancho de aparición
            
            # Calcular límites del área de aparición centrada
            limite_izquierdo = max(0, centro_columna - rango_aparicion)
            limite_derecho = min(columnas_grilla - 1, centro_columna + rango_aparicion)
            
            # Elegir columna aleatoria dentro del área
            return random.randint(limite_izquierdo, limite_derecho)
    
    def aumentar_velocidad(self):
        """
        Incrementa la velocidad de aparición.
        
        Aumenta la velocidad de aparición en el incremento configurado,
        sin exceder el límite máximo establecido.
        
        Retorna:
            float: Nueva velocidad de aparición después del incremento
        """
        self.velocidad = min(VELOCIDAD_APARICION_MAXIMA, self.velocidad + INCREMENTO_VELOCIDAD)
        return self.velocidad
    
    def disminuir_velocidad(self):
        """
        Reduce la velocidad de aparición.
        
        Disminuye la velocidad de aparición en el incremento configurado,
        sin bajar del límite mínimo establecido.
        
        Retorna:
            float: Nueva velocidad de aparición después de la reducción
        """
        self.velocidad = max(VELOCIDAD_APARICION_MINIMA, self.velocidad - INCREMENTO_VELOCIDAD)
        return self.velocidad
    
    def aumentar_ancho(self, ancho_maximo):
        """
        Incrementa el ancho del área de aparición.
        
        Expande el área donde pueden aparecer partículas, hasta el
        límite del ancho total de la grilla.
        
        Parámetros:
            ancho_maximo (int): Ancho máximo permitido (generalmente el ancho de la grilla)
            
        Retorna:
            int: Nuevo ancho del área de aparición
        """
        self.ancho_area = min(ancho_maximo, self.ancho_area + 2)
        return self.ancho_area
    
    def disminuir_ancho(self):
        """
        Reduce el ancho del área de aparición.
        
        Contrae el área donde pueden aparecer partículas, con un
        límite mínimo de 5 columnas para mantener funcionalidad.
        
        Retorna:
            int: Nuevo ancho del área de aparición
        """
        self.ancho_area = max(5, self.ancho_area - 2)
        return self.ancho_area
    
    def aumentar_cluster(self):
        """
        Incrementa el tamaño del cluster de partículas.
        
        Aumenta el número de partículas que se generan juntas,
        hasta el límite máximo configurado.
        
        Retorna:
            int: Nuevo tamaño del cluster
        """
        self.tamaño_cluster = min(TAMANO_CLUSTER_MAXIMO, self.tamaño_cluster + 1)
        return self.tamaño_cluster
    
    def disminuir_cluster(self):
        """
        Reduce el tamaño del cluster de partículas.
        
        Disminuye el número de partículas que se generan juntas,
        con un mínimo de 1 partícula por cluster.
        
        Retorna:
            int: Nuevo tamaño del cluster
        """
        self.tamaño_cluster = max(1, self.tamaño_cluster - 1)
        return self.tamaño_cluster
    
    def alternar_estado(self):
        """
        Alterna el estado de habilitado/deshabilitado del sistema.
        
        Cambia entre activar y desactivar la aparición automática
        de partículas.
        
        Retorna:
            bool: Nuevo estado del sistema (True = habilitado, False = deshabilitado)
        """
        self.habilitado = not self.habilitado
        return self.habilitado
    
    def esta_en_ancho_completo(self, columnas_grilla):
        """
        Verifica si el área de aparición cubre todo el ancho de la grilla.
        
        Determina si el ancho configurado para la aparición de partículas
        es igual o mayor al ancho total de la grilla de simulación.
        
        Parámetros:
            columnas_grilla (int): Número total de columnas de la grilla
            
        Retorna:
            bool: True si cubre todo el ancho, False en caso contrario
        """
        return self.ancho_area >= columnas_grilla 