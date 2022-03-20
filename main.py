
if __name__ == '__main__':

    # further decomposition
    #1) Ask the user for their name and set this to a variable so that we can refer to them later in the program

    #2) Create a function that presents users with a question and allows them to pick an answer from multiple choices
    #A. create another function(or maybe a class) to check whether a user clicks within a buttons hitbox
    #B. darken questions that are clicked by the user

    #3)create multiple maths question
    #A. make these maths questions vary in difficulty
    #B.

    #imports
    import sys

    import pygame
    from pygame.locals import *

    pygame.init() #starts pygame

    #frames per second setup
    fps = 60
    fpsClock = pygame.time.Clock()

    #screen setup
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))



    #constants and colours

    #variables






    # Game loop.
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update.

        # Draw.

        pygame.display.flip()
        fpsClock.tick(fps)