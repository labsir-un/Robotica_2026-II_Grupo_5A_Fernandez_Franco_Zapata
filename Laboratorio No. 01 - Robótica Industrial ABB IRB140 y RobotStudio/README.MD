# 🤖 Laboratorio de Robótica: Robótica Industrial – Trayectorias, Entradas y Salidas Digitales

**Asignatura:** Robótica
**Fecha de entrega:** 29 de octubre de 2026  

---

## 📑 Tabla de Contenidos
1. [Descripción de la Solución](#1-descripción-de-la-solución)
2. [Layout y Plano de Planta](#2-layout-y-plano-de-planta)
3. [Diagrama de Flujo del Sistema](#3-diagrama-de-flujo-del-sistema)
4. [Diseño y Modelado de la Herramienta](#4-diseño-y-modelado-de-la-herramienta)
5. [Calibración de la Herramienta](#5-calibración-de-la-herramienta)
6. [Programación en RAPID](#6-programación-en-rapid)
7. [Código Fuente](#7-código-fuente)

---

## 1. Descripción de la Solución
**Objetivo Principal:**  
Automatizar un proceso de decoración de tortas (aplicado a la industria de alimentos) mediante el seguimiento controlado de trayectorias con un robot ABB IRB 140, integrando una banda transportadora y lógica de control basada en Entradas y Salidas Digitales (I/O).

**Estrategia Implementada:**  
Se diseñó una celda de trabajo donde la banda transporta una "torta virtual" hacia el robot. El sistema opera bajo un ciclo principal (`WHILE TRUE`) que monitorea tres entradas digitales (DI 01, DI 02, DI 03) para ejecutar distintas rutinas:
1. **Ciclo Automático (DI 01):** Transporte, decoración con nombres y figura libre, y evacuación del pastel.
2. **Pose de Mantenimiento (DI 02):** Posición segura para cambio de herramienta/marcador.
3. **Rutina "Farmear Aura" (DI 03):** Coreografía creativa del robot utilizando estructuras intermedias (ciclos/condicionales).

###Durante la implementación se aprendio a controlar la banda transportadora con FWD y BWD Conveyor.
---

## 2. Layout y Plano de Planta

A continuación, se presenta el plano de planta que indica la ubicación exacta de los elementos en el espacio de trabajo:

- **Robot ABB:** ABB 140 + Herramienta (Portamarcador)
- **Banda transportadora:** Controlada bidireccionalmente (`FWD Conveyor` / `BWD Conveyor`), con función principal de llevar el "pastel" a una posición deseada.
- **Superficies de trabajo:** "Pastel", basicamente es un tablero colocado para cumplir función de lugar de dibujo.
- **Herramienta (TCP):** Soporte con marcador/plumón fijado al flange del robot.

![Plano de Planta de la Celda de Trabajo](ruta/a/tu/imagen_plano.png)
*(Figura 1: Plano de planta de la celda de trabajo)*

---

## 3. Diagrama de Flujo del Sistema

El siguiente diagrama de flujo ilustra la secuencia completa de operaciones del sistema, desde el inicio del ciclo hasta la finalización de la tarea:

![Diagrama de Flujo](ruta/a/tu/imagen_flujo.png)
*(Figura 2: Diagrama de flujo de la secuencia del sistema)*

**Descripción de las etapas principales:**
1. **[DI_02, Pose de mantenimiento]:** ...
2. **[DI_01, Decoración]:** ...
3. **[DI_03, Farmear Aura]:** ...

---

## 4. Diseño y Modelado de la Herramienta
### 4.1. Diseño Detallado
| Parámetro Mecánico | Valor / Descripción |
| :--- | :--- |
| **Material de Impresión** | `[SELECCIONAR: PLA / PETG / OTRO]` |
| **Masa Total de la Herramienta ($m$)** | `[INSERTAR MASA EN kg: ej. 0.25 kg]` |
| **Centro de Masa ($X_g, Y_g, Z_g$)** | `[INSERTAR COORDENADAS EN mm]` |
| **Constante del Resorte ($k$) / Amortiguación** | `[INSERTAR ESPECIFICACIÓN DEL RESORTE]` |
| **Porcentaje de Relleno (*Infill*)** | `[INSERTAR % DE RELLENO]` |

### 4.2. Modelo CAD
A continuación, se muestra el modelo CAD de la herramienta desarrollada:

![Modelo CAD de la Herramienta](ruta/a/tu/imagen_cad.png)
*(Figura 3: Modelo CAD de la herramienta / Tool)*

- **Archivo CAD:** [Enlace al archivo `.step`, `.stl` o carpeta en el repositorio si aplica]

---

## 5. Calibración de la Herramienta

El punto de centro de la herramienta (`tool_marcador`) se calibró físicamente mediante el **método de 4 puntos (*4-Point Method*)** aproximando la punta del marcador a una referencia fija desde distintas orientaciones del robot.

* **Parámetros Obtenidos de `tooldata`:**
```rapid
PERS tooldata tool_marcador := [TRUE, [[X_tcp, Y_tcp, Z_tcp], [q1, q2, q3, q4]], [m, [Xg, Yg, Zg], [1, 0, 0, 0], 0, 0, 0]];
```
*(Reemplazar con los valores calibrados por el grupo)*:
* **Posición ($X, Y, Z$):** `[INSERTAR X_tcp, Y_tcp, Z_tcp en mm]`
* **Orientación Quaternion ($q_1, q_2, q_3, q_4$):** `

**Análisis de la comparación:**
*[Explica por qué existen diferencias. ¿Hubo error humano en el robot real? ¿Juego mecánico en las articulaciones? ¿La simulación asume perfección?]*
### Análisis de Desviaciones entre Simulación y Realidad
| Medida | Valor en RobotStudio | Valor Real | Error / Desviación |
| :--- | :--- | :--- | :--- |
| **Error de Posicionamiento TCP** | 0.0 mm | `[INSERTAR ER] mm` | `[INSERTAR]` |
| **Desviación Z del WorkObject** | 0.0 mm | `[INSERTAR ER] mm` | Absorbedor por resorte |

---

## 6. Programación en RAPID
### 6.1. Instrucciones y Funciones Utilizadas
*[Haz una lista o tabla de los comandos de RAPID más importantes que usaste y explica brevemente para qué sirven en el contexto de tu código.]*

| Instrucción / Función | Descripción y uso en la práctica |
| :--- | :--- |
| `MoveJ` / `MoveL` | [Ej. Usado para aproximar a la pieza / para soldar o trazar] |
| `TriggL` | [Ej. Usado para activar la pinza en un punto exacto de la trayectoria] |
| `WaitDI` | [Ej. Usado para esperar a que la banda transportadora posicione la pieza] |
| `[Otra instrucción]` | [Descripción] |

---

## 7. Código Fuente
A continuación, se presenta el código completo en RAPID utilizado durante el desarrollo de la práctica. 

*(Nota: Si el código es muy extenso, puedes dejar aquí los módulos principales y dejar el resto en archivos `.mod` o `.pgf` dentro de una carpeta `/codigo` en tu repositorio).*

```rapid
MODULE MainModule
    ! Declaración de variables y constantes
    CONST robtarget pHome := [...];
    PERS tooldata tTool := [...];
    
    ! Programa principal
    PROC main()
        ! Lógica principal
        ...
    ENDPROC
    
    ! Subrutinas y funciones
    PROC MoverAPieza()
        ...
    ENDPROC
ENDMODULE
