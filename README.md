<div align="center">
<h1> 🌟 Perlita Falling 🌟 </h1>
<h1> Simulador de Acumulación de Partículas de Perlita </h1>

<h3>Un simulador de física de partículas desarrollado en Python que simula el comportamiento de caida de partículas de perlita expandida en un contenedor para su posterior empaquetado. Si se habilita el nivel de llenado, el sistema abre las compuertas de drenaje automaticamente cuando el 95% del volumen por debajo del nivel es alcanzado.</h3>

[![Version](https://img.shields.io/badge/Version-1.3-orange?style=for-the-badge&logoSize=auto)]()
[![Python](https://img.shields.io/badge/_-Python-14354C.svg?style=for-the-badge&logo=python&logoColor=white&logoSize=auto)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/_-Pygame-yellow.svg?style=for-the-badge&logo=python&logoColor=white&logoSize=auto)](https://www.python.org/)
[![VSCode](https://img.shields.io/badge/_-Visual_Studio_Code-3776AB.svg?style=for-the-badge&logoSize=auto&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAApdQTFRFAAAAYmJisLCw8fHx+/v76+vruLi4Xl5eaGhoYGBgwcHB9/f3////7OzsvLy8Xl5eZ2dnaGhoX19fysrK+vr67Ozsw8PDY2NjZmZmaWlpx8fH+/v77u7uvr6+XV1d1tbW/Pz85+fnZWVlXFxc3Nzc/v7+ZGRkbW1tZmZmXFxc29vba2trX19fx8fHvb29Xl5eZ2dnY2NjcXFx5+fn3d3d/f394uLidXV1ZmZmdnZ27Ozs8fHx2tra7+/vqKioYWFhY2NjkZGR7e3t4eHheXl5+Pj4xcXFXV1drq6u9PT0yMjIY2NjXV1d3t7e3t7epKSk9fX18vLyqKioXFxcWlpaXFxcZWVl29vb5OTkhYWFW1tbW1tbWlpaX19fysrKzc3NaGhoW1tbXl5eW1tbYmJiW1tbXFxcw8PD8vLyr6+vXFxcYGBgZGRkW1tbv7+/5ubmjo6OW1tbXFxcZGRkWlpa19fX8fHxra2tbGxsaGho2tra+vr6z8/PYGBga2trYmJibm5u5ubm5eXlkpKSYWFhdHR07Ozs9vb28PDwtra2ampq6enpurq6g4OD7u7u+fn5yMjI+fn57+/vm5ubW1tbe3t75ubm4+PjeHh4W1tbyMjI3d3deXl5WlpaXFxca2tr39/f7u7umJiYurq6w8PDYWFhWlpaW1tbZWVl29vb+fn5XFxclZWVk5OTXFxcW1tby8vLampqXV1dW1tbW1tbZ2dnXV1dxMTEwsLCW1tbsbGx+fn539/fW1tbXFxcqKio+fn52trak5OTZmZmW1tboaGh9PT01tbWlZWVXFxcWlpaZWVlWlpaj4+P7u7u2NjYkpKSXFxcW1tbYGBgX19fWlpahoaG3Nzc9PT01NTUjIyMW1tbW1tbmAVlHQAAAN10Uk5TAAZP7P/TYwkDBlr4/9xvCgMBBm7643gLAwGI/edKCpL/7AIKqP8BAQIMwAEHYGMIAQITyJv/tRgEJdjxs946BQQt5NFf9m4IOuijOTbNq1/y+HQnFygywdlPHyQTLrevNhkHJQQQKqb+fSkHAw+Q41chDQQYsfNmAwLA/5cLAgITyMkgByXW/u1JAeCWX+T9iv/sZSNE3b4hJpTKRR0LPNTmXIacMRYVNsP6IlNTEBO4AgkREgIqp48Ogv7eCyN1+dFHASBj9ctpLBUBHlrxwWEtGwQIG0/b/7lbGgzKgUBXAAAB6UlEQVR4nGNkwAIYoeAHiI1FnhMoB1X2AYsCQahWqEoMBZLvhBk/wnkCGAoEeRkZ3yDxRdEUKAHNfI7qYAYGNcabMJ4GI+MjdB9pgz10AcwxZESohSvgV2W8rsX4+h6QbcHIeAkmrn8RpsDm5XOw1oMMDoyMp2Dy5ownYApYOECUJSPjaTPGwzB5O0bGAzAFvvsh3tdkZNwDFXMFuWo7TEEY41YISwTmfR9GxvP3QjbCFMQwMq5DcXYwI+M5RiPGlTAFKUDj9iHCBqj+0+ODDNk/4AoYchj/skzjgHKTgcqXvWBgyP4At4KBoZiRcQPMiCzGb9wdDKgKKjcETkK4IB9oRBMDshX1jIzdKI4sY3w4h6HlPlxBK2MbhFXdChWqYWxoXKQPt6K7EUz/6GBkrIOKNTOWa+jAFUysBlFtjIfsGRnLYNZ0MzIWwxTMmn2dgaEf6LSVvN6MOTAVUxmzYAqSHW6sAjq07QqDfQYjYzJMxbwkmIIiYESuC550AMgutlkXHMOABhg3Ak2PXuYN5qT4MzPmPUdTAEyTXBdgvPp3z1Iz3qArQAYaE1eFMwYiCWxAzxcaU4FW+sC5WzFz1uHbaoyMbhD2bmxZj+F08DpGRjtgIlwFlF2QiCV3Cx6GZP73Qowda98DABMQd5ryIFUHAAAAAElFTkSuQmCC)](https://code.visualstudio.com/)
[![Github](https://img.shields.io/badge/_-Github-181717.svg?style=for-the-badge&logo=github&logoColor=white&logoSize=auto)](https://github.com/)
</div>

## 📋 Descripción

Este simulador de partículas simula el comportamiento físico de materiales granulares como la perlita expandida. Las partículas caen por gravedad, se acumulan y responden a las interacciones físicas de manera natural. Incluye un sistema de nivel automático con drenaje cuando se alcanza cierta capacidad.

Esta simulacion se hace para poder avanzar en el desarrollo y prototipado de un proyecto de semi automatizacion industrial de una linea de produccion de perlita expandida para su posterior empaquetado. El campo de juego es una representacion de un visor de inspeccion de una tolva de llenado de la linea de produccion, mediante el cual se puede saber el nivel de llenado de la misma. A traves de una camara, se puede detectar (con procesamiento de imagenes y/o opencv) el nivel de llenado de la tolva y enviar una señal al sistema para que se activen electrovalvulas  de apertura y se vacie el contenido de la camara.

### 🎯 Características Principales

- **Simulación de Física**: Gravedad, colisiones y acumulación natural
- **Múltiples tamaños de Partículas**: Partículas de perlita de distintos tamaños
- **Sistema de Nivel Automático**: Drenaje automático cuando se alcanza el nivel configurado
- **Aparición Configurable**: Control de velocidad, área y tamaño de clusters de aparicion de partículas
- **Interfaz Interactiva**: Dibuja con mouse, cambia modos y configura parámetros
- **Redimensionamiento Dinámico**: Ajusta el tamaño visual de las partículas en tiempo real
- **Arquitectura Modular**: Código bien organizado y documentado

## 🚀 Instalación

### Requisitos del Sistema

- **Python 3.8 o superior**

### Dependencias

```bash
# Instalar pygame (única dependencia externa)
pip install pygame
```

### Instalación Paso a Paso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/simulador-perlita.git
   cd simulador-perlita
   ```

2. **Instalar dependencias**:
   ```bash
   pip install pygame
   ```

3. **Ejecutar el simulador**:
   ```bash
   cd "Perlita falling"
   python main.py
   ```

## 🎮 Controles y Uso

### Controles de Movimiento y Configuración

| Tecla | Función |
|-------|---------|
| **↑ ↓** | Aumentar/Disminuir velocidad de aparición |
| **← →** | Encoger/Ampliar área de caída |
| **Re Pág / Av Pág** | Más/Menos partículas por cluster |
| **1-9** | Cambiar tamaño visual de píxeles |

### Modos de Dibujo

| Tecla | Modo |
|-------|------|
| **P** | Modo Perlita |
| **R** | Modo Roca |
| **E** | Modo Borrador |

### Controles del Sistema

| Tecla | Función |
|-------|---------|
| **A** | Activar/Desactivar aparición automática |
| **O** | Pausar/Reanudar simulación |
| **L** | Activar línea de nivel |
| **Inicio/Fin** | Subir/Bajar línea de nivel |
| **Espacio** | Limpiar todo el campo |
| **ESC** | Volver al menú |

### Controles de Mouse

- **Click Izquierdo**: Dibujar partículas del tipo seleccionado
- **Arrastrar**: Dibujar continuamente mientras se mueve

## 📁 Estructura del Proyecto

```
perlita falling v3/
├── main.py                    # 🎮 Punto de entrada principal del juego
├── simulacion.py              # 🎯 Coordinador principal de todos los sistemas
├── particulas.py              # ⚪ Definición de tipos de partículas (perlita, roca)
├── grillas.py                 # 🔲 Sistema de grilla y manejo de la matriz de simulación
├── sistema/                 # ⚙️ Sistemas especializados del juego
│   ├── __init__.py            # Inicializador del paquete de sistemas
│   ├── mensajes.py            # 💬 Sistema de mensajes temporales en pantalla
│   ├── aparicion.py           # 🌟 Control de generación automática de partículas
│   ├── nivel.py               # 📏 Sistema de nivel y drenaje automático
│   ├── input.py               # 🎮 Manejo de entrada (teclado y mouse)
│   └── fisicas.py             # 🔬 Motor de física para movimiento de partículas
├── ui/                      # 🎨 Interfaz de usuario y renderizado
│   ├── __init__.py            # Inicializador del paquete de UI
│   ├── render_juego.py        # 🎮 Renderizador de la pantalla de juego
│   ├── render_menu.py         # 📋 Renderizador de menús y pantalla de inicio
│   └── hud.py                 # 📊 Elementos adicionales de interfaz
├── core/                    # 🏗️ Componentes fundamentales
│   ├── __init__.py            # Inicializador del paquete core
│   ├── constantes.py          # 📋 Todas las constantes de configuración
│   ├── estado_juego.py        # 🔄 Manejo de estados del juego
│   └── utilidades.py          # 🛠️ Funciones de utilidad comunes
└── README.md                  # 📖 Este archivo de documentación
```

## 🔧 Descripción Detallada de Archivos

### Archivos Principales

- **`main.py`**: Punto de entrada que inicializa pygame, maneja la ventana y coordina los estados del juego (splash, menú, simulación).

- **`simulacion.py`**: Clase principal que coordina todos los sistemas. Integra física, aparición, nivel, input y mensajes en un solo lugar.

- **`particulas.py`**: Define las clases `ParticulaPerlita` y `ParticulaRoca` con sus comportamientos físicos específicos.

- **`grillas.py`**: Implementa el sistema de grilla que divide el espacio en celdas para optimizar las colisiones y el renderizado.

### Sistema de Subsistemas

- **`sistema/mensajes.py`**: Maneja los mensajes temporales que aparecen en pantalla para informar cambios al usuario.

- **`sistema/aparicion.py`**: Controla la generación automática de partículas: velocidad, posición, clusters y área de aparición.

- **`sistema/nivel.py`**: Implementa el sistema de drenaje automático cuando las partículas alcanzan un nivel determinado.

- **`sistema/input.py`**: Procesa toda la entrada del usuario (teclado y mouse) y la traduce a acciones del juego.

- **`sistema/fisicas.py`**: Motor de física que actualiza las posiciones de las partículas según gravedad y colisiones.

### Interfaz de Usuario

- **`ui/render_juego.py`**: Renderiza la pantalla principal del juego incluyendo el área de simulación, mensajes e instrucciones.

- **`ui/render_menu.py`**: Maneja el renderizado del splash screen con logo y el menú principal.

- **`ui/hud.py`**: Elementos adicionales como indicadores de modo e información de debug.

### Componentes Core

- **`core/constantes.py`**: Centraliza todas las constantes de configuración para fácil modificación.

- **`core/estado_juego.py`**: Maneja las transiciones entre estados (splash → menú → juego).

- **`core/utilidades.py`**: Funciones de utilidad como interpolación, cálculo de distancias, temporizadores, etc.

## ⚙️ Configuración

### Modificar Parámetros de Simulación

Edita `core/constantes.py` para ajustar:

```python
# Velocidad de aparición
VELOCIDAD_APARICION_POR_DEFECTO = 1.0
VELOCIDAD_APARICION_MAXIMA = 10.0

# Área de simulación
ANCHO_AREA_JUEGO = 200
ALTO_AREA_JUEGO = 600

# Sistema de drenaje
TIEMPO_DRENAJE_SEGUNDOS = 2.0
```

### Personalizar Colores

```python
# En core/constantes.py
COLOR_PERLITA = (240, 240, 235)
COLOR_ROCA = (100, 100, 100)
COLOR_BORDE = (0, 255, 0)
```

## 🔬 Aspectos Técnicos

### Algoritmo de Física

1. **Actualización por Frames**: Cada frame actualiza todas las partículas desde abajo hacia arriba
2. **Detección de Colisiones**: Sistema de grilla optimizado para colisiones eficientes
3. **Gravedad Simulada**: Las partículas intentan caer, con colisiones laterales si hay obstáculos
4. **Prevención de Sesgos**: Alternancia de dirección de procesamiento para evitar patrones artificiales

### Sistema de Aparición Inteligente

- **Velocidades Fraccionarias**: Permite velocidades como 0.5 (50% probabilidad por frame)
- **Clusters Configurables**: Genera grupos de partículas para simular comportamiento realista
- **Área Variable**: Desde aparición puntual hasta cobertura completa del ancho

### Optimizaciones de Rendimiento

- **Grilla Espacial**: División del espacio para colisiones O(1) en lugar de O(n²)
- **Procesamiento Selectivo**: Solo actualiza partículas que pueden moverse
- **Renderizado Optimizado**: Superficie temporal para reducir operaciones de dibujo

## 🐛 Solución de Problemas

### El juego no inicia

1. Verificar que Python 3.8+ esté instalado:
   ```bash
   python --version
   ```

2. Verificar que pygame esté instalado:
   ```bash
   python -c "import pygame; print('Pygame OK')"
   ```

### Rendimiento lento

1. Reducir el tamaño del área de juego en `constantes.py`
2. Disminuir la velocidad de aparición
3. Usar tamaños de celda más grandes (teclas 7-9)

### Problemas de ventana

- El juego soporta redimensionamiento dinámico
- Usar ESC para volver al menú si hay problemas
- Reiniciar con Espacio si la simulación se vuelve muy densa

## 🤝 Como contribuir

1. Fork al proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit a tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

### Guías de Contribución

- Mantener el código en español en lo posible
- Documentar todas las funciones
- Seguir la estructura modular existente
- Agregar tests para nuevas características
- Usar nombres descriptivos para variables y funciones

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

#### Créditos

Partes del codigo (la simulacion de fisica en particular) estan inspiradas en el siguiente proyecto sin licencia:

- [Python-Falling-Sand-with-pygame](https://github.com/educ8s/Python-Falling-Sand-with-pygame)  
  Autor: Programming With Nick  

## 🏢 Desarrollado para

**TUCUMORDOR** - Automatizacion Industrial en Tucumán, Argentina

---

⭐ **¡Dale una estrella si te gusta el proyecto!** ⭐ 