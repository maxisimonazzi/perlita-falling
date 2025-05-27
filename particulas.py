# -*- coding: utf-8 -*-
"""
Clases de Partículas del Simulador de Perlita.

Este módulo define las diferentes tipos de partículas que pueden existir
en la simulación, cada una con sus propias características físicas y
comportamientos específicos.

Tipos de partículas:
- ParticulaPerlita: Representa granos de perlita expandida con física de caída
- ParticulaRoca: Representa obstáculos sólidos inmóviles

Funciones auxiliares:
- generar_color_perlita(): Genera colores realistas para perlita expandida
- generar_color_aleatorio(): Utilidad para generar colores HSV aleatorios
"""

import random
import colorsys

class ParticulaPerlita:
	"""
	Representa una partícula de perlita expandida.
	
	Esta clase implementa el comportamiento físico de los granos de perlita,
	incluyendo la caída por gravedad y el deslizamiento lateral cuando
	encuentran obstáculos. Cada partícula tiene un color único generado
	aleatoriamente para simular las variaciones naturales de la perlita.
	
	Características:
	- Color: Tonos blancos perlados con variaciones sutiles
	- Física: Cae por gravedad, se desliza lateralmente
	- Comportamiento: Busca espacios libres para moverse
	"""
	
	def __init__(self):
		"""
		Inicializa una nueva partícula de perlita expandida.
		
		Genera un color aleatorio que simula los tonos naturales
		de la perlita expandida (blancos perlados con variaciones).
		"""
		# Generar color realista de perlita expandida
		self.color = generar_color_perlita()

	def actualizar(self, grilla, fila, columna):
		"""
		Actualiza la posición de la partícula aplicando física.
		
		Este método implementa el comportamiento físico de la partícula:
		1. Intenta caer directamente hacia abajo (gravedad)
		2. Si no puede, intenta deslizarse diagonalmente
		3. Si no hay movimiento posible, permanece en su lugar
		
		Parámetros:
			grilla: La grilla que contiene la partícula
			fila (int): Fila actual de la partícula
			columna (int): Columna actual de la partícula
			
		Retorna:
			tuple: Nueva posición (fila, columna) de la partícula
			
		Algoritmo de movimiento:
		1. Verificar si puede caer directamente (celda inferior libre)
		2. Si no, intentar caer en diagonal (izquierda o derecha aleatoria)
		3. Si ningún movimiento es posible, mantener posición actual
		"""
		# Intentar caer directamente hacia abajo (gravedad principal)
		if grilla.esta_celda_vacia(fila + 1, columna):
			return fila + 1, columna
		else:
			# Si no puede caer directamente, intentar deslizarse en diagonal
			desplazamientos_laterales = [-1, 1]  # Izquierda y derecha
			random.shuffle(desplazamientos_laterales)  # Orden aleatorio para evitar sesgos
			
			for desplazamiento in desplazamientos_laterales:
				nueva_columna = columna + desplazamiento
				# Verificar si puede caer en diagonal
				if grilla.esta_celda_vacia(fila + 1, nueva_columna):
					return fila + 1, nueva_columna

		# Si no hay movimiento posible, mantener posición actual
		return fila, columna

class ParticulaRoca:
	"""
	Representa una partícula de roca (obstáculo sólido).
	
	Las partículas de roca son elementos estáticos que no se mueven
	y actúan como obstáculos para las partículas de perlita. Se usan
	para crear barreras, canales y estructuras en la simulación.
	
	Características:
	- Color: Tonos grises oscuros
	- Física: Completamente estática (no se mueve)
	- Función: Actúa como obstáculo para otras partículas
	"""
	
	def __init__(self):
		"""
		Inicializa una nueva partícula de roca.
		
		Genera un color gris oscuro aleatorio para simular
		las variaciones naturales en el color de las rocas.
		"""
		# Generar color gris oscuro para simular roca
		self.color = generar_color_aleatorio(
			rango_matiz=(0.0, 0.1),        # Sin matiz (gris)
			rango_saturacion=(0.1, 0.3),   # Baja saturación
			rango_valor=(0.3, 0.5)         # Valor medio-bajo (oscuro)
		)

def generar_color_perlita():
	"""
	Genera colores aleatorios realistas para perlita expandida.
	
	La perlita expandida tiene un color característico blanco perlado
	con ligeras variaciones naturales. Esta función simula esas
	variaciones generando tonos blancos con pequeñas diferencias.
	
	Retorna:
		tuple: Color RGB (r, g, b) con valores entre 0-255
		
	Características del color generado:
	- Base: Blanco perlado (240, 240, 235)
	- Variación: ±15 en rojo y verde, -5 adicional en azul
	- Rango: Entre 225-255 para mantener tonos claros
	"""
	# Base de color blanco perlado característico de la perlita
	base_blanco = 240
	variacion = random.randint(-15, 15)  # Variación sutil para naturalidad
	
	# Calcular componentes RGB con variaciones controladas
	rojo = max(225, min(255, base_blanco + variacion))
	verde = max(225, min(255, base_blanco + variacion))
	# Ligeramente menos azul para el tono perlado característico
	azul = max(220, min(255, base_blanco + variacion - 5))
	
	return (rojo, verde, azul)

def generar_color_aleatorio(rango_matiz, rango_saturacion, rango_valor):
	"""
	Genera un color aleatorio usando el espacio de color HSV.
	
	Esta función utilidad permite generar colores aleatorios
	con control preciso sobre los rangos de matiz, saturación
	y valor, útil para crear paletas de colores específicas.
	
	Parámetros:
		rango_matiz (tuple): Rango (min, max) para el matiz (0.0-1.0)
		rango_saturacion (tuple): Rango (min, max) para saturación (0.0-1.0)
		rango_valor (tuple): Rango (min, max) para el valor/brillo (0.0-1.0)
		
	Retorna:
		tuple: Color RGB (r, g, b) con valores entre 0-255
		
	Ejemplo:
		# Generar un color azul oscuro
		color = generar_color_aleatorio((0.5, 0.7), (0.8, 1.0), (0.3, 0.6))
	"""
	# Generar valores HSV aleatorios dentro de los rangos especificados
	matiz = random.uniform(*rango_matiz)
	saturacion = random.uniform(*rango_saturacion)
	valor = random.uniform(*rango_valor)
	
	# Convertir de HSV a RGB
	r, g, b = colorsys.hsv_to_rgb(matiz, saturacion, valor)
	
	# Convertir a valores enteros 0-255
	return int(r * 255), int(g * 255), int(b * 255)
