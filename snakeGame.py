import pygame

black = (0, 0, 0)


class Snake:

    def __init__(self):
        """ Receives the screen size and initializes the snake at the center of it """
        self.game_screen = pygame.display.get_surface()
        self.max_height = self.game_screen.get_height()
        self.max_width = self.game_screen.get_width()
        self.x_pos = self.game_screen.get_width() / 2
        self.y_pos = self.game_screen.get_height() / 2
        self.color = (255, 255, 255)
        self.blockSize = 10
        self.blockWidth = 10

    def move(self, key_press):
        """ Receives a key-press and decides where to move the snake """

        self.validate_key_press(key_press)

        key = key_press.key
        if key not in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            return

        if key == pygame.K_UP:
            self.y_pos -= 10
        elif key == pygame.K_DOWN:
            self.y_pos += 10
        elif key == pygame.K_LEFT:
            self.x_pos -= 10
        elif key == pygame.K_RIGHT:
            self.x_pos += 10

        self.draw()
        return self.check_if_game_over()
    
    def __str__(self):
        return f"Snake [{self.x_pos}, {self.y_pos}]"

    def draw(self):
        pygame.Surface.fill(self.game_screen, black)
        pygame.draw.rect(self.game_screen, self.color, [self.x_pos, self.y_pos, self.blockSize, self.blockWidth])

    def validate_key_press(self, key_press):
        try:
            if key_press.type not in [pygame.KEYDOWN]:
                raise ValueError
        except AttributeError:
            raise AttributeError('Invalid data type, must be a pygame.KEYDOWN')

    def check_if_game_over(self):
        if self.y_pos < 0 or self.y_pos >= self.max_height:
            return True
        elif self.x_pos < 0 or self.x_pos >= self.max_width:
            return True
        return False
