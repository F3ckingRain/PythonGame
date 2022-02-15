class Settings():
    """Класс для хранениея всех настроек игры"""
    def __init__(self):

        """Инициализирует настройки игры"""
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230,200,255)

        """Настройка корабля"""
        self.ship_x_speed = 2
        self.ship_y_speed = 2.5
        self.ship_limit = 3

        """Параметры снаряда"""
        self.bullet_speed = 1.5
        self.bullet_allowed = 5

        """Настройка пришельцев"""
        self.fleet_drop_speed = 10

        """1 - вправо, -1 - влево"""
        self.fleet_direction = 1

        """Темп для ускорения игры"""
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        """Темп роста стоимости пришельцев"""
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Инициализирует настройки изменяющиеся в ходе игры"""
        self.ship_speed_x_factor = 2
        self.ship_speed_y_factor = 2.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 2.0
        self.fleet_direction = 1

        """Подсчёт очков"""
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев"""
        self.ship_speed_x_factor *= self.speedup_scale
        self.ship_speed_y_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
