import pygame
from core.constantes import *

class RenderizadorJuego:
    """Renderizador para la pantalla de juego"""
    
    def __init__(self):
        # Fuentes estilo 8-bit
        self.font_large = pygame.font.Font(None, 96)
        self.font_medium = pygame.font.Font(None, 64)
        self.font_small = pygame.font.Font(None, 40)
        self.font_tiny = pygame.font.Font(None, 28)
    
    def dibujar(self, screen, simulacion, ancho_borde, color_borde):
        """Dibuja la pantalla de juego completa"""
        screen.fill(NEGRO)
        
        # Calcular dimensiones y posición
        ancho_pantalla = screen.get_width()
        alto_pantalla = screen.get_height()
        
        ancho_juego_real = simulacion.grilla.columnas * simulacion.tamaño_celda
        alto_juego_real = simulacion.grilla.filas * simulacion.tamaño_celda
        
        ancho_total = ancho_juego_real + 2 * ancho_borde
        alto_total = alto_juego_real + 2 * ancho_borde
        centrado_x = (ancho_pantalla - ancho_total) // 2
        centrado_y = (alto_pantalla - alto_total) // 2
        
        # Dibujar borde verde
        borde_remarcado_exterior = pygame.Rect(centrado_x, centrado_y, ancho_total, alto_total)
        pygame.draw.rect(screen, color_borde, borde_remarcado_exterior)
        
        # Área de juego
        area_juego_x = centrado_x + ancho_borde
        area_juego_y = centrado_y + ancho_borde
        area_juego = pygame.Rect(area_juego_x, area_juego_y, ancho_juego_real, alto_juego_real)
        pygame.draw.rect(screen, GRIS, area_juego)
        
        # Crear superficie temporal para el juego
        superficie_juego = pygame.Surface((ancho_juego_real, alto_juego_real))
        superficie_juego.fill(GRIS)
        
        # Dibujar simulación
        simulacion.dibujar(superficie_juego)
        
        # Transferir al screen
        screen.blit(superficie_juego, (area_juego_x, area_juego_y))
        
        # Dibujar mensajes especiales
        self._dibujar_mensaje_drenaje(screen, simulacion, centrado_x, centrado_y, ancho_total)
        self._dibujar_mensaje_estado(screen, simulacion, centrado_x, centrado_y, ancho_total, alto_total)
        
        # Dibujar instrucciones
        self._dibujar_instrucciones(screen, centrado_x, centrado_y, ancho_total)
        
    def _dibujar_mensaje_drenaje(self, screen, simulacion, centrado_x, centrado_y, ancho_total):
        """Dibuja el mensaje 'ABRIENDO COMPUERTAS'"""
        if simulacion.sistema_nivel.esta_drenando and simulacion.sistema_nivel.timer_mensaje_drenaje > 0:
            font = pygame.font.Font(None, 48)
            text = font.render("ABRIENDO COMPUERTAS", True, (255, 255, 0))
            
            text_rect = text.get_rect(center=(
                centrado_x + ancho_total // 2,
                centrado_y - 30
            ))
            
            # Fondo semi-transparente
            overlay = pygame.Surface((text_rect.width + 40, text_rect.height + 20))
            overlay.set_alpha(200)
            overlay.fill((255, 0, 0))
            screen.blit(overlay, (text_rect.x - 20, text_rect.y - 10))
            
            # Borde
            pygame.draw.rect(screen, BLANCO, 
                           (text_rect.x - 20, text_rect.y - 10, 
                            text_rect.width + 40, text_rect.height + 20), 3)
            
            screen.blit(text, text_rect)
    
    def _dibujar_mensaje_estado(self, screen, simulacion, centrado_x, centrado_y, ancho_total, alto_total):
        """Dibuja mensajes de estado debajo del campo"""
        if simulacion.sistema_mensajes.obtener_mensaje():
            font = pygame.font.Font(None, 32)
            text = font.render(simulacion.sistema_mensajes.obtener_mensaje(), True, (255, 0, 0))
            
            text_rect = text.get_rect(center=(
                centrado_x + ancho_total // 2,
                centrado_y + alto_total + 30
            ))
            
            screen.blit(text, text_rect)
    
    def _dibujar_instrucciones(self, screen, centrado_x, centrado_y, ancho_total):
        """Dibuja las instrucciones a los lados"""
        # Instrucciones izquierda
        instrucciones_izquierda = [
            "FLECHAS:",
            "",
            "Control de aparicion de granos",
            "ARRIBA - Mas velocidad de aparicion",
            "ABAJO - Menos velocidad de aparicion", 
            "IZQ - Encojer area de caida",
            "DER - Ampliar area de caida",
            "",
            "MODOS:",
            "",
            "P - Modo Perlita",
            "R - Modo Roca",
            "E - Modo Borrador",
            "A - Aparicion On/Off",
            "",
            "MECANICAS:",
            "",
            "O - Pausar/Reanudar",
            "L - Linea de nivel",
            "D - Debug"
        ]
        
        izquierda_x = 50
        izquierda_start_y = centrado_y + 50
        
        for i, instruccion in enumerate(instrucciones_izquierda):
            if instruccion in ["FLECHAS:", "MODOS:", "MECANICAS:"]:
                color = COLOR_PERLIA
                font = self.font_small
            elif instruccion == "":
                continue
            else:
                color = PERLITA_CLARA
                font = self.font_tiny
            
            text = font.render(instruccion, True, color)
            screen.blit(text, (izquierda_x, izquierda_start_y + i * 22))
        
        # Instrucciones derecha
        instrucciones_derecha = [
            "TAMANO VISUAL:",
            "",
            "Teclas 1 a 9",
            "(tamaño de particula)",
            "",
            "1 - Muy fino",
            "5 - Normal",
            "9 - Muy grueso",
            "",
            "INTENSIDAD:",
            "",
            "PgUp     - Mas particulas",
            "PgDn     - Menos particulas",
            "",
            "NIVEL:",
            "",
            "INICIO   - Subir linea",
            "FIN      - Bajar linea",
            "",
            "OTROS:",
            "",
            "ESC      - Menu",
            "SPACE    - Limpiar"
        ]
        
        derecha_x = centrado_x + ancho_total + 50
        derecha_start_y = centrado_y + 50
        
        for i, instruccion in enumerate(instrucciones_derecha):
            if instruccion in ["TAMANO VISUAL:", "INTENSIDAD:", "NIVEL:", "OTROS:"]:
                color = COLOR_PERLIA
                font = self.font_small
            elif instruccion == "":
                continue
            else:
                color = PERLITA_CLARA
                font = self.font_tiny
            
            text = font.render(instruccion, True, color)
            screen.blit(text, (derecha_x, derecha_start_y + i * 22)) 