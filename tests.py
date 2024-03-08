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

class TestHandleVerticalCollision(unittest.TestCase):
    def test_handle_vertical_collision(self):
        player = Player(100, 100, 50, 50)
        object1 = mario.Object(100, 200, 50, 50)
        object2 = mario.Object(100, 300, 50, 50)

        collided_objects = mario.handle_vertical_collision(player, [object1, object2], 10)

        self.assertIn(object1, collided_objects)
        self.assertEqual(player.rect.y, 200)
        self.assertEqual(player.y_vel, 0)

if __name__ == "__main__":
    unittest.main()
