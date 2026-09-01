import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

bird = pygame.Rect(100, 300, 30, 30)

velocity = 0
gravity = 0.5
jump = -9

pipes = []
score = 0

pipe_width = 70
pipe_gap = 180

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                velocity = jump

    # Bird physics
    velocity += gravity
    bird.y += int(velocity)

    # Create pipes
    if len(pipes) == 0 or pipes[-1].x < 350:

        gap_y = random.randint(150, 450)

        top_pipe = pygame.Rect(
            WIDTH,
            0,
            pipe_width,
            gap_y - pipe_gap // 2
        )

        bottom_pipe = pygame.Rect(
            WIDTH,
            gap_y + pipe_gap // 2,
            pipe_width,
            HEIGHT
        )

        pipes.append([
            top_pipe,
            bottom_pipe,
            False
        ])

    # Move pipes
    for pipe in pipes:

        pipe[0].x -= 4
        pipe[1].x -= 4

        if not pipe[2] and pipe[0].right < bird.left:

            score += 1
            pipe[2] = True

    # Remove old pipes
    pipes = [
        pipe for pipe in pipes
        if pipe[0].right > 0
    ]

    # Collision
    if bird.top <= 0 or bird.bottom >= HEIGHT:

        running = False

    for pipe in pipes:

        if bird.colliderect(pipe[0]) or bird.colliderect(pipe[1]):

            running = False

    screen.fill((100, 180, 255))

    pygame.draw.rect(
        screen,
        "yellow",
        bird
    )

    for pipe in pipes:

        pygame.draw.rect(
            screen,
            "green",
            pipe[0]
        )

        pygame.draw.rect(
            screen,
            "green",
            pipe[1]
        )

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