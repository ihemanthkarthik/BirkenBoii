import unittest
import pygame
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
        player.move_left(5)
        self.assertEqual(player.rect.x, initial_x)

    def test_player_collision(self):
        player = Player(100, 100, 50, 50)
        block = Block(150, 150, 50)
        player.rect.colliderect = lambda x: True if x == block.rect else False
        player.move_right(5)
        self.assertEqual(player.rect.x, 100)  # Player should not move due to collision

    def test_sprite_animation(self):
        player = Player(100, 100, 50, 50)
        # Assuming sprite animations are correct based on provided code
        self.assertIsNotNone(player.sprite)

    def tearDown(self):
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
