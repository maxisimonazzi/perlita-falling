# -*- coding: utf-8 -*-
"""
Simulador Principal de Partículas de Perlita.

Este módulo contiene la clase PerlitaSimulator que implementa la interfaz
principal del juego, incluyendo el manejo de pantallas, eventos del usuario,
renderizado y la integración con el sistema de simulación de partículas.

La aplicación maneja múltiples estados:
- Pantalla de presentación con logo de la empresa
- Menú principal
- Simulación interactiva de partículas de perlita

Características principales:
- Interfaz gráfica completa con pygame
- Cursor personalizado estilo 8-bit
- Ventana redimensionable con contenido centrado
- Integración completa con sistema de simulación
- Manejo de eventos y controles del usuario
"""

import pygame
import sys
import time
from simulacion import Simulacion
from ui.hud import HUD
from ui.render_menu import RenderizadorMenu
from ui.render_juego import RenderizadorJuego
from core.constantes import *

class PerlitaSimulator:
    """
    Simulador principal de partículas de perlita.
    
    Esta clase implementa la aplicación completa del simulador, manejando
    todos los aspectos de la interfaz de usuario, renderizado, eventos
    y coordinación con el sistema de simulación de partículas.
    
    La clase maneja tres estados principales:
    1. PRESENTACION: Pantalla de inicio con logo de empresa
    2. MENU: Menú principal de navegación
    3. JUEGO: Simulación interactiva de partículas
    
    Características implementadas:
    - Ventana redimensionable con contenido centrado
    - Cursor personalizado dibujado estilo 8-bit
    - Interfaz de usuario completa con instrucciones
    - Integración con sistema de debug y HUD
    - Manejo de eventos de teclado y mouse
    - Renderizado optimizado con superficies separadas
    
    Atributos principales:
        screen (pygame.Surface): Superficie principal de la ventana
        simulacion (Simulacion): Instancia del motor de simulación
        hud (HUD): Sistema de interfaz de usuario
        estado (EstadosJuego): Estado actual de la aplicación
        ancho_pantalla (int): Ancho actual de la ventana
        alto_pantalla (int): Alto actual de la ventana
    """
    
    def __init__(self):
        """
        Inicializa el simulador principal.
        
        Configura pygame, crea la ventana redimensionable, inicializa
        todos los sistemas gráficos, define la paleta de colores
        estilo 8-bit y prepara el estado inicial de la aplicación.
        
        Proceso de inicialización:
        1. Inicialización de pygame y configuración de ventana
        2. Configuración del área de juego con constantes
        3. Definición de paleta de colores estilo perlita
        4. Carga de fuentes pixeladas para interfaz
        5. Inicialización de sistemas (HUD, estado, reloj)
        6. Configuración de cursor personalizado
        """
        pygame.init()
        
        # Configuración de ventana redimensionable (no pantalla completa)
        self.screen_info = pygame.display.Info()
        # Comenzar con un tamaño inicial cómodo
        self.ancho_inicial = min(ANCHO_VENTANA_INICIAL, self.screen_info.current_w - MARGEN_PANTALLA)
        self.alto_inicial = min(ALTO_VENTANA_INICIAL, self.screen_info.current_h - MARGEN_PANTALLA)
        
        # Crear ventana redimensionable
        self.screen = pygame.display.set_mode(
            (self.ancho_inicial, self.alto_inicial), 
            pygame.RESIZABLE
        )
        pygame.display.set_caption(TITULO_VENTANA)
        pygame.mouse.set_visible(False)  # Ocultamos cursor del sistema para dibujar uno personalizado
        
        # Configuración del área de juego usando constantes (tamaño fijo)
        self.ancho_juego = ANCHO_AREA_JUEGO
        self.alto_juego = ALTO_AREA_JUEGO
        self.tamaño_celda = TAMANO_CELDA_INICIAL
        # Border constants are used directly from constantes.py
        
        # Variables de pantalla (se actualizarán con redimensionamiento)
        self.ancho_pantalla = self.ancho_inicial
        self.alto_pantalla = self.alto_inicial
               
        # Las fuentes ahora se manejan en los renderizadores específicos
        
        # Estado del juego
        self.estado = EstadosJuego.PRESENTACION
        self.tiempo_splash = time.time()
        
        # HUD para información debug
        self.hud = HUD()
        
        # Renderizador de menús
        self.renderizador_menu = RenderizadorMenu()
        
        # Renderizador de juego
        self.renderizador_juego = RenderizadorJuego()
        
        # Clock
        self.clock = pygame.time.Clock()
        
    def run(self):
        """
        Ejecuta el bucle principal de la aplicación.
        
        Implementa la máquina de estados principal que maneja
        la transición entre pantalla de presentación, menú
        y simulación. Mantiene la aplicación corriendo hasta
        que el usuario decide salir.
        
        Estados manejados:
        - PRESENTACION: Pantalla inicial con logo
        - MENU: Menú principal de navegación  
        - JUEGO: Simulación interactiva
        
        El bucle se ejecuta a la velocidad configurada para suavidad visual
        y termina cuando el usuario cierra la aplicación.
        """
        corriendo = True
        while corriendo:
            if self.estado == EstadosJuego.PRESENTACION:
                corriendo = self.manejar_splash()
            elif self.estado == EstadosJuego.MENU:
                corriendo = self.manejar_menu()
            elif self.estado == EstadosJuego.JUEGO:
                corriendo = self.manejar_juego()
            
            self.clock.tick(FRAMES_POR_SEGUNDO)
        
        pygame.quit()
        sys.exit()
    
    def manejar_splash(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.VIDEORESIZE:
                self.manejar_redimensionar(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    self.estado = EstadosJuego.MENU
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.estado = EstadosJuego.MENU
        
        # Salir del splash después del tiempo configurado
        if time.time() - self.tiempo_splash > TIEMPO_PRESENTACION:
            self.estado = EstadosJuego.MENU
        
        self.renderizador_menu.dibujar_splash(self.screen)
        # Dibujar cursor personalizado
        self.dibujar_cursor_personalizado()
        pygame.display.flip()
        return True
    
    def manejar_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.VIDEORESIZE:
                self.manejar_redimensionar(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_RETURN:
                    self.iniciar_juego()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.boton_comenzar_click(mouse_pos):
                    self.iniciar_juego()
        
        self.boton_comenzar_rect = self.renderizador_menu.dibujar_menu(self.screen)
        # Dibujar cursor personalizado
        self.dibujar_cursor_personalizado()
        pygame.display.flip()
        return True
    
    def manejar_juego(self):
        # ARREGLADO: Pasar todos los eventos a la simulación
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.VIDEORESIZE:
                self.manejar_redimensionar(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.estado = EstadosJuego.MENU
                    return True
        
        # Procesar eventos en la simulación con todos los eventos
        self.simulacion.manejar_controles_con_eventos(events)
        self.simulacion.actualizar()
        
        # Usar el renderizador de juego
        self.renderizador_juego.dibujar(self.screen, self.simulacion, ANCHO_BORDE, COLOR_BORDE)
        
        # Dibujar información de debug si está activada
        self.hud.dibujar_info_debug(self.screen, self.simulacion)
        
        # Dibujar cursor personalizado (SOLO fuera del área de juego)
        self.dibujar_cursor_personalizado_juego()
        
        pygame.display.flip()
        return True
    
    def manejar_redimensionar(self, event):
        """
        Maneja eventos de redimensionamiento de la ventana.
        
        Procesa eventos de cambio de tamaño de ventana y actualiza
        todos los sistemas necesarios para mantener la funcionalidad
        y apariencia correcta de la aplicación.
        
        Parámetros:
            event (pygame.event.Event): Evento VIDEORESIZE de pygame
                que contiene las nuevas dimensiones (.w y .h)
        
        Proceso de redimensionamiento:
        1. Actualiza variables internas de dimensiones de pantalla
        2. Reconfigura la superficie de pygame con nuevas dimensiones
        3. Actualiza offset del mouse si hay simulación activa
        
        El redimensionamiento afecta:
        - Posición centrada del área de juego
        - Coordenadas de interacción del mouse
        - Posición de elementos de interfaz
        - Distribución de instrucciones laterales
        
        La funcionalidad se mantiene completamente tras el redimensionamiento.
        """
        self.ancho_pantalla = event.w
        self.alto_pantalla = event.h
        self.screen = pygame.display.set_mode((self.ancho_pantalla, self.alto_pantalla), pygame.RESIZABLE)
        
        # Si estamos en juego, actualizar el offset del mouse
        if self.simulacion is not None:
            self.actualizar_offset_mouse()

    def actualizar_offset_mouse(self):
        """
        Actualiza el offset del mouse para mantener precisión al redimensionar.
        
        Recalcula y actualiza las coordenadas de desplazamiento del mouse
        para que las interacciones del usuario en el área de juego sigan
        siendo precisas después de redimensionar la ventana.
        
        Algoritmo de cálculo:
        1. Obtiene dimensiones reales de la grilla de simulación
        2. Calcula el área total incluyendo bordes
        3. Determina la posición centrada en la ventana actual
        4. Configura el offset en la simulación
        
        El offset es necesario porque:
        - El área de juego está centrada en la ventana
        - La ventana es redimensionable por el usuario
        - Las coordenadas del mouse son relativas a la ventana completa
        - La simulación necesita coordenadas relativas al área de juego
        
        Sin este offset, las interacciones del mouse estarían desalineadas
        con la posición visual de los elementos en pantalla.
        """
        if self.simulacion is not None:
            # Calcular dimensiones reales de la grilla
            ancho_juego_real = self.simulacion.grilla.columnas * self.simulacion.tamaño_celda
            alto_juego_real = self.simulacion.grilla.filas * self.simulacion.tamaño_celda
            
            # Calcular nueva posición centrada
            ancho_total = ancho_juego_real + 2 * ANCHO_BORDE
            alto_total = alto_juego_real + 2 * ANCHO_BORDE
            centrado_x = (self.ancho_pantalla - ancho_total) // 2
            centrado_y = (self.alto_pantalla - alto_total) // 2
            
            # Actualizar offset del mouse
            offset_x = centrado_x + ANCHO_BORDE
            offset_y = centrado_y + ANCHO_BORDE
            self.simulacion.configurar_offset_mouse(offset_x, offset_y)

    def iniciar_juego(self):
        """
        Inicializa y comienza una nueva sesión de simulación.
        
        Este método configura todos los componentes necesarios para
        ejecutar la simulación de partículas, incluyendo la creación
        de la instancia de simulación, configuración de constantes
        del sistema y preparación de la interfaz de juego.
        
        Proceso de inicialización:
        1. Crea nueva instancia de Simulacion con dimensiones configuradas
        2. Configura constantes del sistema de nivel y drenaje
        3. Actualiza offset del mouse para área de juego centrada
        4. Cambia el estado de la aplicación a JUEGO
        
        La simulación se crea con:
        - Ancho y alto del área de juego (constantes)
        - Tamaño de celda configurable por el usuario
        - Sistemas integrados (física, aparición, nivel, entrada)
        """
        # Inicializar simulación con tamaño de celda configurado
        self.simulacion = Simulacion(self.ancho_juego, self.alto_juego, self.tamaño_celda)
        
        # Configurar constantes del sistema de nivel
        self.simulacion.configurar_constantes_nivel(
            TIEMPO_DRENAJE_SEGUNDOS, 
            COLOR_LINEA_NIVEL, 
            ANCHO_LINEA_NIVEL
        )
        
        # Configurar offset del mouse para el área de juego centrada
        self.actualizar_offset_mouse()
        self.estado = EstadosJuego.JUEGO
    
    def dibujar_cursor_personalizado(self):
        """
        Dibuja cursor personalizado estilo 8-bit para menús y splash.
        
        Renderiza un cursor pixelado personalizado siguiendo la estética
        8-bit del juego.

        El cursor se dibuja píxel por píxel en la posición actual
        del mouse del sistema.
        
        Características del cursor:
        - Diseño de puntero clásico pixelado (12x19 píxeles base)
        - Escalado x2 para mejor visibilidad
        - Renderizado directo sobre la pantalla
        
        Colores utilizados:
        - color_base: Marrón rocoso (150, 75, 50)
        - color_borde: Borde oscuro (60, 30, 20)
        - color_resaltado: Highlight naranja/fuego (255, 150, 100)
        
        El patrón del cursor está definido como una matriz 2D donde
        cada número representa un tipo de píxel diferente, permitiendo
        un control preciso sobre la apariencia final.
        """
        mouse_pos = pygame.mouse.get_pos()
        
        # Colores del cursor estilo roca y fuego (8-bit)
        color_base = (150, 75, 50)         # Color marrón rocoso
        color_borde = (60, 30, 20)         # Borde más oscuro
        color_resaltado = (255, 150, 100)  # Highlight naranja/fuego
        
        # Patrón del cursor estilo puntero pixelado (12x19 píxeles)
        cursor_patron = [
            [1],
            [1,1],
            [1,2,1],
            [1,2,2,1],
            [1,2,2,2,1],
            [1,2,1,2,2,1],
            [1,2,2,2,2,2,1],
            [1,2,2,1,2,1,2,1],
            [1,2,1,1,2,2,2,1,1],
            [1,2,2,2,2,1,1,1,1,1],
            [1,2,2,1,2,2,1],
            [1,2,1,0,1,2,2,1],
            [1,1,0,0,1,2,2,1],
            [1,0,0,0,0,1,2,2,1],
            [0,0,0,0,0,1,2,2,1],
            [0,0,0,0,0,0,1,2,1],
            [0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,1]
        ]
        
        # Escala del cursor
        escala = 2
        
        # Dibujar el cursor píxel por píxel
        for y, fila in enumerate(cursor_patron):
            for x, pixel in enumerate(fila):
                if pixel > 0:  # Solo dibujar píxeles no transparentes
                    pixel_x = mouse_pos[0] + x * escala
                    pixel_y = mouse_pos[1] + y * escala
                    
                    # Elegir color según el valor del píxel
                    if pixel == 1:
                        color = color_borde
                    elif pixel == 2:
                        color = color_base
                    else:
                        color = color_resaltado
                    
                    # Dibujar píxel escalado
                    pygame.draw.rect(self.screen, color, 
                                   (pixel_x, pixel_y, escala, escala))
    
    def dibujar_cursor_personalizado_juego(self):
        """
        Dibuja cursor personalizado exclusivamente fuera del área de juego.
        
        Esta función implementa la lógica específica para mostrar el cursor
        personalizado solo cuando el mouse está fuera del área de simulación,
        preservando el sistema de pincel cuadrado dentro del área de juego.
        
        Algoritmo de funcionamiento:
        1. Obtiene la posición actual del mouse
        2. Calcula las dimensiones y posición del área de juego
        3. Verifica si el mouse está dentro del área de simulación
        4. Solo dibuja el cursor personalizado si está FUERA del área
        
        Propósito:
        - Mantener el cursor personalizado en las áreas de interfaz
        - Preservar el sistema de pincel visual en el área de juego
        - Proporcionar feedback visual consistente al usuario
        
        El área de juego se calcula dinámicamente basándose en:
        - Dimensiones reales de la grilla de simulación
        - Tamaño de celda actual
        - Bordes definidos por constantes
        - Posición centrada en la pantalla
        """
        if self.simulacion is not None:
            mouse_pos = pygame.mouse.get_pos()
            
            # Calcular dimensiones del área de juego
            ancho_juego_real = self.simulacion.grilla.columnas * self.simulacion.tamaño_celda
            alto_juego_real = self.simulacion.grilla.filas * self.simulacion.tamaño_celda
            ancho_total = ancho_juego_real + 2 * ANCHO_BORDE
            alto_total = alto_juego_real + 2 * ANCHO_BORDE
            centrado_x = (self.ancho_pantalla - ancho_total) // 2
            centrado_y = (self.alto_pantalla - alto_total) // 2
            area_juego_x = centrado_x + ANCHO_BORDE
            area_juego_y = centrado_y + ANCHO_BORDE
            
            # Solo dibujar cursor si está FUERA del área de juego
            if not (area_juego_x <= mouse_pos[0] <= area_juego_x + ancho_juego_real and
                    area_juego_y <= mouse_pos[1] <= area_juego_y + alto_juego_real):
                self.dibujar_cursor_personalizado()

    def boton_comenzar_click(self, mouse_pos):
        return hasattr(self, 'boton_comenzar_rect') and self.boton_comenzar_rect.collidepoint(mouse_pos)

if __name__ == "__main__":
    game = PerlitaSimulator()
    game.run()