import pygame
from core.constantes import *

class HUD:
    """Elementos de interfaz de usuario adicionales"""
    
    def __init__(self):
        self.font_small = pygame.font.Font(None, 32)
        self.font_tiny = pygame.font.Font(None, 22)
    
    def dibujar_info_debug(self, screen, simulacion):
        """Dibuja información de debug (opcional)"""
        if hasattr(simulacion, 'debug_mode') and simulacion.debug_mode:
            datos_debug = [
                f"FPS: {pygame.time.Clock().get_fps():.1f}",
                f"Partículas: {self._contar_particulas(simulacion.grilla)}",
                f"Velocidad spawn: {simulacion.sistema_aparicion.velocidad:.1f}",
                f"Ancho spawn: {simulacion.sistema_aparicion.ancho_area}",
                f"Cluster: {simulacion.sistema_aparicion.tamaño_cluster}",
                f"Modo: {simulacion.manejador_entrada.modo}",
                f"Pausado: {simulacion.manejador_entrada.pausado}",
                f"Nivel activo: {simulacion.sistema_nivel.modo_activo}",
                f"Drenando: {simulacion.sistema_nivel.esta_drenando}"
            ]
            
            for i, line in enumerate(datos_debug):
                text = self.font_tiny.render(line, True, AMARILLO)
                screen.blit(text, (screen.get_width() - 175, 10 + i * 20))
    
    def _contar_particulas(self, grilla):
        """Cuenta el número total de partículas en la grilla"""
        cuenta = 0
        for fila in range(grilla.filas):
            for col in range(grilla.columnas):
                if grilla.obtener_celda(fila, col) is not None:
                    cuenta += 1
        return cuenta
    
    def dibujar_indicador_modo(self, screen, modo_actual):
        """Dibuja un indicador del modo actual en la esquina"""
        color_modo = {
            "perlita": COLOR_PERLIA,
            "roca": COLOR_ROCA,
            "borrador": COLOR_BORRADOR
        }
        
        nombre_modo = {
            "perlita": "PERLITA",
            "roca": "ROCA", 
            "borrador": "BORRADOR"
        }
        
        color = color_modo.get(modo_actual, BLANCO)
        nombre = nombre_modo.get(modo_actual, "DESCONOCIDO")
        
        # Fondo del indicador
        indicador_rect = pygame.Rect(screen.get_width() - 120, screen.get_height() - 40, 110, 30)
        pygame.draw.rect(screen, color, indicador_rect)
        pygame.draw.rect(screen, NEGRO, indicador_rect, 2)
        
        # Texto del modo
        text = self.font_small.render(nombre, True, NEGRO)
        text_rect = text.get_rect(center=indicador_rect.center)
        screen.blit(text, text_rect) 