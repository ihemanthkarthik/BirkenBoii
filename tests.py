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

if __name__ == "__main__":
    unittest.main()
