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
        block = mario.get_block(64)
        self.assertIsInstance(block, pygame.Surface)
        self.assertEqual(block.get_width(), 64)
        self.assertEqual(block.get_height(), 64)

if __name__ == "__main__":
    unittest.main()
