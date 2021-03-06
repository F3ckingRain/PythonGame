import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс управления кораблём"""
    def __init__(self, ai_game):
        super().__init__()

        """Инициализирует корабль и его начальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Загружает изображение корабля и получает прямоугольник"""
        self.image = pygame.image.load("images\\1.png")
        self.rect = self.image.get_rect()

        """Каждый новый корабль появляется у нижнего края экрана"""
        self.rect.midbottom = self.screen_rect.midbottom

        """Сохранение вещественной координаты центра корабля"""
        self.x = float(self.rect.x)

        """Флаг перемещения"""
        self.moving_right = False
        self.moving_left = False

        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учётом флага"""
        """Обновляет x , а не rect"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_x_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_x_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed_y_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_y_factor

        """Обновление rect на основании self.x и self.y"""
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль по центру нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)