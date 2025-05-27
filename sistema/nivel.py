import time
import random
from core.constantes import TIEMPO_DRENAJE_SEGUNDOS, COLOR_LINEA_NIVEL, ANCHO_LINEA_NIVEL

class SistemaNivel:
    """Sistema para manejar el nivel de llenado y drenaje"""
    
    def __init__(self):
        self.modo_activo = False
        self.posicion_linea = 0.5  # Posición de la línea (0.0 = arriba, 1.0 = abajo)
        self.esta_drenando = False
        self.tiempo_inicio_drenaje = 0
        self.timer_mensaje_drenaje = 0
        
        # Configuración
        self.tiempo_drenaje_segundos = TIEMPO_DRENAJE_SEGUNDOS
        self.color_linea = COLOR_LINEA_NIVEL
        self.ancho_linea = ANCHO_LINEA_NIVEL
    
    def configurar_constantes(self, tiempo_drenaje, color_linea, ancho_linea):
        """Configura las constantes del sistema de nivel"""
        self.tiempo_drenaje_segundos = tiempo_drenaje
        self.color_linea = color_linea
        self.ancho_linea = ancho_linea
    
    def alternar_modo(self):
        """Alterna el modo de nivel activado/desactivado"""
        self.modo_activo = not self.modo_activo
        return self.modo_activo
    
    def mover_linea_arriba(self):
        """Mueve la línea de nivel hacia arriba"""
        if self.modo_activo:
            self.posicion_linea = max(0.1, self.posicion_linea - 0.05)
        return self.posicion_linea
    
    def mover_linea_abajo(self):
        """Mueve la línea de nivel hacia abajo"""
        if self.modo_activo:
            self.posicion_linea = min(0.9, self.posicion_linea + 0.05)
        return self.posicion_linea
    
    def verificar_nivel_lleno(self, grilla):
        """Verifica si el área debajo de la línea está llena de perlita"""
        if not self.modo_activo or self.esta_drenando:
            return False
            
        fila_linea = int(self.posicion_linea * grilla.filas)
        
        # Contar celdas llenas de perlita y celdas disponibles debajo de la línea
        celdas_perlita = 0
        celdas_disponibles = 0  # Celdas que pueden ser ocupadas por perlita (vacías o con rocas)
        
        for fila in range(fila_linea, grilla.filas):
            for col in range(grilla.columnas):
                particula = grilla.obtener_celda(fila, col)
                # Importar aquí para evitar dependencias circulares
                from particulas import ParticulaPerlita
                
                if isinstance(particula, ParticulaPerlita):
                    celdas_perlita += 1
                    celdas_disponibles += 1
                elif particula is None:  # Celda vacía
                    celdas_disponibles += 1
                # Las rocas no cuentan como disponibles ni como perlita
        
        # Si está 95% lleno de perlita (considerando solo espacios disponibles), activar drenaje
        if celdas_disponibles > 0 and (celdas_perlita / celdas_disponibles) >= 0.95:
            self.iniciar_drenaje()
            return True
        return False
    
    def iniciar_drenaje(self):
        """Inicia el proceso de drenaje"""
        self.esta_drenando = True
        self.tiempo_inicio_drenaje = time.time()
        self.timer_mensaje_drenaje = self.tiempo_drenaje_segundos
    
    def actualizar_drenaje(self, grilla):
        """Actualiza el proceso de drenaje"""
        if not self.esta_drenando:
            return
            
        tiempo_actual = time.time()
        transcurrido = tiempo_actual - self.tiempo_inicio_drenaje
        
        # Actualizar timer del mensaje
        self.timer_mensaje_drenaje = max(0, self.tiempo_drenaje_segundos - transcurrido)
        
        if transcurrido >= self.tiempo_drenaje_segundos:
            # Terminar drenaje - limpiar solo perlita que quede debajo de la línea
            fila_linea = int(self.posicion_linea * grilla.filas)
            for fila in range(fila_linea, grilla.filas):
                for col in range(grilla.columnas):
                    particula = grilla.obtener_celda(fila, col)
                    # Importar aquí para evitar dependencias circulares
                    from particulas import ParticulaPerlita
                    
                    # Solo eliminar partículas de perlita, mantener rocas
                    if isinstance(particula, ParticulaPerlita):
                        grilla.eliminar_particula(fila, col)
            
            self.esta_drenando = False
            self.timer_mensaje_drenaje = 0
            return
        
        # Efecto de gravedad - las partículas caen hacia abajo
        fila_linea = int(self.posicion_linea * grilla.filas)
        
        # Calcular velocidad de caída basada en el progreso
        progreso = transcurrido / self.tiempo_drenaje_segundos
        velocidad_caida = max(1, int(progreso * 3))  # Velocidad aumenta con el tiempo
        
        # Hacer que las partículas caigan hacia abajo
        for _ in range(velocidad_caida):
            self._simular_gravedad_drenaje(grilla, fila_linea)
    
    def _simular_gravedad_drenaje(self, grilla, fila_linea):
        """Simula que las partículas de perlita caen por gravedad durante el drenaje"""
        # Procesar desde abajo hacia arriba para simular caída
        for fila in range(grilla.filas - 1, fila_linea - 1, -1):
            for col in range(grilla.columnas):
                particula = grilla.obtener_celda(fila, col)
                # Importar aquí para evitar dependencias circulares
                from particulas import ParticulaPerlita
                
                # Solo procesar partículas de perlita, ignorar rocas
                if isinstance(particula, ParticulaPerlita):
                    # Intentar mover la partícula hacia abajo
                    if fila == grilla.filas - 1:
                        # Si está en la fila inferior, eliminarla (cae fuera del campo)
                        grilla.eliminar_particula(fila, col)
                    elif grilla.obtener_celda(fila + 1, col) is None:
                        # Si hay espacio abajo, mover la partícula
                        grilla.establecer_celda(fila + 1, col, particula)
                        grilla.eliminar_particula(fila, col)
                    else:
                        # Si no puede caer directamente, intentar caer en diagonal
                        direcciones = [-1, 1]  # Izquierda y derecha
                        random.shuffle(direcciones)
                        
                        for direccion in direcciones:
                            nueva_col = col + direccion
                            if (0 <= nueva_col < grilla.columnas and 
                                grilla.obtener_celda(fila + 1, nueva_col) is None):
                                grilla.establecer_celda(fila + 1, nueva_col, particula)
                                grilla.eliminar_particula(fila, col)
                                break
    
    def obtener_posicion_linea_pixeles(self, grilla_fila, tamaño_celda):
        """Obtiene la posición de la línea en píxeles"""
        return int(self.posicion_linea * grilla_fila * tamaño_celda) 