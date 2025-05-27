import pygame
import time
from core.constantes import *

class RenderizadorMenu:
    """Renderizador para las pantallas de splash y menú"""
    
    def __init__(self):
        # Fuentes estilo 8-bit
        self.font_large = pygame.font.Font(None, 96)
        self.font_medium = pygame.font.Font(None, 64)
        self.font_small = pygame.font.Font(None, 40)
        self.font_tiny = pygame.font.Font(None, 28)
    
    def dibujar_splash(self, screen):
        """Dibuja la pantalla de splash"""
        ancho_pantalla = screen.get_width()
        alto_pantalla = screen.get_height()
        
        screen.fill(PERLITA_OSCURA)
        
        # Patrón de fondo pixelado
        for x in range(0, ancho_pantalla, 40):
            for y in range(0, alto_pantalla, 40):
                if (x + y) % 80 == 0:
                    pygame.draw.rect(screen, COLOR_PERLIA, (x, y, 20, 20))
        
        # Cargar y mostrar el logo
        try:
            logo = pygame.image.load("logo_tucumordor.png")
            
            # Escalar el logo
            ancho_maximo = int(ancho_pantalla * 0.6)
            alto_maximo = int(alto_pantalla * 0.6)
            
            ancho_original, alto_original = logo.get_size()
            factor_escalado = min(ancho_maximo / ancho_original, alto_maximo / alto_original)
            
            nuevo_ancho = int(ancho_original * factor_escalado)
            nuevo_alto = int(alto_original * factor_escalado)
            
            logo = pygame.transform.scale(logo, (nuevo_ancho, nuevo_alto))
            logo_rect = logo.get_rect(center=(ancho_pantalla//2, alto_pantalla//2))
            screen.blit(logo, logo_rect)
        except:
            # Respaldo si no se puede cargar el logo
            texto_tucumordor = self.font_large.render("TUCUMORDOR", True, NEGRO)
            tucumordor_rect = texto_tucumordor.get_rect(center=(ancho_pantalla//2, alto_pantalla//2))
            screen.blit(texto_tucumordor, tucumordor_rect)
        
        # Instrucción
        instrucciones_menu = self.font_small.render("Presiona ENTER o haz click para continuar", True, NEGRO)
        instruccion_rect = instrucciones_menu.get_rect(center=(ancho_pantalla//2, alto_pantalla - 80))
        screen.blit(instrucciones_menu, instruccion_rect)
    
    def dibujar_menu(self, screen):
        """Dibuja la pantalla de menú y retorna el rectángulo del botón"""
        ancho_pantalla = screen.get_width()
        alto_pantalla = screen.get_height()
        
        screen.fill(PERLITA_OSCURA)
        
        # Patrón de fondo pixelado
        for x in range(0, ancho_pantalla, 60):
            for y in range(0, alto_pantalla, 60):
                if (x + y) % 120 == 0:
                    pygame.draw.rect(screen, COLOR_PERLIA, (x, y, 30, 30))
        
        # Título principal
        texto_titulo = self.font_medium.render("Simulacion de Acumulacion", True, NEGRO)
        titulo_rect = texto_titulo.get_rect(center=(ancho_pantalla//2, alto_pantalla//4))
        screen.blit(texto_titulo, titulo_rect)
        
        texto_subtitulo = self.font_medium.render("de Particulas de Perlita", True, NEGRO)
        subtitulo_rect = texto_subtitulo.get_rect(center=(ancho_pantalla//2, alto_pantalla//4 + 50))
        screen.blit(texto_subtitulo, subtitulo_rect)
        
        # Botón grande de COMENZAR
        ancho_boton = 450
        alto_boton = 150
        boton_comenzar_rect = pygame.Rect(
            ancho_pantalla//2 - ancho_boton//2, 
            alto_pantalla//2 - alto_boton//2, 
            ancho_boton, 
            alto_boton
        )
        
        # Dibujar botón con estilo 8-bit
        pygame.draw.rect(screen, COLOR_PERLIA, boton_comenzar_rect)
        pygame.draw.rect(screen, PERLITA_CLARA, boton_comenzar_rect, 6)
        
        # Texto del botón
        texto_comenzar = self.font_large.render("COMENZAR", True, NEGRO)
        texto_comenzar_rect = texto_comenzar.get_rect(center=boton_comenzar_rect.center)
        screen.blit(texto_comenzar, texto_comenzar_rect)
        
        return boton_comenzar_rect 