"""Player-related logic."""

import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Player:
    """Represents the player aircraft.

    The player is backed by a :class:`pygame.Rect` which also serves as the
    positional state. Input handling updates the rectangle and ``update``
    constrains it within the screen bounds. ``draw`` renders a simple
    rectangle for now; later phases can swap in a sprite.
    """

    def __init__(self, x=0, y=0, speed: int = 5, health: int = 100) -> None:
        # position is encoded in ``rect`` for easy rendering and collision
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed = speed
        self.health = health

    # existing helper preserved for backwards compatibility if ever used
    def move(self, dx: int, dy: int) -> None:
        """Move the player by ``dx``/``dy`` without clamping."""
        self.rect.x += dx
        self.rect.y += dy

    def handle_input(self) -> None:
        """Read the current keyboard state and adjust velocity accordingly."""
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += self.speed
        self.move(dx, dy)

    def update(self) -> None:
        """Clamp the player inside the screen bounds."""
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the player to the given surface (currently as a yellow rect)."""
        pygame.draw.rect(surface, (200, 200, 0), self.rect)
