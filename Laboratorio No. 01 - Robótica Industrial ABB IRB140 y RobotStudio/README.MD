# 🤖 Laboratorio de Robótica: [Nombre o Título de la Práctica]

**Asignatura:** [Nombre de la asignatura]  
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
*[Aquí debes redactar un resumen claro de cómo abordaste el problema. Explica el objetivo de la práctica, la estrategia general que seguiste y cómo el robot, la banda transportadora y la herramienta interactúan para cumplir la tarea.]*

- **Objetivo principal:** [Breve descripción del objetivo]
- **Estrategia implementada:** [Explicación de la lógica general]

---

## 2. Layout y Plano de Planta

A continuación, se presenta el plano de planta que indica la ubicación exacta de los elementos en el espacio de trabajo:

- **Robot ABB:** ABB 140 + Herramienta (Portamarcador)
- **Banda transportadora:** Ubicada Frente al robot, con función principal de llevar el "pastel" a una posición deseada.
- **Superficies de trabajo:** "Pastel", basicamente es un tablero colocado para cumplir función de lugar de dibujo.

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
*[Describe cómo es la herramienta (Tool Data / Tool Center Point - TCP). Explica los materiales, el mecanismo de agarre (si es una pinza), la sujeción al brida del robot, y las consideraciones de diseño que tuviste en cuenta (peso, centro de gravedad, reach, etc.).]*

### 4.2. Modelo CAD
A continuación, se muestra el modelo CAD de la herramienta desarrollada:

![Modelo CAD de la Herramienta](ruta/a/tu/imagen_cad.png)
*(Figura 3: Modelo CAD de la herramienta / Tool)*

- **Archivo CAD:** [Enlace al archivo `.step`, `.stl` o carpeta en el repositorio si aplica]

---

## 5. Calibración de la Herramienta
*[Esta es una sección crítica. Compara ambos métodos.]*

Se realizó la calibración del TCP (Tool Center Point) utilizando dos métodos distintos. A continuación, se comparan los resultados:

| Parámetro / Métrica | Calibración en RobotStudio (Simulación) | Calibración en Robot Real (Físico) | Diferencia / Observaciones |
| :--- | :--- | :--- | :--- |
| **Método usado** | [Ej. 4 puntos / Automático] | [Ej. 4 puntos / Manual con punta] | - |
| **Coordenada X (mm)** | [Valor] | [Valor] | [Diferencia] |
| **Coordenada Y (mm)** | [Valor] | [Valor] | [Diferencia] |
| **Coordenada Z (mm)** | [Valor] | [Valor] | [Diferencia] |
| **Error máximo (mm)** | [Valor] | [Valor] | [Diferencia] |

**Análisis de la comparación:**
*[Explica por qué existen diferencias. ¿Hubo error humano en el robot real? ¿Juego mecánico en las articulaciones? ¿La simulación asume perfección?]*

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
