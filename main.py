
if __name__ == '__main__':
    '''
    decomposition
    1) Ask the user for their name and set this to a variable so that we can refer to them later in the program

    2) Create a function that presents users with a question and allows them to pick an answer from multiple choices
    A. create another function(or maybe a class) to check whether a user clicks within a buttons hitbox
    B. darken questions that are clicked by the user
    C. allow this function to takein a background to also display to the user

    3)create multiple maths question
    A. make these maths questions vary in difficulty
    B. make the questions harder the more they succeed

    4) After completing the quiz display to users their mistakes and overall percentage on the test
    a. record what questions they got wrong
    b) find a percentage using the total questions divided by the number of questions they got right they got right

    5) Ask the user whether they want to try again(show improvements over time)
    '''

    #imports
    import sys

    import pygame
    from pygame.locals import *

    pygame.init() #starts pygame

    #frames per second setup
    fps = 60
    fpsClock = pygame.time.Clock()

    #screen setup
    width, height = 800, 480
    screen = pygame.display.set_mode((width, height))

    font = pygame.font.SysFont('Comic Sans MS', 30)





    #constants and colours

    #variables, dictionaries and lists
    question = 1
    question_dictionary = {1: ["what is 1+1", "2", "window", "11"]}
    #print(question_dictionary.get((question))[0])

    class button:
        def __init__(self, x, y, text):
            self.clicked = False
            self.correct = None
            self.x = x
            self.y = y
            self.text = text



    def ask_question(background, question_number):

        #screen.blit(background)
        question = question_dictionary.get(question_number)[0] #finds a question stored in the dictionary
        answer = question_dictionary.get(question_number)[1] #finds a question stored in the dictionary

        textsurface = font.render(str(question), False, (255, 255, 255))
        screen.blit(textsurface, (0, 0))
        print(question) #test
        print(answer) #test


    # Game loop.
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update.
        ask_question("None", 1)

        # Draw.

        pygame.display.flip()
        fpsClock.tick(fps)