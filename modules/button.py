import pygame, modules.data_base as data, modules.path_file as path
class Button:
    def __init__(self, x = 0, y = 0, width = 200, height = 66, text = 0, action = None):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.TEXT = text
        self.ACTION = action
        self.STATE = None
    def check_click(self, act):
        if (self.X < pygame.mouse.get_pos()[0] < self.X + self.WIDTH and
            self.Y < pygame.mouse.get_pos()[1] < self.Y + self.HEIGHT):
            if act == "click":
                self.STATE = "click"
            elif act == "up" and self.STATE == "click":
                self.ACTION()
            elif act == "hover":
                self.STATE = "hover"                
    def blit_button(self, screen):
        font = pygame.font.Font(path.path_to_file("font\\EightBits.ttf"), (self.HEIGHT - self.HEIGHT // 5)// 1.2)
        if self.STATE == None: screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file("images\\another\\button_unpressed.png")), (self.WIDTH, self.HEIGHT)), (self.X, self.Y))
        elif self.STATE == "click" or self.STATE == "up": screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file("images\\another\\button_pressed.png")), (self.WIDTH, self.HEIGHT)), (self.X, self.Y))
        if self.STATE != None: pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        screen.blit(font.render(self.TEXT, True,(0, 0, 0)), (self.X + self.WIDTH // 20, self.Y + self.HEIGHT - self.HEIGHT // 5))