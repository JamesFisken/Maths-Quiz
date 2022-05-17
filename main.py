if __name__ == '__main__':
    # imports
    import sys  # imports system module for sys.exit to close the quiz
    import random #for randomizing questions
    import pygame #for displaying the quiz
    import time #for adding delay
    from pygame.locals import *

    pygame.init()  # starts pygame

    # frames per second setup
    fps = 60
    fpsClock = pygame.time.Clock()
    size = 1 # this variable scales all the screen sizes and buttons
    # screen setup

    def init(): #sets up all necassery variables and globalises them
        global width, height, screen, font_size, font, font2, button_size_x, button_size_y, button_distance
        width, height = 900 * size, 480 * size

        screen = pygame.display.set_mode((width, height))  #sets screen to the main display surface

        font = pygame.font.SysFont('Arial', round(32 * size)) # font for the title
        font2 = pygame.font.SysFont('Comic sans', round(40*size)) # font for the buttons

        button_size_x = 420 * size
        button_size_y = 150 * size
        button_distance = 440 * size

    init()

    # constants and colours

    # variables, dictionaries and lists
    question = 1
    score = 0
    question_dictionary = {1: ["what is 1+1", "2", "window", "11", "IDK",], #question dictionary holds all the questions and answer
                           2: ["5 + b = 12,  what is the value of b", "7", "2", "5", "what?"],
                           3: ["there were 5 birds, 2 flew away. how many birds are left?", "3", "1000000000", "4", "whats a bird"],
                           4: ["10 x 4 = 40", "True", "False"],
                           5: ["20 - 10 = 5", "False", "True"],
                           6: ["3 + 8 x 3", "27", "33"],
                           7: ["what is 8 x 8", "64", "16", "88", "42"],
                           8: ["what is 12 ÷ 3", "4", "2", "3", "9"],
                           9: ["9 x 9", "81", "36", "72", "18"],
                           10: ["a square has a width of 5, what is the area of the square", "25", "not enough infomation", "5", "20"],
                           11: ["8-4*8", "-24", "24"],
                           12: ["9 x 6 = 54", "True", "False"],
                           13: ["16 / 4", "4", "3", "2", "8"],
                           14: ["8+8+8+8+8", "40", "32", "48", "8"],
                           15: ["what is 12 x 8", "96", "48", "112", "92"],
                           16: ["20 x 20", "400", "4400", "40", "440"],
                           17: ["what is 9 x 5 x 2?", "90", "952"],
                           18: ["You scored      %,", "True", "False"]


                           }

    class Button: #creates class for the buttons
        def __init__(self, x, y, text):

            self.correct = False
            self.x = x
            self.y = y
            self.text = text #text that displays on the button


        def display(self, colour):

            pygame.draw.rect(screen, colour, pygame.Rect(self.x, self.y, button_size_x, button_size_y)) #draws button onto the screen
            text = font2.render(self.text, False, (0, 0, 0)) #sets up text surface
            text_width = text.get_width()  # gets text width
            text_height = text.get_height() # gets text height
            screen.blit(text, (self.x+button_size_x/2-text_width/2, self.y+button_size_y/2-text_height/2)) #displays text surface perfectly centred using the text width and height
    def get_statistics(score): #should run after doing all the questions
        if int(score) > 70: # greater than 70% results in a pass
            score_text = font.render(score, False, (0, 255, 0)) #text is gonna be green (pass)
        else:
            score_text = font.render(score, False, (255, 0, 0)) #text is gonna be red (fail)
        display_question("None", question) #just displays an empty question
        screen.blit(score_text, (485*size, 50*size))
        pygame.display.update() #updates the screen to display the changes

        time.sleep(4) #adds some display before stopping the quiz

        pygame.quit() #quits pygame
        exit() #ends program




    def check_mouse_inputs(x, y):
        global question
        global score

        for button in buttons: #loops through every button
            if button.x+button_size_x > x and button.x < x and button.y+button_size_y > y and button.y < y: #clicking on the button
                if button.correct: #if the button has the attribute "Correct = True" has been clicked then the user has inputed the right answer
                    button.display((0, 255, 0)) #displays green to symbolise that they got the question correct
                    score += 1

                elif button.correct == False:
                    button.display((255, 0, 0)) #displays red to symbolise that they got the question wrong

                    for button in buttons: #loops through every button
                        if button.correct:  # if the button has the attribute "Correct = True"
                            button.display((0, 255, 0)) #make the button display green
                    pygame.display.flip() #update the screen
                    pygame.time.wait(2000) #waits extra time(since they got the question wrong)

                pygame.display.flip() #updates the screen
                pygame.time.wait(500) #adds delay

                question += 1 #goes to the next question

                randomise_question(question) #randomisises question answers

    def randomise_question(question):
        global buttons
        buttons = []
        if question < len(question_dictionary):

            if len(question_dictionary.get(question)) == 3:  #number of given answers = 2 (true/false question)
                values = [1, 2]
                for x in range(2): #loops 2 times
                    choice = random.choice(values)
                    buttons.append(Button(20 * size+button_distance*x, height - 270 * size, question_dictionary.get(question)[choice]))   # button
                    values.remove(choice)


            if len(question_dictionary.get(question)) == 5: #number of given answers = 4
                #creates 4 buttons from the button class
                values = [1, 2, 3, 4]

                for x in range(2): #loops 2 times
                    choice = random.choice(values)
                    buttons.append(Button(20 * size + button_distance*x, height - 338 * size, question_dictionary.get(question)[choice]))   # button
                    values.remove(choice)

                for x in range(2): #loops 2 times
                    choice = random.choice(values)
                    buttons.append(Button(20 * size + button_distance*x, height - 168 * size, question_dictionary.get(question)[choice]))  #button
                    values.remove(choice)

            for x in buttons:
                if x.text == question_dictionary.get(question)[1]:
                    x.correct = True
        else:
            get_statistics(str(round(score / (len(question_dictionary) - 1) * 100)))


    def display_question(background, question_number):
        global buttons

        screen.fill((0, 0, 255)) #displays background

        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 0, 80 * size, 40 * size))  # draws a rectangle around the question counter for visibility

        #sets up question counter display
        # i have to do this manually because the syntax for for displaying text is very strange/specific
        #idealy the proceding code wouldn't be as repetitive
        text_1 = str(question_number)
        text_2 = "/"
        text_3 = str(len(question_dictionary)-1)

        question_number_text_1 = font.render(text_1, False, (0, 0, 0))  #creates a surface
        question_number_text_2 = font.render(text_2, False, (0, 0, 0)) #creates a surface
        question_number_text_3 = font.render(text_3, False, (0, 0, 0)) #creates a surface

        screen.blit(question_number_text_1, (1 * size, -1 * size)) #displays the surface
        screen.blit(question_number_text_2, (25 * size, -1 * size)) #displays the surface
        screen.blit(question_number_text_3, (45 * size, -1 * size)) #displays the surface

        pygame.draw.ellipse(screen, (247, 95, 7), pygame.Rect(50 * size, 20 * size, width - 100 * size, 100 * size))  # draws orange eclipse around the question

        question = question_dictionary.get(question_number)[0]  # finds a question stored in the dictionary at the dedicated question number




        question_title = font.render(str(question), False, (255, 255, 255)) #creates a surface for the question to go on
        text_width = question_title.get_width()  # finds the width of the text surface
        screen.blit(question_title, ((width / 2) - (text_width / 2), 50 * size))  # displays the question in the middle of the screen



        #render buttons
        for button in buttons:
            button.display((255, 255, 255)) #displays all buttons



    randomise_question(question)
    # Game loop.
    while True:

        display_question("None", question) #displays the screen at the relevant question number


        for event in pygame.event.get():
            if event.type == QUIT: #if the red X is clicked
                pygame.quit() #close pygame
                sys.exit() #close program
            if event.type == pygame.MOUSEBUTTONDOWN: # if mouse down
                x, y = pygame.mouse.get_pos() #gets the mouse coords
                check_mouse_inputs(x, y) #passes these coords into a function
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS or event.key == pygame.K_MINUS:
                    if event.key == pygame.K_EQUALS and size < 3:
                        size += 0.1
                    if event.key == pygame.K_MINUS and size > 0.2:
                        size -= 0.1
                    init()
                    randomise_question(question)


        pygame.display.flip()
        fpsClock.tick(fps)