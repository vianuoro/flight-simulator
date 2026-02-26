"""Entry point for the SkyRiot game."""

import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SkyRiot Phase 1")

    clock = pygame.time.Clock()
    running = True

    # simple player represented by a rect
    player_rect = pygame.Rect(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 20, 40, 40)
    speed = 5

    def handle_input():
        nonlocal running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def update():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_rect.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_rect.x += speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_rect.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_rect.y += speed

        # clamp to screen
        player_rect.x = max(0, min(player_rect.x, SCREEN_WIDTH - player_rect.width))
        player_rect.y = max(0, min(player_rect.y, SCREEN_HEIGHT - player_rect.height))

    def render():
        screen.fill((0, 0, 50))  # dark blue background
        pygame.draw.rect(screen, (200, 200, 0), player_rect)
        pygame.display.flip()

    # Main loop
    while running:
        handle_input()
        update()
        render()
        clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()
