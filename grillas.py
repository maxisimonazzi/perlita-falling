# -*- coding: utf-8 -*-
"""
Sistema de Grilla del Simulador de Perlita.

Este módulo contiene la clase Grilla que maneja la estructura de datos
bidimensional donde se almacenan y organizan todas las partículas de la simulación.
La grilla actúa como el espacio físico donde las partículas pueden existir y moverse.

Funcionalidades principales:
- Almacenamiento eficiente de partículas en una matriz 2D
- Operaciones de inserción, eliminación y consulta de partículas
- Renderizado visual de todas las partículas
- Validación de límites y detección de colisiones
- Limpieza completa del espacio de simulación
"""

import pygame

class Grilla:
	"""
	Representa la grilla bidimensional donde se almacenan las partículas.
	
	Esta clase implementa una matriz 2D que actúa como el espacio físico
	de la simulación. Cada celda puede contener una partícula o estar vacía.
	La grilla maneja todas las operaciones espaciales y de renderizado.
	
	Características:
	- Estructura de datos: Matriz 2D de celdas
	- Cada celda puede contener una partícula o None (vacía)
	- Coordenadas: (fila, columna) donde (0,0) es la esquina superior izquierda
	- Renderizado: Dibuja todas las partículas con sus colores respectivos
	"""
	
	def __init__(self, ancho, alto, tamaño_celda):
		"""
		Inicializa una nueva grilla con las dimensiones especificadas.
		
		Parámetros:
			ancho (int): Ancho total de la grilla en píxeles
			alto (int): Alto total de la grilla en píxeles
			tamaño_celda (int): Tamaño de cada celda individual en píxeles
			
		La grilla se divide automáticamente en celdas basándose en el tamaño
		especificado, calculando el número de filas y columnas necesarias.
		"""
		# Calcular dimensiones de la grilla en celdas
		self.filas = alto // tamaño_celda
		self.columnas = ancho // tamaño_celda
		self.tamaño_celda = tamaño_celda
		
		# Inicializar matriz de celdas vacías
		self.celdas = [[None for _ in range(self.columnas)] for _ in range(self.filas)]

	def dibujar(self, ventana):
		"""
		Dibuja todas las partículas de la grilla en la ventana especificada.
		
		Parámetros:
			ventana (pygame.Surface): Superficie donde dibujar las partículas
			
		Este método recorre toda la grilla y dibuja cada partícula existente
		como un rectángulo del color correspondiente a la partícula.
		Las celdas vacías (None) no se dibujan.
		
		Algoritmo:
		1. Recorre todas las filas y columnas de la grilla
		2. Para cada celda que contiene una partícula:
		   - Obtiene el color de la partícula
		   - Calcula la posición en píxeles
		   - Dibuja un rectángulo del tamaño de la celda
		"""
		for fila in range(self.filas):
			for columna in range(self.columnas):
				particula = self.celdas[fila][columna]
				if particula is not None:
					# Obtener color de la partícula
					color = particula.color
					
					# Calcular posición en píxeles
					x = columna * self.tamaño_celda
					y = fila * self.tamaño_celda
					
					# Dibujar rectángulo representando la partícula
					pygame.draw.rect(ventana, color, 
								   (x, y, self.tamaño_celda, self.tamaño_celda))

	def agregar_particula(self, fila, columna, tipo_particula):
		"""
		Agrega una nueva partícula en la posición especificada.
		
		Parámetros:
			fila (int): Fila donde colocar la partícula
			columna (int): Columna donde colocar la partícula
			tipo_particula (class): Clase de la partícula a crear
			
		La partícula solo se agrega si:
		1. La posición está dentro de los límites de la grilla
		2. La celda está actualmente vacía
		
		Si se cumplen las condiciones, se crea una nueva instancia
		del tipo de partícula especificado y se coloca en la celda.
		"""
		if (0 <= fila < self.filas and 
			0 <= columna < self.columnas and 
			self.esta_celda_vacia(fila, columna)):
			# Crear nueva instancia de la partícula y colocarla
			self.celdas[fila][columna] = tipo_particula()

	def eliminar_particula(self, fila, columna):
		"""
		Elimina la partícula en la posición especificada.
		
		Parámetros:
			fila (int): Fila de la partícula a eliminar
			columna (int): Columna de la partícula a eliminar
			
		Si la posición está dentro de los límites de la grilla,
		la celda se establece como vacía (None), eliminando
		efectivamente cualquier partícula que estuviera allí.
		"""
		if 0 <= fila < self.filas and 0 <= columna < self.columnas:
			self.celdas[fila][columna] = None

	def esta_celda_vacia(self, fila, columna):
		"""
		Verifica si una celda específica está vacía.
		
		Parámetros:
			fila (int): Fila a verificar
			columna (int): Columna a verificar
			
		Retorna:
			bool: True si la celda está vacía y dentro de límites, False en caso contrario
			
		Una celda se considera vacía si:
		1. Está dentro de los límites de la grilla
		2. Contiene None (no hay partícula)
		
		Las posiciones fuera de los límites se consideran no vacías
		para prevenir que las partículas se muevan fuera de la grilla.
		"""
		if 0 <= fila < self.filas and 0 <= columna < self.columnas:
			return self.celdas[fila][columna] is None
		return False

	def establecer_celda(self, fila, columna, particula):
		"""
		Establece directamente el contenido de una celda.
		
		Parámetros:
			fila (int): Fila donde colocar la partícula
			columna (int): Columna donde colocar la partícula
			particula (Particle): Instancia de partícula a colocar
			
		Este método permite colocar una partícula existente en una celda
		específica, útil para mover partículas entre posiciones.
		Solo opera si la posición está dentro de los límites.
		"""
		if 0 <= fila < self.filas and 0 <= columna < self.columnas:
			self.celdas[fila][columna] = particula

	def obtener_celda(self, fila, columna):
		"""
		Obtiene el contenido de una celda específica.
		
		Parámetros:
			fila (int): Fila a consultar
			columna (int): Columna a consultar
			
		Retorna:
			Particle o None: La partícula en la celda, o None si está vacía o fuera de límites
			
		Este método permite consultar qué hay en una posición específica
		de la grilla. Retorna None tanto para celdas vacías como para
		posiciones fuera de los límites de la grilla.
		"""
		if 0 <= fila < self.filas and 0 <= columna < self.columnas:
			return self.celdas[fila][columna]
		return None

	def limpiar(self):
		"""
		Elimina todas las partículas de la grilla.
		
		Este método recorre toda la grilla y elimina cada partícula,
		dejando todas las celdas vacías (None). Es útil para reiniciar
		la simulación o limpiar el estado actual.
		
		Algoritmo:
		1. Recorre todas las filas y columnas
		2. Llama a eliminar_particula para cada posición
		3. Resultado: grilla completamente vacía
		"""
		for fila in range(self.filas):
			for columna in range(self.columnas):
				self.eliminar_particula(fila, columna)
