# -*- coding: utf-8 -*-
"""
Constantes globales del simulador de perlita.

Este archivo contiene todas las constantes de configuración del juego,
organizadas por categorías para facilitar su mantenimiento y modificación.
"""

# =============================================================================
# CONFIGURACIÓN VISUAL DEL JUEGO
# =============================================================================

# Colores del borde y área de juego
COLOR_BORDE = (0, 255, 0)              # Color verde del contorno del área de juego
ANCHO_BORDE = 20                       # Ancho en píxeles del borde verde
ANCHO_AREA_JUEGO = 200                 # Ancho en píxeles del área de simulación
ALTO_AREA_JUEGO = 600                  # Alto en píxeles del área de simulación
TAMANO_CELDA_INICIAL = 3               # Tamaño inicial en píxeles de cada celda de la grilla

# =============================================================================
# SISTEMA DE NIVEL Y DRENAJE
# =============================================================================

# Configuración del sistema de drenaje automático
TIEMPO_DRENAJE_SEGUNDOS = 2.0          # Duración en segundos del proceso de drenaje
COLOR_LINEA_NIVEL = (255, 0, 0)        # Color rojo de la línea indicadora de nivel
ANCHO_LINEA_NIVEL = 5                  # Grosor en píxeles de la línea de nivel

# =============================================================================
# PALETA DE COLORES (estilo 8-bit inspirados en perlita expandida)
# =============================================================================

# Colores básicos
NEGRO = (0, 0, 0)                      # Color negro puro
BLANCO = (255, 255, 255)               # Color blanco puro
GRIS = (29, 29, 29)                    # Gris oscuro para el fondo del área de juego
AMARILLO = (255, 255, 0)               # Color amarillo puro

# Colores de partículas
COLOR_PERLIA = (240, 240, 235)         # Color perlita expandida - blanco perlado
COLOR_ROCA = (150, 150, 150)           # Color gris para las partículas de roca
COLOR_BORRADOR = (0, 0, 255)           # Color azul para el modo borrador

# Colores de interfaz
PERLITA_OSCURA = (200, 200, 195)         # Color de fondo claro tipo perlita
PERLITA_CLARA = (250, 250, 245)          # Color perlita clara para texto y elementos UI

# =============================================================================
# CONFIGURACIÓN DE LA SIMULACIÓN DE PARTÍCULAS
# =============================================================================

# Parámetros de aparición automática
VELOCIDAD_APARICION_POR_DEFECTO = 1.0  # Velocidad inicial de generación de partículas
VELOCIDAD_APARICION_MAXIMA = 10.0      # Velocidad máxima permitida de aparición
VELOCIDAD_APARICION_MINIMA = 0.0       # Velocidad mínima permitida de aparición
INCREMENTO_VELOCIDAD = 0.2             # Incremento/decremento al cambiar velocidad

# Parámetros de área de aparición
ANCHO_APARICION_POR_DEFECTO = 100      # Ancho inicial del área donde aparecen partículas
TAMANO_CLUSTER_POR_DEFECTO = 1         # Tamaño inicial del cluster de partículas
TAMANO_CLUSTER_MAXIMO = 10             # Tamaño máximo permitido para clusters

# Configuración de mensajes en pantalla
DURACION_MENSAJE = 2.0                 # Duración en segundos de los mensajes en pantalla

# =============================================================================
# ESTADOS DEL JUEGO
# =============================================================================

class EstadosJuego:
    """
    Enumeración de los posibles estados del juego.
    
    Esta clase define las constantes que representan los diferentes estados
    por los que puede pasar la aplicación durante su ejecución.
    """
    PRESENTACION = "presentacion"       # Estado inicial con logo de la empresa
    MENU = "menu"                      # Estado del menú principal
    JUEGO = "juego"                    # Estado de la simulación activa

# =============================================================================
# CONFIGURACIÓN DE FÍSICA Y RENDIMIENTO
# =============================================================================

# Parámetros de simulación física
PROBABILIDAD_APARICION_PERLITA = 0.15    # Probabilidad de que aparezca una partícula de perlita
FRAMES_POR_SEGUNDO = 120                 # FPS objetivo de la simulación

# Configuración de controles (no implementado, se lo deja planteado para futuras versiones)
TAMANO_PINCEL_POR_DEFECTO = 3          # Tamaño inicial del pincel de dibujo
SENSIBILIDAD_MOUSE = 1.0               # Sensibilidad del mouse para dibujar

# =============================================================================
# CONFIGURACIÓN DE VENTANA Y PANTALLA
# =============================================================================

# Dimensiones iniciales de ventana
ANCHO_VENTANA_INICIAL = 1200           # Ancho inicial de la ventana del juego
ALTO_VENTANA_INICIAL = 800             # Alto inicial de la ventana del juego
TITULO_VENTANA = "Simulación de Acumulación de Partículas de Perlita"

# Configuración de pantalla completa
MARGEN_PANTALLA = 100                  # Margen en píxeles desde los bordes de la pantalla
TIEMPO_PRESENTACION = 10               # Tiempo en segundos antes de avanzar automáticamente 