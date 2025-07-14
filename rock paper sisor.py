import random
import pygame


class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
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

        self.rock_btn = Button(30, 520, 300, 140)
        self.paper_btn = Button(340, 520, 300, 140)
        self.scissors_btn = Button(650, 520, 300, 140)

        self.font = pygame.font.Font('splatch.ttf', 90)  # Make sure this file exists, or use None for default
        self.text = self.font.render(f" ", True, (255, 255, 255))

        self.pl_score = 0
        self.pc_score = 0

        self.player_choice = None
        self.ai_choice = None
        self.result = None

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rock_btn.clicked(event.pos):
                            self.player_choice = "rock"
                            self.screen.blit(self.choose_rock, (120, 200))
                        elif self.paper_btn.clicked(event.pos):
                            self.player_choice = "paper"
                            self.screen.blit(self.choose_paper, (120, 200))
                        elif self.scissors_btn.clicked(event.pos):
                            self.player_choice = "scissors"
                            self.screen.blit(self.choose_scissors, (120, 200))

            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.r_btn, (20, 500))
            self.screen.blit(self.p_btn, (330, 500))
            self.screen.blit(self.s_btn, (640, 500))
            pygame.display.flip()

        pygame.quit()

    def computer(self):
        self.pc_option = random.choice(["rock", "paper", "scissors"])
        if self.pc_option == "rock":
            pc_choice = self.choose_rock
        elif self.pc_option == "paper":
            pc_choice = self.choose_paper
        else:
            pc_choice = self.choose_scissors
        self.screen.blit(pc_choice, (600, 200))
        return self.pc_option

    def pl_score_cache(self):
        self.pl_score = 0


