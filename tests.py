import unittest
from unittest.mock import Mock, patch
import pygame
import mario  # Import the main file where setup_level is defined
from mario import Player, Block, Fire

class TestSpriteSheets(unittest.TestCase):
    def test_load_sprite_sheets(self):
        sprites = mario.load_sprite_sheets("MainCharacters", "PinkMan", 32, 32, True)
        self.assertGreater(len(sprites), 0)
        self.assertTrue("idle_left" in sprites)
        self.assertTrue("idle_right" in sprites)

class TestGetBlock(unittest.TestCase):
    def test_get_block(self):
        block = mario.get_block(32)
        self.assertIsInstance(block, pygame.Surface)
        self.assertNotEqual(block.get_width(), 32)
        self.assertNotEqual(block.get_height(), 32)

class MockPlayer:
    def __init__(self):
        self.rect = Mock()
        self.sprite = Mock()
        self.mask = Mock()
        self.x_vel = 0
        self.y_vel = 0

    def jump(self):
        self.y_vel = -10

    def move_left(self, value):
        self.x_vel = -value

    def move_right(self, value):
        self.x_vel = value


class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        player = MockPlayer()
        self.assertIsInstance(player, MockPlayer)
        self.assertIsInstance(player.rect, Mock)
        self.assertIsInstance(player.sprite, Mock)
        self.assertIsInstance(player.mask, Mock)

    def test_player_jump(self):
        player = MockPlayer()
        player.jump()
        self.assertLessEqual(player.y_vel, 0)

    def test_player_move_left(self):
        player = MockPlayer()
        player.move_left(10)
        self.assertEqual(player.x_vel, -10)

    def test_player_move_right(self):
        player = MockPlayer()
        player.move_right(10)
        self.assertEqual(player.x_vel, 10)

if __name__ == "__main__":
    unittest.main()
