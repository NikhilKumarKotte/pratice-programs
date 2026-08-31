import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# Player
player = pygame.Rect(225, 600, 50, 80)

# Enemy cars
enemies = []

score = 0
speed = 5

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 7

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 7

    # Keep player on road
    player.x = max(100, min(350, player.x))

    # Create enemy
    if random.randint(1, 30) == 1:
        x = random.randint(100, 350)

        enemy = pygame.Rect(x, -100, 50, 80)
        enemies.append(enemy)

    # Move enemies
    for enemy in enemies:
        enemy.y += speed

        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            score += 1

    # Collision
    for enemy in enemies:
        if player.colliderect(enemy):
            running = False

    # Draw
    screen.fill((30, 130, 30))

    # Road
    pygame.draw.rect(
        screen,
        (60, 60, 60),
        (75, 0, 350, HEIGHT)
    )

    # Road lines
    for y in range(0, HEIGHT, 80):
        pygame.draw.rect(
            screen,
            "white",
            (245, y, 10, 40)
        )

    # Player
    pygame.draw.rect(screen, "blue", player)

    # Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, "red", enemy)

    text = font.render(
        f"Score: {score}",
        True,
        "white"
    )

    screen.blit(text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

print("Game Over!")
print("Score:", score)