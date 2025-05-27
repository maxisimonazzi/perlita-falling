# -*- coding: utf-8 -*-
"""
Sistema de mensajes temporales en pantalla.

Este módulo maneja la visualización de mensajes informativos que aparecen
temporalmente en la pantalla para comunicar al usuario cambios de estado,
configuraciones actuales y eventos importantes del juego.
"""

import time
from core.constantes import DURACION_MENSAJE

class SistemaMensajes:
    """
    Administra los mensajes temporales que se muestran en pantalla.
    
    Esta clase se encarga de mostrar mensajes informativos al usuario
    durante un tiempo determinado, como cambios de modo, configuraciones
    de velocidad, estados del juego, etc.
    
    Atributos:
        mensaje_actual (str): El mensaje que se está mostrando actualmente
        tiempo_mensaje (float): Tiempo restante para mostrar el mensaje
        duracion_mensaje (float): Duración en segundos de cada mensaje
    """
    
    def __init__(self):
        """
        Inicializa el sistema de mensajes.
        
        Configura el estado inicial del sistema con valores por defecto:
        - Sin mensaje activo
        - Temporizador en cero
        - Duración estándar desde constantes
        """
        self.mensaje_actual = ""                    # Texto del mensaje que se muestra actualmente
        self.tiempo_mensaje = 0                     # Contador de tiempo restante para el mensaje
        self.duracion_mensaje = DURACION_MENSAJE    # Duración en segundos de cada mensaje
    
    def mostrar_mensaje(self, mensaje):
        """
        Muestra un nuevo mensaje en pantalla.
        
        Establece un nuevo mensaje para mostrar y reinicia el temporizador.
        Si ya había un mensaje activo, lo reemplaza inmediatamente.
        
        Parámetros:
            mensaje (str): El texto del mensaje a mostrar al usuario
            
        Ejemplo:
            sistema_mensajes.mostrar_mensaje("Velocidad: 5.0")
        """
        self.mensaje_actual = mensaje              # Establece el nuevo mensaje
        self.tiempo_mensaje = self.duracion_mensaje  # Reinicia el temporizador
    
    def actualizar(self, tiempo_delta=1/60.0):
        """
        Actualiza el temporizador del mensaje actual.
        
        Decrementa el tiempo restante del mensaje y lo elimina cuando
        el tiempo expira. Este método debe llamarse en cada frame.
        
        Parámetros:
            tiempo_delta (float): Tiempo transcurrido desde la última actualización
                                en segundos (por defecto 1/60 para 60 FPS)
                                
        Funcionamiento:
            1. Si hay un mensaje activo, reduce el tiempo restante
            2. Si el tiempo llega a cero o menos, elimina el mensaje
            3. Si no hay mensaje, no hace nada
        """
        if self.tiempo_mensaje > 0:                # Solo procesar si hay mensaje activo
            self.tiempo_mensaje -= tiempo_delta    # Reducir tiempo restante
            if self.tiempo_mensaje <= 0:           # Si el tiempo expiró
                self.mensaje_actual = ""           # Eliminar el mensaje
    
    def tiene_mensaje(self):
        """
        Verifica si hay un mensaje activo para mostrar.
        
        Retorna:
            bool: True si hay un mensaje activo, False en caso contrario
            
        Uso:
            Útil para que los renderizadores sepan si deben dibujar
            un mensaje en pantalla.
        """
        return self.mensaje_actual != ""
    
    def obtener_mensaje(self):
        """
        Obtiene el texto del mensaje actual.
        
        Retorna:
            str: El texto del mensaje actual, o cadena vacía si no hay mensaje
            
        Uso:
            Los renderizadores usan este método para obtener el texto
            que deben dibujar en pantalla.
        """
        return self.mensaje_actual
    
    def limpiar(self):
        """
        Elimina inmediatamente el mensaje actual.
        
        Borra el mensaje activo sin esperar a que expire el temporizador.
        Útil para limpiar la pantalla de mensajes cuando sea necesario.
        
        Efectos:
            - El mensaje actual se convierte en cadena vacía
            - El temporizador se reinicia a cero
        """
        self.mensaje_actual = ""    # Eliminar mensaje
        self.tiempo_mensaje = 0     # Reiniciar temporizador 