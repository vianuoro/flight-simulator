"""Entry point for the SkyRiot game."""

import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SkyRiot Phase 1")

    clock = pygame.time.Clock()
    running = True

    # create a player object, starting centered on screen
    player = Player(
        SCREEN_WIDTH // 2 - 20,
        SCREEN_HEIGHT // 2 - 20,
    )

    def handle_input():
        nonlocal running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def update():
        # delegate movement and clamping to player object
        player.handle_input()
        player.update()

    def render():
        screen.fill((0, 0, 50))  # dark blue background
        player.draw(screen)
        pygame.display.flip()

    # Main loop
    while running:
        handle_input()
        update()
        render()
        clock.tick(60)

    pygame.quit()
