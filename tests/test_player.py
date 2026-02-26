"""Unit tests for :class:`Player`."""

import pygame
import pytest

from skyriot.player import Player
from skyriot.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class FakeKeys:
    """Mimic pygame.key.get_pressed() sequence."""

    def __init__(self, pressed_set):
        # set of key constants that should appear pressed
        self.pressed = pressed_set

    def __getitem__(self, index):
        return 1 if index in self.pressed else 0


@pytest.fixture(autouse=True)
def init_pygame(tmp_path, monkeypatch):
    # ensure pygame can initialize in headless CI environment
    pygame.display.init()
    pygame.display.set_mode((1, 1))
    yield
    pygame.display.quit()


def test_player_moves_left_and_clamps(monkeypatch):
    player = Player(10, 10, speed=5)

    # simulate holding left arrow for one frame
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: FakeKeys({pygame.K_LEFT}))
    player.handle_input()
    player.update()

    assert player.rect.x == 5
    assert player.rect.y == 10

    # move far left past boundary
    player.rect.x = 0
    monkeypatch.setattr(pygame.key, "get_pressed", lambda: FakeKeys({pygame.K_LEFT}))
    player.handle_input()
    player.update()
    assert player.rect.x == 0, "Player should not move past left edge"


def test_player_moves_diagonally(monkeypatch):
    player = Player(100, 100, speed=3)

    monkeypatch.setattr(
        pygame.key,
        "get_pressed",
        lambda: FakeKeys({pygame.K_RIGHT, pygame.K_DOWN}),
    )
    player.handle_input()
    player.update()

    assert player.rect.x == 103
    assert player.rect.y == 103
