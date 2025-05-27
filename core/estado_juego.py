from core.constantes import EstadosJuego

class ManejadorEstado:
    """Maneja el estado global del juego"""
    
    def __init__(self):
        self.estado_actual = EstadosJuego.SPLASH
        self.estado_anterior = None
        self.tiempo_cambio = 0
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia al nuevo estado"""
        if nuevo_estado != self.estado_actual:
            self.estado_anterior = self.estado_actual
            self.estado_actual = nuevo_estado
            self.tiempo_cambio = 0
    
    def obtener_estado(self):
        """Obtiene el estado actual"""
        return self.estado_actual
    
    def es_estado(self, estado):
        """Verifica si está en el estado especificado"""
        return self.estado_actual == estado
    
    def volver_estado_anterior(self):
        """Vuelve al estado anterior si existe"""
        if self.estado_anterior is not None:
            self.cambiar_estado(self.estado_anterior)
    
    def actualizar_tiempo(self, delta_tiempo):
        """Actualiza el tiempo en el estado actual"""
        self.tiempo_cambio += delta_tiempo
    
    def tiempo_en_estado(self):
        """Retorna el tiempo transcurrido en el estado actual"""
        return self.tiempo_cambio 