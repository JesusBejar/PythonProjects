import pygame
import random
import math

# PARA INICIALIZAR PYGAME
pygame.init()

# PARA CREAR LA PANTALLA
# dentro de .set_mode determinas ancho y alto
# primer numero = alto, segundo numero = ancho
pantalla = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("fondo.png")

# TITULO & ICONO
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# ICONO DE JUGADOR
# variables del jugador
img_jugador = pygame.image.load("cohete.png")
# variable del jugador
jugador_x = 368
jugador_y = 510
jugador_x_cambio = 0

# variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo64.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

# variable de la bala
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 510
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# variables para puntaje
puntaje = 0

# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# funcion de la bala
def disparaBala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# funcion detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# LOOP DEL JUEGO
se_ejecuta = True
while se_ejecuta:
    # imagen de fondo
    pantalla.blit(fondo, (0, 0))
    # RGB COLOR DE FONDO
    # pantalla.fill((250, 242, 7))
    # jugador_x += 0.10

    #  iterar eventos
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar flechas
        # KEYDOWN
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                # print("flecha izquierda")
                jugador_x_cambio = -2
            if evento.key == pygame.K_RIGHT:
                # print("flecha derecha")
                jugador_x_cambio = 2
            if evento.key == pygame.K_SPACE:
                # bala_visible == False
                if not bala_visible:
                    bala_x = jugador_x
                    disparaBala(bala_x, bala_y)
        # evento soltar flechas
        # KEYUP
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                # print("flecha fue soltada")
                jugador_x_cambio = 0
    # modificar lugar del jugador
    jugador_x += jugador_x_cambio

    # mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparaBala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # modificar lugar del enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]


        # mantener dentro de bordes
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -.1
            enemigo_y[e] += enemigo_y_cambio[e]

    # colision
        colsion = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colsion:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)
            enemigo(enemigo_x[e], enemigo_y[e], e)

    jugador(jugador_x, jugador_y)
    # enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()