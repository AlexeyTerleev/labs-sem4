import pygame
import gui.utils as utils
import gui.config as config
import time


class InfoBox:
    def __init__(self, text='', background_color=(255, 255, 255), text_color=(0, 0, 0), font_size=30,
                 border_color=(0, 0, 0), border_radius=0, border=1, font_style=None):

        self.background_color = background_color
        self.border_color = border_color
        self.border = border
        self.border_radius = border_radius
        self.text_color = text_color
        self.text = text
        self.font = pygame.font.Font(font_style, font_size)
        self.txt_surface = self.font.render(self.text, True, self.text_color)

        self.surface = pygame.Surface((self.txt_surface.get_width() + 10, self.txt_surface.get_height() + 10))
        self.surface.fill(background_color)
        self.surface.set_alpha(200)

        self.timer = 0.
        self.clock = time.time()
        self.called = False

    def draw(self, screen):

        curr_time = time.time()
        self.timer += (curr_time - self.clock)
        self.clock = curr_time

        styled_text = self.font.render(self.text, True, self.text_color)
        text_rect = styled_text.get_rect(center=(5, 5))
        self.surface.blit(styled_text, text_rect)

        screen.blit(self.surface, ((config.WIDTH - (self.txt_surface.get_width() + 10)) // 2,
                                   config.HEIGHT // 6 * 5))
        pygame.display.update(
            ((config.WIDTH - (self.txt_surface.get_width() + 10)) // 2, config.HEIGHT // 6 * 5,
             self.txt_surface.get_width() + 10, self.txt_surface.get_height() + 10)
        )

    def call(self, screen):
        if not self.called:
            self.called = True

            self.clock = time.time()
            for _ in iter(int, 1):
                print(self.timer)
                self.draw(screen)
                if self.timer > 2.:
                    break
