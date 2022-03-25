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

    import pygame
    from pygame.locals import *

    pygame.init()  # starts pygame

    # frames per second setup
    fps = 60
    fpsClock = pygame.time.Clock()
    size = 1 # this variable scales all the screen sizes and buttons

    # screen setup
    width, height = 900 * size, 480 * size
    screen = pygame.display.set_mode((width, height))
    font_size = round(40 * size)

    font = pygame.font.SysFont('Comic Sans MS', font_size) # font for the title
    font2 = pygame.font.SysFont('Comic Sans MS', round(30*size)) # font for the title

    button_size_x = 400 * size
    button_size_y = 150 * size
    button_distance = 460 * size

    # constants and colours

    # variables, dictionaries and lists
    question = 1
    question_dictionary = {1: ["what is 1+1", "2", "window", "11", "IDK"], #question dictionary holds all the questions and answer
                           2: ["5 + b = 12,  what is the value of b", "7", "2", "5", "what?"],
                           3: ["10 x 4 = 40", "True", "False"],
                           4: ["10 x 4 = 40", "True", "False"],
                           5: ["10 x 4 = 40", "True", "False"],
                           6: ["10 x 4 = 40", "True", "False"],
                           7: ["10 x 4 = 40", "True", "False"],
                           8: ["10 x 4 = 40", "True", "False"]

                           }


    # print(question_dictionary.get((question))[0]) TEST

    class button:
        def __init__(self, x, y, text):
            self.clicked = False
            self.correct = None
            self.x = x
            self.y = y
            self.text = text

            if self.clicked == True:
                self.colour = (200, 200, 200)
            else:
                self.colour = (255, 255, 255)
        def display(self):
            pygame.draw.rect(screen, self.colour, pygame.Rect(self.x, self.y, button_size_x, button_size_y)) #draws button onto the screen


            text = font2.render(self.text, False, (0, 0, 0)) #sets up text surface
            text_width = text.get_width()  # gets text width
            text_height = text.get_height()
            screen.blit(text, (self.x+button_size_x/2-text_width/2, self.y+button_size_y/2-text_width/4)) #displays text surface perfectly centred using the text width

    def check_mouse_inputs(x, y):

        for button in buttons:
            if button.x+button_size_x > x and button.x < x and button.y+button_size_y > y and button.y < y: #clicking on the button
                print(button.text)



    def ask_question(background, question_number):
        global buttons
        buttons = []
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
        #print(len(question_dictionary.get(question_number)))
        if len(question_dictionary.get(question_number)) == 3:  #number of given answers = 2 (true/false question)
            b1 = button(20*size, height-330*size, answer)
            b2 = button(20*size+button_distance, height-330*size, question_dictionary.get(question_number)[2])
            b1.display()
            b2.display()
        if len(question_dictionary.get(question_number)) == 5:

            b1 = button(20 * size, height - 330 * size, question_dictionary.get(question_number)[1])
            b2 = button(20 * size + button_distance, height - 330 * size, question_dictionary.get(question_number)[2])
            b3 = button(20 * size, height - 160 * size, question_dictionary.get(question_number)[3])
            b4 = button(20 * size + button_distance, height - 160 * size, question_dictionary.get(question_number)[4])

            b1.display()
            b2.display()
            b3.display()
            b4.display()

            buttons.append(b1)
            buttons.append(b2)
            buttons.append(b3)
            buttons.append(b4)




    # Game loop.
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                check_mouse_inputs(x, y)

        # Update.
        ask_question("None", question)

        # Draw.

        pygame.display.flip()
        fpsClock.tick(fps)