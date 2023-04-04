import pygame.gfxdraw

import src.utilities as utilities
from src.save import Save
from src.rating import Rating

WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()
pygame.display.set_caption("Crimsoland")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

save_data = Save()
r_table = Rating(save_data.get('rating'))

background_image = pygame.image.load(utilities.get_image("land.png")).convert()
background_image = pygame.transform.scale(background_image, (1600, 1200))

font = pygame.font.SysFont('Bodoni 72 Book', 60)



