import unittest
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

class TestPlayer(unittest.TestCase):
    def test_player_init(self):
        player = Player(100, 100, 50, 50)
        self.assertIsInstance(player, Player)
        self.assertIsInstance(player.rect, pygame.Rect)
        self.assertIsInstance(player.sprite, pygame.Surface)
        self.assertIsInstance(player.mask, pygame.mask.Mask)

    def test_player_jump(self):
        player = Player(100, 100, 50, 50)
        player.jump()
        self.assertLess(player.y_vel, 0)

    def test_player_move_left(self):
        player = Player(100, 100, 50, 50)
        player.move_left(10)
        self.assertEqual(player.x_vel, -10)

    def test_player_move_right(self):
        player = Player(100, 100, 50, 50)
        player.move_right(10)
        self.assertEqual(player.x_vel, 10)

if __name__ == "__main__":
    unittest.main()
