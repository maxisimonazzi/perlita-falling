# -*- coding: utf-8 -*-
"""
Motor de Físicas del Simulador de Perlita.

Este módulo contiene la clase MotorFisicas que se encarga de manejar toda la simulación
física de las partículas en el juego. Incluye la actualización de posiciones, detección
de colisiones, aplicación de gravedad y manejo de clusters de partículas.

Funcionalidades principales:
- Actualización de física de partículas con gravedad
- Generación de clusters de partículas de perlita
- Aplicación de herramientas de dibujo (pincel)
- Optimización de rendimiento con procesamiento direccional alternado
"""

from core.constantes import PROBABILIDAD_APARICION_PERLITA

class MotorFisicas:
    """
    Sistema para manejar la física de las partículas.
    
    Esta clase implementa el motor de física que controla el comportamiento
    de todas las partículas en la simulación, incluyendo la gravedad,
    colisiones y interacciones entre partículas.
    """
    
    def __init__(self):
        """
        Inicializa el motor de físicas.
        
        Queda planteado para futuras implementaciones.
        """
        pass
    
    def actualizar_particulas(self, grilla):
        """
        Actualiza todas las partículas en la grilla aplicando física.
        
        Este método procesa todas las partículas de perlita en la grilla,
        aplicando gravedad y detectando colisiones. El procesamiento se
        realiza desde abajo hacia arriba para simular correctamente la
        caída de partículas.
        
        Parámetros:
            grilla: La grilla que contiene las partículas a actualizar
            
        Algoritmo:
            1. Procesa filas desde abajo hacia arriba (gravedad)
            2. Alterna dirección de columnas para evitar sesgos visuales
            3. Actualiza posición de cada partícula de perlita
            4. Mueve partículas a nuevas posiciones si es necesario
        """
        from particulas import ParticulaPerlita
        
        # Actualizar partículas existentes desde abajo hacia arriba para simular gravedad
        for fila in range(grilla.filas - 2, -1, -1):
            # Alternar dirección de procesamiento para evitar sesgos visuales
            if fila % 2 == 0:
                rango_columnas = range(grilla.columnas)
            else:
                rango_columnas = reversed(range(grilla.columnas))

            for columna in rango_columnas:
                particula = grilla.obtener_celda(fila, columna)
                if isinstance(particula, ParticulaPerlita):
                    # Calcular nueva posición basada en física de la partícula
                    nueva_posicion = particula.actualizar(grilla, fila, columna)
                    
                    # Si la partícula se movió, actualizar su posición en la grilla
                    if nueva_posicion != (fila, columna):
                        grilla.establecer_celda(nueva_posicion[0], nueva_posicion[1], particula)
                        grilla.eliminar_particula(fila, columna)
    
    def agregar_particula(self, grilla, fila, columna, tipo_particula, probabilidad=None):
        """
        Agrega una partícula a la grilla en la posición especificada.
        
        Parámetros:
            grilla: La grilla donde agregar la partícula
            fila (int): Fila donde colocar la partícula
            columna (int): Columna donde colocar la partícula
            tipo_particula (str): Tipo de partícula ("perlita" o "roca")
            probabilidad (float, opcional): Probabilidad de aparición para perlita
            
        Nota:
            Para partículas de perlita, se usa probabilidad para simular
            aparición natural. Las rocas siempre se colocan.
        """
        import random
        from particulas import ParticulaPerlita, ParticulaRoca
        
        # Usar probabilidad por defecto si no se especifica
        if probabilidad is None:
            probabilidad = PROBABILIDAD_APARICION_PERLITA
        
        if tipo_particula == "perlita":
            # Las partículas de perlita aparecen con cierta probabilidad
            if random.random() < probabilidad:
                grilla.agregar_particula(fila, columna, ParticulaPerlita)
        elif tipo_particula == "roca":
            # Las rocas siempre se colocan cuando se solicita
            grilla.agregar_particula(fila, columna, ParticulaRoca)
    
    def agregar_cluster_perlita(self, grilla, fila_inicio, columna_inicio, tamaño_cluster):
        """
        Agrega un cluster (grupo) de partículas de perlita del tamaño especificado.
        
        Este método crea un área cuadrada de partículas de perlita, útil para
        la generación automática de partículas o para herramientas de dibujo
        con mayor intensidad.
        
        Parámetros:
            grilla: La grilla donde agregar el cluster
            fila_inicio (int): Fila superior izquierda del cluster
            columna_inicio (int): Columna superior izquierda del cluster
            tamaño_cluster (int): Tamaño del lado del cluster (cuadrado)
            
        Ejemplo:
            Para tamaño_cluster=3, se creará un área de 3x3 partículas
            
        Algoritmo:
            1. Itera sobre el área cuadrada especificada
            2. Verifica límites de la grilla
            3. Solo agrega partículas en celdas vacías
            4. Usa probabilidad estándar para cada partícula
        """
        for desplazamiento_fila in range(tamaño_cluster):
            for desplazamiento_columna in range(tamaño_cluster):
                fila_actual = fila_inicio + desplazamiento_fila
                columna_actual = columna_inicio + desplazamiento_columna
                
                # Verificar que la posición esté dentro de los límites de la grilla
                if (0 <= fila_actual < grilla.filas and 
                    0 <= columna_actual < grilla.columnas and
                    grilla.obtener_celda(fila_actual, columna_actual) is None):
                    # Agregar partícula de perlita en la posición válida
                    self.agregar_particula(grilla, fila_actual, columna_actual, "perlita")
    
    def aplicar_pincel(self, grilla, fila, columna, modo_pincel, tamaño_pincel=3):
        """
        Aplica el pincel en la posición especificada según el modo seleccionado.
        
        Esta función implementa las herramientas de dibujo del usuario,
        permitiendo agregar perlita, rocas o borrar partículas en un área
        determinada por el tamaño del pincel.
        
        Parámetros:
            grilla: La grilla donde aplicar el pincel
            fila (int): Fila central donde aplicar el pincel
            columna (int): Columna central donde aplicar el pincel
            modo_pincel (str): Modo del pincel ("perlita", "roca", "borrador")
            tamaño_pincel (int): Tamaño del área de efecto del pincel
            
        Modos disponibles:
            - "perlita": Agrega partículas de perlita
            - "roca": Agrega partículas de roca
            - "borrador": Borra partículas existentes
            
        Algoritmo:
            1. Itera sobre el área cuadrada del pincel
            2. Para modo "borrador": elimina partículas
            3. Para otros modos: agrega partículas del tipo correspondiente
        """
        for desplazamiento_fila in range(tamaño_pincel):
            for desplazamiento_columna in range(tamaño_pincel):
                fila_actual = fila + desplazamiento_fila
                columna_actual = columna + desplazamiento_columna

                if modo_pincel == "borrador":
                    # Modo borrador: eliminar partículas existentes
                    grilla.eliminar_particula(fila_actual, columna_actual)
                else:
                    # Modos de dibujo: agregar partículas del tipo especificado
                    self.agregar_particula(grilla, fila_actual, columna_actual, modo_pincel) 