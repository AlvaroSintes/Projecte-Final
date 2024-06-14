import pygame
import sys
import random

def pex3():

# Inicializar Pygame
    pygame.init()

# Configuración de la pantalla
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego con Obstáculos")

# Colores
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # Posición inicial del círculo
    x, y = 400, 300
    radius = 25
    velocity = 5

    # Clase para obstáculos
    class Obstacle:
        def __init__(self, x, y, w, h, color, shape):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.color = color
            self.shape = shape
            self.vel_x = random.choice([-6, -5, -4, 4, 5, 6])
            self.vel_y = random.choice([-6, -5, -4, 4, 5, 6])
        
        def move(self):
            self.x += self.vel_x
            self.y += self.vel_y
            if self.x <= 0 or self.x + self.w >= 800:
                self.vel_x *= -1
            if self.y <= 0 or self.y + self.h >= 600:
                self.vel_y *= -1
        
        def draw(self, screen):
            if self.shape == "rect":
                pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
            elif self.shape == "circle":
                pygame.draw.circle(screen, self.color, (self.x + self.w // 2, self.y + self.h // 2), self.w // 2)

    # Crear obstáculos
    obstacles = [
        Obstacle(random.randint(0, 750), random.randint(0, 550), random.randint(30, 50), random.randint(30, 50), RED, "rect")
        for _ in range(3)
    ] + [
        Obstacle(random.randint(0, 750), random.randint(0, 550), random.randint(30, 50), random.randint(30, 50), BLUE, "circle")
        for _ in range(2)
    ]

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Teclas de dirección
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
        if keys[pygame.K_RIGHT]:
            x += velocity
        if keys[pygame.K_UP]:
            y -= velocity
        if keys[pygame.K_DOWN]:
            y += velocity

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar el círculo del jugador
        pygame.draw.circle(screen, GREEN, (x, y), radius)

        # Mover y dibujar los obstáculos
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw(screen)

        # Verificar colisiones
        player_rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        for obstacle in obstacles:
            if obstacle.shape == "rect":
                obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.w, obstacle.h)
            elif obstacle.shape == "circle":
                obstacle_rect = pygame.Rect(obstacle.x, obstacle.y, obstacle.w, obstacle.h)
            if player_rect.colliderect(obstacle_rect):
                print("¡Colisión!")
                running = False

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del bucle
        pygame.time.Clock().tick(30)

    # Salir de Pygame
    pygame.quit()
    sys.exit()


