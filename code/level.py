from tokenize import group
import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # Get the Display Surface
        self.display_surface = pygame.display.get_surface()

        # Sprite Group Setup
        self.visible_sprites = YSort_CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprite Setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            #print("%02d" % row_index, ' ', row)
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
                

    def run(self):
        # Update and Draw the Game]
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSort_CameraGroup(pygame.sprite.Group):
    def __init__(self):

        # General Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        # Getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)