# -*- coding: utf-8 -*-
"""
Simulación Principal del Juego de Perlita.

Este módulo contiene la clase Simulacion que actúa como coordinador central
de todos los sistemas del juego. Se encarga de integrar y sincronizar:
- Sistema de mensajes en pantalla
- Sistema de aparición automática de partículas
- Sistema de nivel y drenaje automático
- Manejador de entrada del usuario
- Motor de físicas de partículas

La simulación maneja el ciclo principal de actualización y renderizado,
así como la comunicación entre todos los subsistemas.
"""

import pygame
from grillas import Grilla
from sistema.mensajes import SistemaMensajes
from sistema.aparicion import SistemaAparicion
from sistema.nivel import SistemaNivel
from sistema.input import ManejadorInput
from sistema.fisicas import MotorFisicas
from core.constantes import *

class Simulacion:
    """
    Clase principal que coordina todos los sistemas del juego.
    
    Esta clase actúa como el núcleo central de la simulación, integrando
    todos los subsistemas y manejando el flujo principal de datos entre ellos.
    Se encarga de la inicialización, actualización y renderizado de toda
    la simulación de partículas de perlita.
    
    Sistemas integrados:
    - SistemaMensajes: Manejo de mensajes temporales en pantalla
    - SistemaAparicion: Generación automática de partículas
    - SistemaNivel: Control de nivel de llenado y drenaje
    - ManejadorInput: Procesamiento de entrada del usuario
    - MotorFisicas: Simulación física de partículas
    """
    
    def __init__(self, ancho, alto, tamaño_celda):
        """
        Inicializa la simulación con las dimensiones especificadas.
        
        Parámetros:
            ancho (int): Ancho del área de simulación en píxeles
            alto (int): Alto del área de simulación en píxeles
            tamaño_celda (int): Tamaño de cada celda en píxeles
        """
        # Configuración básica de la grilla
        self.tamaño_celda = tamaño_celda
        self.grilla = Grilla(ancho, alto, tamaño_celda)
        
        # Modo debug (inicialmente desactivado)
        self.debug_mode = False
        
        # Inicializar todos los sistemas del juego
        self.sistema_mensajes = SistemaMensajes()
        self.sistema_aparicion = SistemaAparicion()
        self.sistema_nivel = SistemaNivel()
        self.manejador_entrada = ManejadorInput()
        self.motor_fisicas = MotorFisicas()
        
        # Diccionario de sistemas para fácil acceso desde otros módulos
        self.sistemas = {
            'mensajes': self.sistema_mensajes,
            'aparicion': self.sistema_aparicion,
            'nivel': self.sistema_nivel,
            'input': self.manejador_entrada,
            'fisicas': self.motor_fisicas
        }
    
    def configurar_constantes_nivel(self, tiempo_drenaje, color_linea, ancho_linea):
        """
        Configura las constantes del sistema de nivel.
        
        Parámetros:
            tiempo_drenaje (float): Duración del proceso de drenaje en segundos
            color_linea (tuple): Color RGB de la línea de nivel
            ancho_linea (int): Grosor de la línea de nivel en píxeles
        """
        self.sistema_nivel.configurar_constantes(tiempo_drenaje, color_linea, ancho_linea)
    
    def configurar_desplazamiento_mouse(self, desplazamiento_x, desplazamiento_y):
        """
        Configura el desplazamiento del mouse para el área de juego.
        
        Parámetros:
            desplazamiento_x (int): Desplazamiento horizontal en píxeles
            desplazamiento_y (int): Desplazamiento vertical en píxeles
        """
        self.manejador_entrada.configurar_offset_mouse(desplazamiento_x, desplazamiento_y)
    
    def actualizar(self):
        """
        Actualiza todos los sistemas de la simulación.
        
        Este método ejecuta el ciclo principal de actualización:
        1. Actualiza el sistema de mensajes (siempre activo)
        2. Si no está pausado, actualiza física y sistemas activos
        3. Procesa generación automática de partículas
        4. Actualiza física de partículas existentes
        5. Verifica condiciones de drenaje automático
        """
        # Actualizar sistema de mensajes siempre (incluso si está pausado)
        self.sistema_mensajes.actualizar()
        
        # Si el juego está pausado, no actualizar física ni generación
        if self.manejador_entrada.pausado:
            return
        
        # Actualizar sistema de nivel (procesar drenaje si está activo)
        self.sistema_nivel.actualizar_drenaje(self.grilla)
        
        # Generar partículas automáticamente si está habilitado y en modo perlita
        if (self.sistema_aparicion.habilitado and 
            self.manejador_entrada.modo == "perlita"):
            self._generar_particulas_automaticas()
        
        # Actualizar física de todas las partículas existentes
        self.motor_fisicas.actualizar_particulas(self.grilla)
        
        # Verificar si se debe activar el drenaje automático
        if self.sistema_nivel.modo_activo and not self.sistema_nivel.esta_drenando:
            self.sistema_nivel.verificar_nivel_lleno(self.grilla)
    
    def _generar_particulas_automaticas(self):
        """
        Genera partículas automáticamente según la configuración actual.
        
        Este método privado calcula cuántas partículas generar basándose
        en la velocidad de aparición configurada y las coloca en posiciones
        aleatorias dentro del área de aparición definida.
        
        Algoritmo:
        1. Calcula número de apariciones basado en velocidad y tiempo
        2. Para cada aparición, determina posición aleatoria
        3. Genera cluster de partículas según intensidad configurada
        """
        numero_apariciones = self.sistema_aparicion.calcular_apariciones()
        
        for _ in range(numero_apariciones):
            # Calcular posición aleatoria dentro del área de aparición
            columna = self.sistema_aparicion.calcular_posicion(self.grilla.columnas)
            fila = 0  # Las partículas siempre aparecen en la fila superior
            
            # Agregar cluster de perlita según el tamaño de intensidad configurado
            self.motor_fisicas.agregar_cluster_perlita(
                self.grilla, fila, columna, 
                self.sistema_aparicion.tamaño_cluster
            )
    
    def manejar_controles_con_eventos(self, eventos):
        """
        Maneja controles del usuario con eventos proporcionados externamente.
        
        Parámetros:
            eventos (list): Lista de eventos de pygame a procesar
        """
        self.manejador_entrada.procesar_eventos(eventos, self.sistemas, self)
    
    def aplicar_pincel(self, fila, columna, modo_pincel):
        """
        Aplica el pincel del usuario en la posición especificada.
        
        Parámetros:
            fila (int): Fila donde aplicar el pincel
            columna (int): Columna donde aplicar el pincel
            modo_pincel (str): Modo del pincel ("perlita", "roca", "borrador")
        """
        self.motor_fisicas.aplicar_pincel(
            self.grilla, fila, columna, modo_pincel, 
            self.manejador_entrada.tamaño_pincel
        )
    
    def reiniciar(self):
        """
        Reinicia la simulación a su estado inicial.
        
        Limpia todas las partículas de la grilla y resetea el estado
        del sistema de drenaje si estaba activo.
        """
        self.grilla.limpiar()
        # Resetear estado de drenaje si estaba activo
        self.sistema_nivel.esta_drenando = False
        self.sistema_nivel.timer_mensaje_drenaje = 0
    
    def cambiar_tamaño_grano(self, nuevo_tamaño):
        """
        Cambia el tamaño visual de los granos de perlita.
        
        Este método permite cambiar dinámicamente el tamaño de visualización
        de las partículas, manteniendo la simulación activa y escalando
        las partículas existentes proporcionalmente.
        
        Parámetros:
            nuevo_tamaño (int): Nuevo tamaño en píxeles para cada celda
            
        Algoritmo:
        1. Calcula nuevas dimensiones de grilla basadas en área constante
        2. Guarda posiciones actuales de partículas
        3. Escala posiciones proporcionalmente
        4. Crea nueva grilla con nuevo tamaño
        5. Restaura partículas en posiciones escaladas
        """
        tamaño_anterior = self.tamaño_celda
        self.tamaño_celda = nuevo_tamaño
        
        # Calcular dimensiones que resulten en un área de juego similar
        columnas_objetivo = ANCHO_AREA_JUEGO // nuevo_tamaño
        filas_objetivo = ALTO_AREA_JUEGO // nuevo_tamaño
        
        # Calcular las dimensiones reales que usará la nueva grilla
        ancho_ventana = columnas_objetivo * nuevo_tamaño
        alto_ventana = filas_objetivo * nuevo_tamaño
        
        # Guardar las partículas actuales con escalado apropiado
        particulas_guardadas = []
        if hasattr(self.grilla, 'filas') and hasattr(self.grilla, 'columnas'):
            # Calcular factores de escala para mantener proporciones
            factor_escala_x = columnas_objetivo / self.grilla.columnas
            factor_escala_y = filas_objetivo / self.grilla.filas
            
            # Recorrer todas las celdas y guardar partículas existentes
            for fila in range(self.grilla.filas):
                for columna in range(self.grilla.columnas):
                    particula = self.grilla.obtener_celda(fila, columna)
                    if particula is not None:
                        # Escalar posición para mantener proporción relativa
                        nueva_fila = int(fila * factor_escala_y)
                        nueva_columna = int(columna * factor_escala_x)
                        particulas_guardadas.append((nueva_fila, nueva_columna, type(particula)))
        
        # Crear nueva grilla con dimensiones calculadas
        self.grilla = Grilla(ancho_ventana, alto_ventana, self.tamaño_celda)
        
        # Restaurar partículas en sus nuevas posiciones escaladas
        for nueva_fila, nueva_columna, tipo_particula in particulas_guardadas:
            if (0 <= nueva_fila < self.grilla.filas and 0 <= nueva_columna < self.grilla.columnas):
                self.grilla.agregar_particula(nueva_fila, nueva_columna, tipo_particula)
    
    def dibujar(self, superficie):
        """
        Dibuja toda la simulación en la superficie especificada.
        
        Parámetros:
            superficie (pygame.Surface): Superficie donde dibujar la simulación
            
        Elementos dibujados:
        1. Grilla y todas las partículas
        2. Indicador visual del pincel del usuario
        3. Línea de nivel (si está activada)
        """
        # Dibujar grilla base y todas las partículas
        self.grilla.dibujar(superficie)
        
        # Dibujar indicador visual del pincel
        self._dibujar_pincel(superficie)
        
        # Dibujar línea de nivel si el modo está activado
        if self.sistema_nivel.modo_activo:
            self._dibujar_linea_nivel(superficie)
    
    def _dibujar_pincel(self, superficie):
        """
        Dibuja el indicador visual del pincel para mostrar dónde se va a dibujar.
        
        Parámetros:
            superficie (pygame.Surface): Superficie donde dibujar el pincel
            
        El pincel se muestra como un rectángulo del color correspondiente
        al modo actual, siguiendo la posición del mouse del usuario.
        """
        posicion_mouse = pygame.mouse.get_pos()
        
        # Ajustar posición considerando el desplazamiento del área de juego
        x_ajustado = posicion_mouse[0] - self.manejador_entrada.offset_mouse_x
        y_ajustado = posicion_mouse[1] - self.manejador_entrada.offset_mouse_y
        
        # Solo dibujar el pincel si está dentro del área de juego
        if (0 <= x_ajustado < self.grilla.columnas * self.tamaño_celda and 
            0 <= y_ajustado < self.grilla.filas * self.tamaño_celda):
            
            # Convertir posición de píxeles a coordenadas de grilla
            columna = x_ajustado // self.tamaño_celda
            fila = y_ajustado // self.tamaño_celda

            # Calcular tamaño visual del pincel
            tamaño_visual_pincel = self.manejador_entrada.tamaño_pincel * self.tamaño_celda
            color_pincel = self.manejador_entrada.obtener_color_pincel()

            # Dibujar el pincel como un rectángulo con relleno completo
            pygame.draw.rect(superficie, color_pincel, 
                           (columna * self.tamaño_celda, fila * self.tamaño_celda, 
                            tamaño_visual_pincel, tamaño_visual_pincel))
    
    def _dibujar_linea_nivel(self, superficie):
        """
        Dibuja la línea indicadora de nivel de llenado.
        
        Parámetros:
            superficie (pygame.Surface): Superficie donde dibujar la línea
            
        La línea se dibuja horizontalmente a través de toda la grilla
        en la posición configurada por el usuario.
        """
        # Obtener posición vertical de la línea en píxeles
        posicion_y_linea = self.sistema_nivel.obtener_posicion_linea_pixeles(
            self.grilla.filas, self.tamaño_celda
        )
        
        # Obtener propiedades visuales de la línea
        ancho_linea = self.sistema_nivel.ancho_linea
        color_linea = self.sistema_nivel.color_linea
        
        # Dibujar línea horizontal que atraviesa toda la grilla
        pygame.draw.rect(superficie, color_linea, 
                        (0, posicion_y_linea - ancho_linea//2, 
                         self.grilla.columnas * self.tamaño_celda, ancho_linea))
    
    def configurar_offset_mouse(self, offset_x, offset_y):
        """Método de compatibilidad para configurar offset del mouse."""
        self.configurar_desplazamiento_mouse(offset_x, offset_y) 