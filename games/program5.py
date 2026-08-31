import pygame
import random
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie Survival")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player = pygame.Rect(380, 280, 40, 40)

zombies = []
bullets = []

score = 0
health = 100

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

    # Spawn zombies
    if random.randint(1, 40) == 1:

        side = random.randint(0, 3)

        if side == 0:
            x, y = random.randint(0, WIDTH), 0
        elif side == 1:
            x, y = random.randint(0, WIDTH), HEIGHT
        elif side == 2:
            x, y = 0, random.randint(0, HEIGHT)
        else:
            x, y = WIDTH, random.randint(0, HEIGHT)

        zombies.append(pygame.Rect(x, y, 35, 35))

    # Move zombies toward player
    for zombie in zombies[:]:

        dx = player.centerx - zombie.centerx
        dy = player.centery - zombie.centery

        distance = math.hypot(dx, dy)

        if distance != 0:
            zombie.x += int(dx / distance * 2)
            zombie.y += int(dy / distance * 2)

        if zombie.colliderect(player):
            health -= 1

    # Move bullets
    for bullet in bullets[:]:

        bullet[0] += bullet[2]
        bullet[1] += bullet[3]

        if (
            bullet[0] < 0 or
            bullet[0] > WIDTH or
            bullet[1] < 0 or
            bullet[1] > HEIGHT
        ):
            bullets.remove(bullet)
            continue

        bullet_rect = pygame.Rect(
            bullet[0],
            bullet[1],
            8,
            8
        )

        for zombie in zombies[:]:

            if bullet_rect.colliderect(zombie):

                zombies.remove(zombie)

                if bullet in bullets:
                    bullets.remove(bullet)

                score += 1
                break

    if health <= 0:
        running = False

    screen.fill((20, 20, 20))

    pygame.draw.rect(screen, "blue", player)

    for zombie in zombies:
        pygame.draw.rect(screen, "green", zombie)

    for bullet in bullets:
        pygame.draw.circle(
            screen,
            "yellow",
            (int(bullet[0]), int(bullet[1])),
            5
        )

    text = font.render(
        f"Health: {health}  Score: {score}",
        True,
        "white"
    )

    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()

print("You survived!")
print("Score:", score)