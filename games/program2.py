import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

snake = [(300, 200), (280, 200), (260, 200)]
direction = (CELL, 0)

food = (
    random.randrange(0, WIDTH, CELL),
    random.randrange(0, HEIGHT, CELL)
)

score = 0
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key in (pygame.K_UP, pygame.K_w):
                if direction != (0, CELL):
                    direction = (0, -CELL)

            elif event.key in (pygame.K_DOWN, pygame.K_s):
                if direction != (0, -CELL):
                    direction = (0, CELL)

            elif event.key in (pygame.K_LEFT, pygame.K_a):
                if direction != (CELL, 0):
                    direction = (-CELL, 0)

            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                if direction != (-CELL, 0):
                    direction = (CELL, 0)

    head = snake[0]
    new_head = (
        head[0] + direction[0],
        head[1] + direction[1]
    )

    # Wall collision
    if (
        new_head[0] < 0 or
        new_head[0] >= WIDTH or
        new_head[1] < 0 or
        new_head[1] >= HEIGHT
    ):
        running = False

    # Body collision
    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    # Eat food
    if new_head == food:
        score += 1

        food = (
            random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL)
        )
    else:
        snake.pop()

    screen.fill((20, 20, 20))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(
            screen,
            (0, 200, 0),
            (segment[0], segment[1], CELL, CELL)
        )

    # Draw food
    pygame.draw.rect(
        screen,
        (200, 0, 0),
        (food[0], food[1], CELL, CELL)
    )

    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()

print("Game Over!")
print("Final Score:", score)