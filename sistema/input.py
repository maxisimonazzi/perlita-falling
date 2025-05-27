import pygame
import sys

class ManejadorInput:
    """Sistema para manejar la entrada del usuario (teclado y mouse)"""
    
    def __init__(self):
        self.modo = "perlita"
        self.pausado = False
        self.tamaño_pincel = 3
        self.offset_mouse_x = 0
        self.offset_mouse_y = 0
    
    def configurar_offset_mouse(self, offset_x, offset_y):
        """Configura el offset del mouse para el área de juego"""
        self.offset_mouse_x = offset_x
        self.offset_mouse_y = offset_y
    
    def procesar_eventos(self, eventos, sistemas, simulacion):
        """Procesa todos los eventos de entrada"""
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                self._manejar_tecla(evento, sistemas, simulacion)
        
        # Manejar mouse
        self._manejar_mouse(simulacion)
    
    def _manejar_tecla(self, evento, sistemas, simulacion):
        """Maneja las teclas presionadas"""
        # Sistema de mensajes
        mensajes = sistemas['mensajes']
        aparicion = sistemas['aparicion']
        nivel = sistemas['nivel']
        
        if evento.key == pygame.K_SPACE:
            simulacion.reiniciar()
        
        # Cambio de modos
        elif evento.key == pygame.K_p:
            self.modo = "perlita"
            if aparicion.habilitado:
                mensajes.mostrar_mensaje("Modo Perlita - Auto spawn: ON")
            else:
                mensajes.mostrar_mensaje("Modo Perlita - Auto spawn: OFF")
        
        elif evento.key == pygame.K_r:
            self.modo = "roca"
            if aparicion.habilitado:
                mensajes.mostrar_mensaje("Modo Roca - Auto spawn: ON (pausado)")
            else:
                mensajes.mostrar_mensaje("Modo Roca - Auto spawn: OFF")
        
        elif evento.key == pygame.K_b:
            self.modo = "borrador"
            if aparicion.habilitado:
                mensajes.mostrar_mensaje("Modo Borrador - Auto spawn: ON (pausado)")
            else:
                mensajes.mostrar_mensaje("Modo Borrador - Auto spawn: OFF")
        
        # Auto spawn
        elif evento.key == pygame.K_a:
            habilitado = aparicion.alternar_estado()
            if self.modo == "perlita":
                mensajes.mostrar_mensaje(f"Auto spawn: {'ON' if habilitado else 'OFF'}")
            else:
                mensajes.mostrar_mensaje(f"Auto spawn: {'ON (activara en modo perlita)' if habilitado else 'OFF'}")
        
        # Pausa
        elif evento.key == pygame.K_o:
            self.pausado = not self.pausado
            mensajes.mostrar_mensaje(f"Juego: {'PAUSADO' if self.pausado else 'REANUDADO'}")
        
        # Sistema de nivel
        elif evento.key == pygame.K_l:
            activo = nivel.alternar_modo()
            mensajes.mostrar_mensaje(f"Modo nivel: {'ON' if activo else 'OFF'}")
        
        elif evento.key == pygame.K_HOME:
            if nivel.modo_activo:
                posicion = nivel.mover_linea_arriba()
                mensajes.mostrar_mensaje(f"Linea de nivel: {posicion:.2f}")
        
        elif evento.key == pygame.K_END:
            if nivel.modo_activo:
                posicion = nivel.mover_linea_abajo()
                mensajes.mostrar_mensaje(f"Linea de nivel: {posicion:.2f}")
        
        # Controles de aparición
        elif evento.key == pygame.K_UP:
            velocidad = aparicion.aumentar_velocidad()
            mensajes.mostrar_mensaje(f"Velocidad: {velocidad:.1f}")
        
        elif evento.key == pygame.K_DOWN:
            velocidad = aparicion.disminuir_velocidad()
            mensajes.mostrar_mensaje(f"Velocidad: {velocidad:.1f}")
        
        elif evento.key == pygame.K_LEFT:
            ancho = aparicion.disminuir_ancho()
            mensajes.mostrar_mensaje(f"Ancho area: {ancho} columnas")
        
        elif evento.key == pygame.K_RIGHT:
            max_ancho = simulacion.grilla.columnas if hasattr(simulacion.grilla, 'columnas') else 50
            ancho = aparicion.aumentar_ancho(max_ancho)
            if aparicion.esta_en_ancho_completo(simulacion.grilla.columnas):
                mensajes.mostrar_mensaje(f"Ancho area: {ancho} columnas (COMPLETO)")
            else:
                mensajes.mostrar_mensaje(f"Ancho area: {ancho} columnas")
        
        # Controles de cluster
        elif evento.key == pygame.K_PAGEUP:
            tamaño = aparicion.aumentar_cluster()
            mensajes.mostrar_mensaje(f"Intensidad: {tamaño}x{tamaño} particulas")
        
        elif evento.key == pygame.K_PAGEDOWN:
            tamaño = aparicion.disminuir_cluster()
            mensajes.mostrar_mensaje(f"Intensidad: {tamaño}x{tamaño} particulas")
        
        # Controles de tamaño visual (1-9)
        elif evento.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                           pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
            nuevo_tamaño = evento.key - pygame.K_0  # Convertir tecla a número
            simulacion.cambiar_tamaño_grano(nuevo_tamaño)
            mensajes.mostrar_mensaje(f"Tamano visual: {nuevo_tamaño}x{nuevo_tamaño} pixeles")
        
        # Modo debug
        elif evento.key == pygame.K_d:
            simulacion.debug_mode = not simulacion.debug_mode
            mensajes.mostrar_mensaje(f"Modo debug: {'ON' if simulacion.debug_mode else 'OFF'}")
    
    def _manejar_mouse(self, simulacion):
        """Maneja la entrada del mouse"""
        botones = pygame.mouse.get_pressed()
        if botones[0]:  # Click izquierdo
            pos = pygame.mouse.get_pos()
            # Ajustar posición considerando el offset
            x_ajustado = pos[0] - self.offset_mouse_x
            y_ajustado = pos[1] - self.offset_mouse_y
            
            # Verificar que esté dentro del área de juego
            if (0 <= x_ajustado < simulacion.grilla.columnas * simulacion.tamaño_celda and 
                0 <= y_ajustado < simulacion.grilla.filas * simulacion.tamaño_celda):
                fila = y_ajustado // simulacion.tamaño_celda
                columna = x_ajustado // simulacion.tamaño_celda
                
                simulacion.aplicar_pincel(fila, columna, self.modo)
    
    def obtener_color_pincel(self):
        """Obtiene el color del pincel según el modo actual"""
        from core.constantes import COLOR_PERLIA, COLOR_ROCA, COLOR_BORRADOR
        
        if self.modo == "roca":
            return COLOR_ROCA
        elif self.modo == "perlita":
            return COLOR_PERLIA
        elif self.modo == "borrador":
            return COLOR_BORRADOR
        return (255, 255, 255) 