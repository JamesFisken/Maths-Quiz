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

    # imports
    import sys
    import random
    import pygame
    import time
    from pygame.locals import *

    pygame.init()  # starts pygame

    # frames per second setup
    fps = 60
    fpsClock = pygame.time.Clock()
    size = 1.33 # this variable scales all the screen sizes and buttons

    # screen setup
    width, height = 900 * size, 480 * size
    screen = pygame.display.set_mode((width, height))
    font_size = round(30 * size)

    font = pygame.font.SysFont('Comic Sans MS', font_size) # font for the title
    font2 = pygame.font.SysFont('Comic Sans MS', round(30*size)) # font for the title

    button_size_x = 400 * size
    button_size_y = 150 * size
    button_distance = 460 * size

    # constants and colours

    # variables, dictionaries and lists
    question = 1
    question_dictionary = {1: ["what is 1+1", "2", "window", "11", "IDK",], #question dictionary holds all the questions and answer
                           2: ["5 + b = 12,  what is the value of b", "7", "2", "5", "what?"],
                           3: ["there were 5 birds, 2 flew away. how many birds are left?", "3", "1000000000", "4", "whats a bird"],
                           4: ["10 x 4 = 40", "True", "False"],
                           5: ["20 - 10 = 5", "False", "True"],
                           6: ["3 + 8 x 3", "27", "33"],
                           7: ["what is 8 x 8", "64", "16", "88", "42"],
                           8: ["what is 12 ÷ 3", "4", "2", "3", "9"],
                           9: ["Which polynomial has roots triple that of x^2 + 12x + 1 = 0", "x^2 + 36x + 9 = 0", "x^5 + 3x + 12 = 0", "x^2 + 24x + 8 = 0", "x^3 + 24x + 8 = 0"],
                           10: ["10 x 4 = 40", "True", "False"],
                           11: ["10 x 4 = 40", "True", "False"]

                           }


    # print(question_dictionary.get((question))[0]) TEST

    class button:
        def __init__(self, x, y, text):

            self.correct = False
            self.x = x
            self.y = y
            self.text = text


        def display(self, colour):

            pygame.draw.rect(screen, colour, pygame.Rect(self.x, self.y, button_size_x, button_size_y)) #draws button onto the screen
            text = font2.render(self.text, False, (0, 0, 0)) #sets up text surface
            text_width = text.get_width()  # gets text width
            text_height = text.get_height()
            screen.blit(text, (self.x+button_size_x/2-text_width/2, self.y+button_size_y/2-text_height/2)) #displays text surface perfectly centred using the text width

    def check_mouse_inputs(x, y):
        global question
        for button in buttons:
            if button.x+button_size_x > x and button.x < x and button.y+button_size_y > y and button.y < y: #clicking on the button
                if button.correct: #if the button has the attribute "Correct = True" has been clicked then the user has inputed the right answer
                    button.display((0, 255, 0))
                elif button.correct == False:
                    button.display((255, 0, 0))

                pygame.display.flip()
                time.sleep(1)
                question += 1
                randomise_question(question)

    def randomise_question(question):
        global buttons
        buttons = []

        if len(question_dictionary.get(question)) == 3:  #number of given answers = 2 (true/false question)
            values = [1, 2]
            for x in range(2):
                choice = random.choice(values)
                buttons.append(button(20 * size+button_distance*x, height - 270 * size, question_dictionary.get(question)[choice]))   # button1
                values.remove(choice)


        if len(question_dictionary.get(question)) == 5:
            #creates 4 buttons from the button class
            values = [1, 2, 3, 4]

            for x in range(2):
                choice = random.choice(values)
                buttons.append(button(20 * size + button_distance*x, height - 330 * size, question_dictionary.get(question)[choice]))   # button1
                values.remove(choice)

            for x in range(2):
                choice = random.choice(values)
                buttons.append(button(20 * size + button_distance*x, height - 160 * size, question_dictionary.get(question)[choice]))
                values.remove(choice)

        for x in buttons:
            if x.text == question_dictionary.get(question)[1]:
                x.correct = True



    def display_question(background, question_number):
        global buttons

        # screen.blit(background)
        if background == "None":
            screen.fill((0, 0, 255))
        else:
            screen.blit(background, 0, 0)

        question = question_dictionary.get(question_number)[0]  # finds a question stored in the dictionary
        answer = question_dictionary.get(question_number)[1]  # finds a question stored in the dictionary

        pygame.draw.ellipse(screen, (255, 124, 43), pygame.Rect(50*size, 20*size, width-100*size, 100 * size))
        question_title = font.render(str(question), False, (255, 255, 255)) #creates a surface for the question to go on
        text_width = question_title.get_width() # finds the width of the text surface
        screen.blit(question_title, ((width / 2) - (text_width / 2), 40 * size)) #displays the question in the middle of the screen

        #render buttons
        for button in buttons:
            button.display((255, 255, 255))


    randomise_question(question)
    # Game loop.
    while True:
        screen.fill((0, 0, 0))


        display_question("None", question)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                check_mouse_inputs(x, y)

        pygame.display.flip()
        fpsClock.tick(fps)