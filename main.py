import pygame
import random

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Caza de Frutas")

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.bottom = height - 10

    def update(self):
        # Mover el jugador con las teclas izquierda y derecha
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += 5

# Clase para las frutas
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.speedy = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(-100, -50)
            self.speedy = random.randint(1, 5)

# Función para mostrar el menú de inicio
def show_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Presiona ESPACIO para comenzar", True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Función para mostrar el menú de finalización
def show_end_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Juego terminado. Presiona ESPACIO para jugar de nuevo", True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()

# Crear jugador
player = Player()
all_sprites.add(player)

# Variables de juego
score = 0

# Bucle principal del juego
running = True
show_start_menu()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generar frutas
    if random.random() < 0.02:
        fruit = Fruit()
        all_sprites.add(fruit)
        fruits.add(fruit)

    # Actualizar sprites
    all_sprites.update()

    # Verificar colisiones
    hits = pygame.sprite.spritecollide(player, fruits, True)
    for hit in hits:
        score += 1

    # Dibujar todo en la pantalla
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)

# Mostrar el menú de finalización
show_end_menu()

# Finalizar Pygame
pygame.quit()










