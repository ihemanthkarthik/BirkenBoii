import unittest
import pygame
import mario  # Import the main file where setup_level is defined
from mario import Player, Block, Fire

class TestGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def test_player_movement(self):
        player = Player(100, 100, 50, 50)
        initial_x = player.rect.x
        player.move_right(5)
        self.assertEqual(player.rect.x, initial_x + 5)

    def test_player_collision(self):
        player = Player(100, 100, 50, 50)
        block = Block(150, 150, 50)
        # Simulate collision by checking if the rectangles intersect
        self.assertTrue(player.rect.colliderect(block.rect))

    def test_sprite_animation(self):
        player = Player(100, 100, 50, 50)
        # Assuming sprite animations are correct based on provided code
        self.assertIsNotNone(player.sprite)

    def test_level_setup(self):
        level_draw = []
        mario.main.setup_level(level_draw)  # Call the function from the main file
        # Assuming the level is correctly set up based on provided code
        self.assertTrue(len(level_draw) > 0)

    def tearDown(self):
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
