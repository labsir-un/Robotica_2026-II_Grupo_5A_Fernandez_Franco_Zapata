from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math
from matplotlib.textpath import TextPath
from matplotlib.path import Path
#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
#if not robot.Connect():
 #   raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
#if not robot.ConnectedState():
  #  raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

print("Robot conectado correctamente.")

#------------------------------------------------
# 2) Cargar el Frame (ya existente) donde quieres dibujar
#    Ajusta el nombre si tu Frame se llama diferente
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

# Asignamos este frame al robot
robot.setPoseFrame(frame)
# Usamos la herramienta activa
robot.setPoseTool(robot.PoseTool())

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s - Ajusta según necesites
robot.setRounding(5)  # blending (radio de curvatura)

#---------------------------------------------------------------
#               PARAMETROS
#--------------------------------------------------------------

z_surface = 0
z_safe    = -50             # NEGATIVO: el +Z del frame apunta hacia la superficie
z_up      = -10             # altura para viajar entre trazos de las letras
ORIENT    = rotx(0)         # usar rotx(pi) solo si el TCP apunta al revés

# Espiral  r = b * theta
turns   = 5                 # vueltas
R_max   = 70                # mm. Alcance medido: 140 mm. Si se sube, el texto sube y puede salir del alcance
seg_len = 5                 # mm por segmento (3 a 10)
b          = R_max / (2 * math.pi * turns)
theta_max  = 2 * math.pi * turns
num_points = max(20, int(math.pi * turns * R_max / seg_len))


#---------------------------------------------------------------
#               FUNCIONES
#--------------------------------------------------------------
def ir_home ():
    robot.setRounding(-1)
    robot.MoveJ(robot.JointsHome())
    #robot.MoveJ(pose(0, 0, z_surface + z_safe))
    #robot.MoveL(pose(0, 0, z_surface))

#----------------------------------
def pose(x, y, z):
    return transl(x, y, z) * ORIENT

def espiral ():
    robot.setRounding(1)
    for i in range(1, num_points + 1):
        theta = theta_max * math.sqrt(i / num_points)    # longitud de arco ~uniforme
        r = b * theta
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        robot.MoveL(pose(x, y, z_surface))

    robot.setRounding(-1)
    robot.MoveL(pose(x, y, z_surface + z_safe))          # subir al terminar la espiral

#------------------------------------------------




def nombres ():
    
    text = "DIEGO"
    scale = 1.5             # escalado (para probar tamaños)
    letter_spacing = 50       # separación entre letras en X (en el frame del objeto es y positivo)
    text_offset_x = -150        # donde empieza el texto en X (en el frame del objeto es y positivo)
    text_offset_y = 260 # debajo de la rosa en Y (en el frame del objeto es x positivo)

    x_cursor = text_offset_x  # cursor que avanza en X por cada letra

    for char in text:
        tp = TextPath((0, 0), char, size=50)
        verts = tp.vertices * scale
        codes = tp.codes

        last_x, last_y = None, None

        for (vx, vy), code in zip(verts, codes):
            x_pos = x_cursor + vx
            y_pos = text_offset_y + vy

            if code == Path.MOVETO:
                robot.MoveL(transl(y_pos , x_pos, z_safe))
                robot.MoveL(transl(y_pos , x_pos, z_surface))
            elif code in (Path.LINETO, Path.CURVE3, Path.CURVE4):
                robot.MoveL(transl(y_pos, x_pos, z_surface))

            # Actualiza última posición
            last_x, last_y = x_pos, y_pos

        # Al terminar la letra, solo levanta en el mismo sitio
        if last_x is not None and last_y is not None:
            robot.MoveL(transl(last_y , last_x, z_safe))

        # Avanza cursor para la siguiente letra
        x_cursor += letter_spacing

    # segundo nombre
    text2 = "ALEJANDRO"
    x_cursor = text_offset_x       # reinicia el cursor horizontal
    text_offset_y -= 80  # baja el texto

    for char in text2:
        tp = TextPath((0, 0), char, size=50)
        verts = tp.vertices * scale
        codes = tp.codes

        last_x, last_y = None, None

        for (vx, vy), code in zip(verts, codes):
            x_pos = x_cursor + vx
            y_pos = text_offset_y + vy

            if code == Path.MOVETO:
                robot.MoveL(transl(y_pos, x_pos, z_safe))
                robot.MoveL(transl(y_pos, x_pos, z_surface))
            elif code in (Path.LINETO, Path.CURVE3, Path.CURVE4):
                robot.MoveL(transl(y_pos, x_pos, z_surface))

            last_x, last_y = x_pos, y_pos

        # Levantar pluma al terminar la letra
        if last_x is not None and last_y is not None:
            robot.MoveL(transl(last_y, last_x, z_safe))

        # Avanzar cursor para la siguiente letra
        x_cursor += letter_spacing

        # tercer nombre
    text3 = "EDWIN"
    x_cursor = text_offset_x       # reinicia el cursor horizontal
    text_offset_y -= 80  # baja el texto

    for char in text3:
        tp = TextPath((0, 0), char, size=50)
        verts = tp.vertices * scale
        codes = tp.codes

        last_x, last_y = None, None

        for (vx, vy), code in zip(verts, codes):
            x_pos = x_cursor + vx
            y_pos = text_offset_y + vy

            if code == Path.MOVETO:
                robot.MoveL(transl(y_pos, x_pos, z_safe))
                robot.MoveL(transl(y_pos, x_pos, z_surface))
            elif code in (Path.LINETO, Path.CURVE3, Path.CURVE4):
                robot.MoveL(transl(y_pos, x_pos, z_surface))

            last_x, last_y = x_pos, y_pos

        # Levantar pluma al terminar la letra
        if last_x is not None and last_y is not None:
            robot.MoveL(transl(last_y, last_x, z_safe))

        # Avanzar cursor para la siguiente letra
        x_cursor += letter_spacing

#----------------------------------------------------------
ir_home()        
espiral()
nombres()
ir_home()
