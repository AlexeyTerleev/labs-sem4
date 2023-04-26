import pygame


class ScrollBox:

    def __init__(self, x, y, width, height, real_width, real_height, content):

        self.pos = (x, y)

        self.content_pos = (0, 0)
        self.scroll = (0, 0)

        self.surface = pygame.Surface((real_width, real_height))
        self.visible_surface = pygame.Surface((width, height))

        self.real_width = real_width
        self.real_height = real_height
        self.content = content

    def update(self):
        self.content_pos = (- self.scroll[0] * self.surface.get_size()[0] / 2,
                            - self.scroll[1] * self.surface.get_size()[1] / 2)

    def draw(self, screen):
        self.surface.fill((211, 211, 0))
        for element in self.content:
            element.draw(self.surface)

        if self.surface.get_width() != self.real_width:
            pygame.draw.rect(
                self.surface,
                (0, 0, 0),
                (
                    int(self.surface.get_width() * self.scroll[0]) - 5,
                    self.surface.get_height() - 10,
                    10, 10
                )
            )
        if self.surface.get_height() != self.real_height:
            pygame.draw.rect(
                self.surface,
                (0, 0, 0),
                (
                    self.surface.get_width() - 10,
                    int(self.surface.get_height() * self.scroll[1]) - 5,
                    10, 10
                )
            )

        self.visible_surface.blit(self.surface, self.content_pos)
        screen.blit(self.visible_surface, self.pos)
