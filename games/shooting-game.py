import pygame
import random
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player = pygame.Rect(380, 280, 40, 40)

targets = []
bullets = []

score = 0

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            dx = mouse_x - player.centerx
            dy = mouse_y - player.centery

            distance = math.hypot(dx, dy)

            if distance != 0:

                dx /= distance
                dy /= distance

                bullets.append([
                    player.centerx,
                    player.centery,
                    dx * 10,
                    dy * 10
                ])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= 5

    if keys[pygame.K_s]:
        player.y += 5

    if keys[pygame.K_a]:
        player.x -= 5

    if keys[pygame.K_d]:
        player.x += 5

    # Spawn targets
    if random.randint(1, 30) == 1:

        target = pygame.Rect(
            random.randint(0, WIDTH - 30),
            random.randint(0, HEIGHT - 30),
            30,
            30
        )

        targets.append(target)

    # Move bullets
    for bullet in bullets[:]:

        bullet[0] += bullet[2]
        bullet[1] += bullet[3]

        bullet_rect = pygame.Rect(
            bullet[0],
            bullet[1],
            8,
            8
        )

        for target in targets[:]:

            if bullet_rect.colliderect(target):

                targets.remove(target)

                if bullet in bullets:
                    bullets.remove(bullet)

                score += 1
                break

    screen.fill((15, 15, 25))

    pygame.draw.rect(
        screen,
        "blue",
        player
    )

    for target in targets:

        pygame.draw.circle(
            screen,
            "red",
            target.center,
            15
        )

    for bullet in bullets:

        pygame.draw.circle(
            screen,
            "yellow",
            (int(bullet[0]), int(bullet[1])),
            5
        )

    text = font.render(
        f"Score: {score}",
        True,
        "white"
    )

    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()