import random

import pygame


pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blue Block Dodge")
clock = pygame.time.Clock()

WHITE = (245, 245, 245)
BLACK = (25, 25, 35)
RED = (230, 55, 65)
BLUE = (55, 125, 235)

PLAYER_SIZE = 48
PLAYER_SPEED = 6
OBSTACLE_SIZE = 40
START_OBSTACLE_SPEED = 3
SPAWN_EVENT = pygame.USEREVENT + 1

font = pygame.font.Font(None, 36)
large_font = pygame.font.Font(None, 72)


def reset_game():
    player = pygame.Rect(
        WIDTH // 2 - PLAYER_SIZE // 2,
        HEIGHT - PLAYER_SIZE - 20,
        PLAYER_SIZE,
        PLAYER_SIZE,
    )
    return player, [], 0.0


player, obstacles, elapsed_time = reset_game()
pygame.time.set_timer(SPAWN_EVENT, 700)
game_over = False
playing = True

while playing:
    delta_time = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == SPAWN_EVENT and not game_over:
            x_position = random.randint(0, WIDTH - OBSTACLE_SIZE)
            obstacles.append(
                pygame.Rect(x_position, -OBSTACLE_SIZE, OBSTACLE_SIZE, OBSTACLE_SIZE)
            )
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                player, obstacles, elapsed_time = reset_game()
                game_over = False
            elif event.key == pygame.K_ESCAPE:
                playing = False

    if not game_over:
        elapsed_time += delta_time
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += PLAYER_SPEED

        player.clamp_ip(screen.get_rect())

        obstacle_speed = START_OBSTACLE_SPEED + int(elapsed_time // 10)
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.colliderect(player):
                game_over = True

        obstacles = [obstacle for obstacle in obstacles if obstacle.top < HEIGHT]

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player, border_radius=8)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLUE, obstacle, border_radius=5)

    seconds = int(elapsed_time)
    score_text = font.render(f"Time: {seconds}s", True, BLACK)
    screen.blit(score_text, (16, 16))

    speed_level = 1 + seconds // 10
    speed_text = font.render(f"Speed: {speed_level}", True, BLACK)
    screen.blit(speed_text, (16, 50))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 190))
        screen.blit(overlay, (0, 0))

        title = large_font.render("Game Over!", True, RED)
        final_score = font.render(f"You survived for {seconds} seconds", True, BLACK)
        retry = font.render("Press R to play again or Esc to quit", True, BLACK)

        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
        screen.blit(
            final_score,
            final_score.get_rect(center=(WIDTH // 2, HEIGHT // 2)),
        )
        screen.blit(retry, retry.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45)))

    pygame.display.flip()

pygame.quit()
