"""Tests for the main game loop."""
import pytest

import pygame
from skyriot import main


def test_main_starts_and_quits(monkeypatch):
    # run main for a very short time by posting a QUIT event
    # monkeypatch pygame.event.get to return QUIT once
    calls = {"count": 0}

    def fake_get():
        if calls["count"] == 0:
            calls["count"] += 1
            return [pygame.event.Event(pygame.QUIT)]
        return []

    monkeypatch.setattr(pygame.event, "get", fake_get)
    # Should exit without error
    main.main()
