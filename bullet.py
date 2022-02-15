import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами"""
    def __init__(self,ai_game):
        """Создание объектов снарядов в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images\\2.png")

        """Создание снаряда в позицйии (0,0) и назначение правильной позиции"""
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        """Позицуия снаряда"""
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        """Обновление позиции снаряда"""
        self.y -= self.settings.bullet_speed

        """Обновление позиции прямоугольника"""
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда"""
        self.screen.blit(self.image, self.rect)