import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
RED1 = (200, 0, 0)
RED2 = (150, 0, 0)
RED3 = (100, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # bug 1: fixed by reversing the operation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 15
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 15

    enemy_pos[1] += enemy_speed

    # bug 2: fixed by setting enemy position to a random point at the top
    if enemy_pos[1] > HEIGHT:
        score += 1
        print(f"Score: {score}")
        enemy_speed += 1
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    # bug 3: fixed by using a correct collision detection method
    if (
        player_pos[0] < enemy_pos[0] + enemy_size and
        player_pos[0] + player_size > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + enemy_size and
        player_pos[1] + player_size > enemy_pos[1]
    ):
        print("Game Over!")
        game_over = True

    # Drawing
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, RED3, (enemy_pos[0], enemy_pos[1] - (85 - enemy_speed), enemy_size, enemy_size))
    pygame.draw.rect(screen, RED2, (enemy_pos[0], enemy_pos[1] - (60 - enemy_speed), enemy_size, enemy_size))
    pygame.draw.rect(screen, RED1, (enemy_pos[0], enemy_pos[1] - (35 - enemy_speed), enemy_size, enemy_size))

    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
