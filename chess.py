import pygame

pygame.init()
widht = 800
height = 700
screen = pygame.display.set_mode((widht, height))
pygame.display.set_caption("Chess Game")
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
#peices
white_pieces = ['']

run = True
while run:
    timer.tick(fps)
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()