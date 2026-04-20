import pygame
import random
import os

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
font = pygame.font.Font(None, 36)

with open("highscore.txt", "r") as file:
    try:
        highscore = int(file.read())
    except ValueError:
        highscore = 0

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50
player_img1 = pygame.image.load(os.path.join("assets", "player_frame1.png")).convert_alpha()
player_img2 = pygame.image.load(os.path.join("assets", "player_frame2.png")).convert_alpha()

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10
last_x = 0
trail = []
enemy_img = pygame.image.load(os.path.join("assets", "enemy.jpg")).convert_alpha()

score = 0
game_over = False
frame_count = 0

def close_game():
    if score > highscore:
        with open("highscore.txt", "w") as file:
            file.write(str(score)) 
    game_over = True

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass

    # bug 1: fixed by reversing the operation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 15
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 15

    enemy_pos[1] += enemy_speed
    trail.append({'x': enemy_pos[0], 'y': enemy_pos[1], 'alpha': 255})

    for segment in trail: segment['alpha'] -= 40
    trail = [segment for segment in trail if segment['alpha'] > 0]

    # bug 2: fixed by setting enemy position to a random point at the top
    if enemy_pos[1] > HEIGHT:
        score += 1
        print(f"Score: {score}")
        enemy_speed += 1
        last_x = enemy_pos[0]

        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    # bug 3: fixed by using a correct collision detection method
    if (
        player_pos[0] < enemy_pos[0] + enemy_size and
        player_pos[0] + player_size > enemy_pos[0] and
        player_pos[1] < enemy_pos[1] + enemy_size and
        player_pos[1] + player_size > enemy_pos[1]
    ):
        print("Game Over!")
        close_game()
        game_over = True

    # Drawing
    screen.fill((0, 0, 0))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    highscore_text = font.render(f"Highscore: {highscore}", True, WHITE)
    screen.blit(highscore_text, (10, 40))

    frame_count += 1
    if (frame_count // 10) % 2 == 0:
        screen.blit(player_img1, (player_pos[0], player_pos[1]))
    else:
        screen.blit(player_img2, (player_pos[0], player_pos[1]))

    for segment in trail:
        trail_surface = pygame.Surface((enemy_size, enemy_size), pygame.SRCALPHA)
        trail_surface.blit(enemy_img, (0, 0))

        trail_surface.set_alpha(segment['alpha'])
        screen.blit(trail_surface, (segment['x'], segment['y']))

    screen.blit(enemy_img, (enemy_pos[0], enemy_pos[1]))

    pygame.display.update()
    clock.tick(30)

pygame.quit()