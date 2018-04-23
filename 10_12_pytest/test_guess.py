from unittest.mock import patch
import random

import pytest

from guess import get_random_number, Game


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effects=[1, 12])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 1
    assert game.guess() == 12
