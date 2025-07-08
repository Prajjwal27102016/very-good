import ramdom
import pygame


class Button():
    def __init__(self, x, y,pos ,width, height):
        self.x =x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos
    
    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
    
class RockPaperScissors():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("Rock Paper Scissors")

        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("rock.png").convert_alpha()
        self.p_btn = pygame.image.load("paper.png").convert_alpha()
        self.s_btn = pygame.image.load("scissors.png").convert_alpha()

        self.choose_rock = pygame.image.load("choose_rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("choose_paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("choose_scissors.png").convert_alpha()

