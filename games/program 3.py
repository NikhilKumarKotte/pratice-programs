import pygame

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

paddle_width = 15
paddle_height = 100

player1 = pygame.Rect(
    30, HEIGHT // 2 - 50,
    paddle_width, paddle_height
)

player2 = pygame.Rect(
    WIDTH - 45, HEIGHT // 2 - 50,
    paddle_width, paddle_height
)

ball = pygame.Rect(
    WIDTH // 2 - 10,
    HEIGHT // 2 - 10,
    20, 20
)

ball_speed_x = 5
ball_speed_y = 5

score1 = 0
score2 = 0

font = pygame.font.Font(None, 60)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player1.y -= 6

    if keys[pygame.K_s]:
        player1.y += 6

    if keys[pygame.K_UP]:
        player2.y -= 6

    if keys[pygame.K_DOWN]:
        player2.y += 6

    # Keep paddles inside screen
    player1.y = max(0, min(HEIGHT - paddle_height, player1.y))
    player2.y = max(0, min(HEIGHT - paddle_height, player2.y))

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Top/bottom collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Paddle collision
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Score
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = 5

    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x = -5

    screen.fill((20, 20, 20))

    pygame.draw.rect(screen, "white", player1)
    pygame.draw.rect(screen, "white", player2)
    pygame.draw.ellipse(screen, "white", ball)

    score_text = font.render(
        f"{score1}     {score2}",
        True,
        "white"
    )

    screen.blit(
        score_text,
        (WIDTH // 2 - 100, 30)
    )

    pygame.display.update()
    clock.tick(60)

pygame.quit()