# Import required libraries
# Inherit required classes
# Create game screen
# Import pictures of characters
# Main menu and start button
# Pictures were all retrieved from disney.fandom.com

# Basic controls:
# Click on buttons to guess character traits - total of 8 guesses
# Click on character portait to guess them as the secret character. Only one guess so make it count!
# Try clicking things multiple times as pygame detection can be wonky.


from team3.ICS3UI.classes_disney import Person

import pygame, random, sys

pygame.init()  # initiate pygame
height = 780  # set height dimension
width = 1200  # set width dimension
screen = pygame.display.set_mode((width, height))  # create screen with given dimensions
BLACK = (0, 0, 0)  # set black color
WHITE = (255, 255, 255)  # set white color
RED = (235, 64, 52)  # set red color
GREEN = (48, 230, 84)  # set green color
BLUE = (48, 127, 230)  # set blue color
GREY = (224, 223, 218)  # set grey color
YELLOW = (220, 237, 66)  # set yellow color
PURPLE = (206, 47, 214)  # set purple color


def main():  # put the main program in a function
    # load character images from pics folder
    image_anita = pygame.image.load("pics/Anita.jpg")
    image_ariel = pygame.image.load("pics/Ariel.jpg")
    image_aurora = pygame.image.load("pics/Aurora.jpg")
    image_belle = pygame.image.load("pics/Belle.jpg")
    image_captain = pygame.image.load("pics/Captain Hook.jpg")
    image_carl = pygame.image.load("pics/Carl Fredricksen.jpg")
    image_doc = pygame.image.load("pics/Doc Dwarf.jpg")
    image_duke = pygame.image.load("pics/Duke of Weselton.jpg")
    image_elsa = pygame.image.load("pics/Elsa.jpg")
    image_esmeralda = pygame.image.load("pics/Esmeralda.jpg")
    image_godmother = pygame.image.load("pics/Fairy Godmother.jpg")
    image_flynn = pygame.image.load("pics/Flynn Rider.jpg")
    image_geppetto = pygame.image.load("pics/Geppetto.jpg")
    image_jafar = pygame.image.load("pics/Jafar.jpg")
    image_jasmine = pygame.image.load("pics/Jasmine.jpg")
    image_jessica = pygame.image.load("pics/Jessica Rabbit.jpg")
    image_john = pygame.image.load("pics/John Darling.jpg")
    image_kristoff = pygame.image.load("pics/Kristoff.jpg")
    image_megara = pygame.image.load("pics/Megara.jpg")
    image_milo = pygame.image.load("pics/Milo Thatch.jpg")
    image_peter = pygame.image.load("pics/Peter Pan.jpg")
    image_rapunzel = pygame.image.load("pics/Rapunzel.jpg")
    image_snow = pygame.image.load("pics/Snow White.jpg")
    image_tarzan = pygame.image.load("pics/Tarzan.jpg")

    # use class Person to create arrays for each character
    anita = Person("anita", "red hair", 'black eyes', 'fair', 'none', 'none', 'glasses', 'none', 'none', 'none', 'none')
    ariel = Person("ariel", 'red hair', 'blue eyes', 'olive', 'none', 'none', 'none', 'none', 'none', 'none', 'none')
    aurora = Person("aurora", 'blonde hair', 'violet eyes', 'pale', 'none', 'none', 'none', 'none', 'none', 'none',
                    'none')
    belle = Person("belle", 'brown hair', 'brown eyes', 'pale', 'none', 'none', 'none', 'none', 'none', 'none', 'none')
    captain = Person("captain ", 'black hair', 'black eyes', 'tan', 'facial_hair', 'none', 'none', 'none', 'big_nose',
                     'none', 'none')
    carl = Person("carl", 'white hair', 'blue eyes', 'pale', 'none', 'elderly', 'glasses', 'none', 'big_nose', 'none',
                  'none')
    doc = Person("doc", 'white hair', 'brown eyes', 'olive', 'facial_hair', 'elderly', 'glasses', 'none', 'big_nose',
                 'none', 'none')
    duke = Person("duke", 'white hair', 'blue eyes', 'olive', 'facial_hair', 'elderly', 'none', 'none', 'big_nose',
                  'none', 'none')
    elsa = Person("elsa", 'blonde hair', 'blue eyes', 'pale', 'none', 'none', 'none', 'pony_tail', 'none', 'none',
                  'none')
    esmeralda = Person("esmeralda", 'black hair', 'green eyes', 'brown', 'none', 'none', 'none', 'pony_tail', 'none',
                       'none', 'earring')
    godmother = Person("godmother", 'white hair', 'black eyes', 'fair', 'none', 'elderly', 'none', 'none', 'none',
                       'none', 'none')
    flynn = Person("flynn", 'brown hair', 'brown eyes', 'tan', 'facial_fair', 'none', 'none', 'none', 'none', 'none',
                   'none')
    geppetto = Person("geppetto", 'white hair', 'blue eyes', 'olive', 'facial_hair', 'elderly', 'glasses', 'none',
                      'none', 'none', 'none')
    jafar = Person("jafar", 'black hair', 'black eyes', 'brown ', 'facial_hair', 'none', 'none', 'none', 'none', 'hat',
                   'none')
    jasmine = Person("jasmine", 'black hair', 'black eyes', 'brown', 'none', 'none', 'none', 'pony_tail', 'none',
                     'none', 'earring')
    jessica = Person("jessica", 'red hair', 'green eyes', 'fair', 'none', 'none', 'none', 'none', 'none', 'none',
                     'earring')
    john = Person("john", 'red hair', 'brown eyes', 'fair', 'none', 'none', 'glasses', 'none', 'none', 'hat', 'none')
    kristoff = Person("kristoff", 'blonde hair', 'brown eyes', 'fair', 'none', 'none', 'none''none', 'none', 'none',
                      'none', 'none')
    megara = Person("megara", 'brown hair', 'violet eyes', 'tan', 'none', 'none', 'none', 'pony_tail', 'none', 'none',
                    'none')
    milo = Person("milo", 'brown hair', 'black eyes', 'tan', 'none', 'none', 'glasses', 'none', 'none', 'none', 'none')
    peter = Person("peter", 'red hair', 'black eyes', 'olive', 'none', 'none', 'none', 'none', 'none', 'hats', 'none')
    rapunzel = Person("rapunzel", 'blonde hair', 'green eyes', 'fair', 'none', 'none', 'none', 'none', 'none', 'none',
                      'none')
    snow = Person("snow white", 'black hair', 'brown eyes', 'pale', 'none', 'none', 'none', 'none', 'none', 'none',
                  'none')
    tarzan = Person("tarzan", 'brown hair', 'green eyes', 'brown', 'none', 'none', 'none', 'none', 'none', 'none',
                    'none')

    # create locations for guess trait questions
    button1clicked = pygame.Rect(1050, 20, 200, 35)
    button2clicked = pygame.Rect(1050, 60, 200, 35)
    button3clicked = pygame.Rect(1050, 100, 200, 35)
    button4clicked = pygame.Rect(1050, 140, 200, 35)
    button5clicked = pygame.Rect(1050, 180, 200, 35)
    button6clicked = pygame.Rect(1050, 220, 200, 35)
    button7clicked = pygame.Rect(1050, 260, 200, 35)
    button8clicked = pygame.Rect(1050, 300, 200, 35)
    button9clicked = pygame.Rect(1050, 340, 200, 35)
    button10clicked = pygame.Rect(1050, 380, 200, 35)
    button11clicked = pygame.Rect(1050, 420, 200, 35)
    button12clicked = pygame.Rect(1050, 460, 200, 35)
    button13clicked = pygame.Rect(1050, 500, 200, 35)
    button14clicked = pygame.Rect(1050, 540, 200, 35)
    button15clicked = pygame.Rect(1050, 580, 200, 35)
    button16clicked = pygame.Rect(1050, 620, 200, 35)
    button17clicked = pygame.Rect(1050, 660, 200, 35)
    button18clicked = pygame.Rect(1050, 700, 200, 35)
    button19clicked = pygame.Rect(1050, 740, 200, 35)
    button20clicked = pygame.Rect(1050, 780, 200, 35)
    button21clicked = pygame.Rect(1050, 820, 200, 35)
    button22clicked = pygame.Rect(1050, 860, 200, 35)

    button1 = pygame.Rect(1050, 20, 200, 35)
    button2 = pygame.Rect(1050, 60, 200, 35)
    button3 = pygame.Rect(1050, 100, 200, 35)
    button4 = pygame.Rect(1050, 140, 200, 35)
    button5 = pygame.Rect(1050, 180, 200, 35)
    button6 = pygame.Rect(1050, 220, 200, 35)
    button7 = pygame.Rect(1050, 260, 200, 35)
    button8 = pygame.Rect(1050, 300, 200, 35)
    button9 = pygame.Rect(1050, 340, 200, 35)
    button10 = pygame.Rect(1050, 380, 200, 35)
    button11 = pygame.Rect(1050, 420, 200, 35)
    button12 = pygame.Rect(1050, 460, 200, 35)
    button13 = pygame.Rect(1050, 500, 200, 35)
    button14 = pygame.Rect(1050, 540, 200, 35)
    button15 = pygame.Rect(1050, 580, 200, 35)
    button16 = pygame.Rect(1050, 620, 200, 35)
    button17 = pygame.Rect(1050, 660, 200, 35)
    button18 = pygame.Rect(1050, 700, 200, 35)
    button19 = pygame.Rect(1050, 740, 200, 35)
    button20 = pygame.Rect(1050, 780, 200, 35)
    button21 = pygame.Rect(1050, 820, 200, 35)
    button22 = pygame.Rect(1050, 860, 200, 35)
    # buttons fors for guessing the character(final guesses mostly)
    button_anita = pygame.Rect(15, 60, 145, 150)
    button_ariel = pygame.Rect(15, 250, 145, 150)
    button_aurora = pygame.Rect(15, 440, 145, 150)
    button_belle = pygame.Rect(15, 630, 145, 150)
    button_captain = pygame.Rect(200, 60, 145, 150)
    button_carl = pygame.Rect(200, 250, 145, 150)
    button_doc = pygame.Rect(200, 440, 145, 150)
    button_duke = pygame.Rect(200, 630, 145, 150)
    button_elsa = pygame.Rect(375, 60, 145, 150)
    button_esmeralda = pygame.Rect(375, 250, 145, 150)
    button_godmother = pygame.Rect(375, 440, 145, 150)
    button_flynn = pygame.Rect(375, 630, 145, 150)
    button_geppetto = pygame.Rect(550, 60, 145, 150)
    button_jafar = pygame.Rect(550, 250, 145, 150)
    button_jasmine = pygame.Rect(550, 440, 145, 150)
    button_jessica = pygame.Rect(550, 630, 145, 150)
    button_john = pygame.Rect(725, 60, 145, 150)
    button_kristoff = pygame.Rect(725, 250, 145, 150)
    button_megara = pygame.Rect(725, 440, 145, 150)
    button_milo = pygame.Rect(725, 630, 145, 150)
    button_peter = pygame.Rect(900, 60, 145, 150)
    button_rapunzel = pygame.Rect(900, 250, 145, 150)
    button_snow = pygame.Rect(900, 440, 145, 150)
    button_tarzan = pygame.Rect(900, 630, 145, 150)

    # fonts of text in buttons
    font_trait = pygame.font.SysFont(None, 30)
    lilfont_trait = pygame.font.SysFont(None, 20)
    # text in buttons for traits
    trait1 = font_trait.render('blonde hair', True, BLACK)
    trait2 = font_trait.render('black hair', True, BLACK)
    trait3 = font_trait.render("brown hair", True, BLACK)
    trait4 = font_trait.render("white hair", True, BLACK)
    trait5 = font_trait.render("red hair", True, BLACK)
    trait6 = font_trait.render("blue eyes", True, BLACK)
    trait7 = font_trait.render("brown eyes", True, BLACK)
    trait8 = font_trait.render("green eyes", True, BLACK)
    trait9 = font_trait.render("black eyes", True, BLACK)
    trait10 = font_trait.render("violet eyes", True, BLACK)
    trait11 = font_trait.render("pale skin", True, BLACK)
    trait12 = font_trait.render("fair skin", True, BLACK)
    trait13 = font_trait.render("olive skin", True, BLACK)
    trait14 = font_trait.render("tan skin", True, BLACK)
    trait15 = font_trait.render("brown skin", True, BLACK)
    trait16 = font_trait.render("facial hair", True, BLACK)
    trait17 = font_trait.render("eldrely", True, BLACK)
    trait18 = font_trait.render("glasses", True, BLACK)
    trait19 = lilfont_trait.render("ponytail/done up hair", True, BLACK)
    trait20 = font_trait.render("big nose", True, BLACK)
    trait21 = font_trait.render("hats", True, BLACK)
    trait22 = font_trait.render("earring", True, BLACK)

    # fonts and texts for the end screen and instructions
    font_endtitle1 = pygame.font.SysFont(None, 200)
    text_endtitle1 = font_endtitle1.render("YOU LOSE", True, RED)

    font_endtitle2 = pygame.font.SysFont(None, 200)
    text_endtitle2 = font_endtitle2.render("YOU WIN", True, YELLOW)

    font_instructions = pygame.font.SysFont(None, 40)
    text_instructions = font_instructions.render("INSTRUCTIONS", True, BLACK)

    # function for rendering pictures on the screen
    def render_picture(character, x, y):
        screen.blit(character, (x, y))

    # pictures for main menu
    disney_title = pygame.image.load('disney.png')
    carl_title = pygame.image.load('carl fredricksen.png')
    elsa_title = pygame.image.load('elsa.png')
    gepetto_title = pygame.image.load('gepetto.png')
    beauty_title = pygame.image.load('beauty.png')

    font_menutitle1 = pygame.font.SysFont(None, 120)
    text_menutitle1 = font_menutitle1.render("GUESS WHO?", True, RED)

    font_menutext = pygame.font.SysFont(None, 40)
    text_menutext = font_menutext.render("Press Enter to play again.", True, BLACK)

    # help button
    helpbutton1 = pygame.Rect(475, 550, 233, 85)
    # picture with instructions of how to play
    howtoplay = pygame.image.load('howtoplay.png')
    # game loops
    running_helpmenu = False
    main_loop = True
    running_mainmenu = True
    running_gamescreen = False
    # loop for end screens
    running_endscreen_lose = False
    running_endscreen_win = False
    # variables for buttons for traits
    button1_avail = True
    button2_avail = True
    button3_avail = True
    button4_avail = True
    button5_avail = True
    button6_avail = True
    button7_avail = True
    button8_avail = True
    button9_avail = True
    button10_avail = True
    button11_avail = True
    button12_avail = True
    button13_avail = True
    button14_avail = True
    button15_avail = True
    button16_avail = True
    button17_avail = True
    button18_avail = True
    button19_avail = True
    button20_avail = True
    button21_avail = True
    button22_avail = True

    blonde_hair_avail = True
    black_hair_avail = True
    brown_hair_avail = True
    white_hair_avail = True
    red_hair_avail = True
    blue_eyes_avail = True
    brown_eyes_avail = True
    green_eyes_avail = True
    black_eyes_avail = True
    violet_eyes_avail = True
    pale_avail = True
    fair_avail = True
    olive_avail = True
    tan_avail = True
    brown_skin_avail = True
    facial_hair_avail = True
    elderly_avail = True
    glasses_avail = True
    ponytail_avail = True
    bignose_avail = True
    hat_avail = True
    earring_avail = True

    button_anita_avail = True
    button_ariel_avail = True
    button_aurora_avail = True
    button_belle_avail = True
    button_captain_avail = True
    button_carl_avail = True
    button_doc_avail = True
    button_duke_avail = True
    button_elsa_avail = True
    button_esmeralda_avail = True
    button_godmother_avail = True
    button_flynn_avail = True
    button_geppetto_avail = True
    button_jafar_avail = True
    button_jasmine_avail = True
    button_jessica_avail = True
    button_john_avail = True
    button_kristoff_avail = True
    button_megara_avail = True
    button_milo_avail = True
    button_peter_avail = True
    button_rapunzel_avail = True
    button_snow_avail = True
    button_tarzan_avail = True

    # all of the character traits
    character_traits = ['blonde hair', 'black hair', 'brown hair', 'white hair', 'red hair', 'blue hair', 'blue eyes',
                        'brown eyes',
                        'green eyes', 'black eyes', 'violet eyes', 'pale skin', 'fair skin', 'olive skin', 'tan skin',
                        'brown skin',
                        'facial hair', 'elderly', 'glasses', 'Ponytail/Done up hair', 'big nose', 'hat', 'earring']

    # game characteres
    characters = [snow, ariel, jafar, captain, tarzan, milo, peter, elsa, carl,
                  geppetto, godmother, duke, doc, jessica, john, rapunzel, anita,
                  belle, esmeralda, flynn, kristoff, jasmine, megara, aurora]

    # pickk  random characteres
    random_character = random.choice(characters)

    random_computer_character = random.choice(characters) \
        # if our guesses are done computer will guess a random character
    final_guess = random.choice(characters)
    print(random_character)
    print(random_computer_character)

    # counts our guesse
    def guess_counter(number):
        font_guess_counter = pygame.font.SysFont(None, 50)
        text_guess_counter = font_guess_counter.render("Number of guesses remaining: " + str(number), True, WHITE)
        screen.blit(text_guess_counter, (200, 850))

    guess_number = random.randrange(0, 22)
    guess = character_traits.pop(guess_number)
    print(guess_number)
    print(guess)
    print(character_traits)
    number_of_guesses = 8  # number of guesses we have

    while main_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # exit pygame
        if running_mainmenu:
            screen.fill(BLUE)  # background color
            screen.blit(text_menutitle1, (500, 100))
            screen.blit(disney_title, (150, 30))
            screen.blit(text_menutext, (430, 500))
            screen.blit(carl_title, (80, 600))
            screen.blit(elsa_title, (800, 600))
            screen.blit(gepetto_title, (30, 400))
            screen.blit(beauty_title, (980, 380))
            pygame.draw.rect(screen, WHITE, helpbutton1)  # help button
            screen.blit(text_instructions, (480, 580))  # instructions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_mainmenu = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running_gamescreen = True
                    running_mainmenu = False  # goes to the main game screen
                if event.type == pygame.QUIT:
                    # exit
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if helpbutton1.collidepoint(mouse_pos):
                        print('Open a help menu')
                        running_helpmenu = True
                        running_mainmenu = False
                    if event.type == pygame.QUIT:
                        # exit
                        sys.exit()

        if running_helpmenu:  # help menu
            screen.fill(WHITE)
            screen.blit(text_menutext, (450, 850))
            screen.blit(howtoplay, (380, 100))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running_helpmenu = False  # exits the help menu
                running_mainmenu = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        if running_gamescreen:
            screen.fill(GREEN)
            guess_counter(number_of_guesses)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # if buttons get clicked the color will change to red
            if button1_avail == True:
                pygame.draw.rect(screen, GREY, button1)
            if button1_avail == False:
                pygame.draw.rect(screen, RED, button1)
            if button2_avail == True:
                pygame.draw.rect(screen, GREY, button2)
            if button2_avail == False:
                pygame.draw.rect(screen, RED, button2)
            if button3_avail == True:
                pygame.draw.rect(screen, GREY, button3)
            if button3_avail == False:
                pygame.draw.rect(screen, RED, button3)
            if button4_avail == True:
                pygame.draw.rect(screen, GREY, button4)
            if button4_avail == False:
                pygame.draw.rect(screen, RED, button4)
            if button5_avail == True:
                pygame.draw.rect(screen, GREY, button5)
            if button5_avail == False:
                pygame.draw.rect(screen, RED, button5)
            if button6_avail == True:
                pygame.draw.rect(screen, GREY, button6)
            if button6_avail == False:
                pygame.draw.rect(screen, RED, button6)
            if button7_avail == True:
                pygame.draw.rect(screen, GREY, button7)
            if button7_avail == False:
                pygame.draw.rect(screen, RED, button7)
            if button8_avail == True:
                pygame.draw.rect(screen, GREY, button8)
            if button8_avail == False:
                pygame.draw.rect(screen, RED, button8)
            if button9_avail == True:
                pygame.draw.rect(screen, GREY, button9)
            if button9_avail == False:
                pygame.draw.rect(screen, RED, button9)
            if button10_avail == True:
                pygame.draw.rect(screen, GREY, button10)
            if button10_avail == False:
                pygame.draw.rect(screen, RED, button10)
            if button11_avail == True:
                pygame.draw.rect(screen, GREY, button11)
            if button11_avail == False:
                pygame.draw.rect(screen, RED, button11)
            if button12_avail == True:
                pygame.draw.rect(screen, GREY, button12)
            if button12_avail == False:
                pygame.draw.rect(screen, RED, button12)
            if button13_avail == True:
                pygame.draw.rect(screen, GREY, button13)
            if button13_avail == False:
                pygame.draw.rect(screen, RED, button13)
            if button14_avail == True:
                pygame.draw.rect(screen, GREY, button14)
            if button14_avail == False:
                pygame.draw.rect(screen, RED, button14)
            if button15_avail == True:
                pygame.draw.rect(screen, GREY, button15)
            if button15_avail == False:
                pygame.draw.rect(screen, RED, button15)
            if button16_avail == True:
                pygame.draw.rect(screen, GREY, button16)
            if button16_avail == False:
                pygame.draw.rect(screen, RED, button16)
            if button17_avail == True:
                pygame.draw.rect(screen, GREY, button17)
            if button17_avail == False:
                pygame.draw.rect(screen, RED, button17)
            if button18_avail == True:
                pygame.draw.rect(screen, GREY, button18)
            if button18_avail == False:
                pygame.draw.rect(screen, RED, button18)
            if button19_avail == True:
                pygame.draw.rect(screen, GREY, button19)
            if button19_avail == False:
                pygame.draw.rect(screen, RED, button19)
            if button20_avail == True:
                pygame.draw.rect(screen, GREY, button20)
            if button20_avail == False:
                pygame.draw.rect(screen, RED, button20)
            if button21_avail == True:
                pygame.draw.rect(screen, GREY, button21)
            if button21_avail == False:
                pygame.draw.rect(screen, RED, button21)
            if button22_avail == True:
                pygame.draw.rect(screen, GREY, button22)
            if button22_avail == False:
                pygame.draw.rect(screen, RED, button22)

            # displays all of the traits on the buttons
            screen.blit(trait1, (1060, 30))
            screen.blit(trait2, (1060, 70))
            screen.blit(trait3, (1060, 110))
            screen.blit(trait4, (1060, 150))
            screen.blit(trait5, (1060, 190))
            screen.blit(trait6, (1060, 230))
            screen.blit(trait7, (1060, 270))
            screen.blit(trait8, (1060, 310))
            screen.blit(trait9, (1060, 350))
            screen.blit(trait10, (1060, 390))
            screen.blit(trait11, (1060, 430))
            screen.blit(trait12, (1060, 470))
            screen.blit(trait13, (1060, 510))
            screen.blit(trait14, (1060, 550))
            screen.blit(trait15, (1060, 590))
            screen.blit(trait16, (1060, 630))
            screen.blit(trait17, (1060, 670))
            screen.blit(trait18, (1060, 710))
            screen.blit(trait19, (1060, 750))
            screen.blit(trait20, (1060, 790))
            screen.blit(trait21, (1060, 830))
            screen.blit(trait22, (1060, 870))

            # renders pictures of the character to the screen. if a button is clicked that trait will get unavailabe
            # and it will not render to the screen
            if blonde_hair_avail == True and violet_eyes_avail == True and pale_avail == True:
                render_picture(image_aurora, 15, 440)
                button_aurora_avail = True

            if blonde_hair_avail == True and blue_eyes_avail == True and pale_avail == True and ponytail_avail == True:
                render_picture(image_elsa, 375, 60)
                button_elsa_avail = True

            if blonde_hair_avail == True and green_eyes_avail == True and fair_avail == True:
                render_picture(image_rapunzel, 900, 250)
                button_rapunzel_avail = True

            if blonde_hair_avail == True and brown_eyes_avail == True and fair_avail == True:
                render_picture(image_kristoff, 725, 250)
                button_kristoff_avail = True

            if red_hair_avail == True and black_eyes_avail == True and fair_avail == True and glasses_avail == True:
                render_picture(image_anita, 15, 60)
                button_anita_avail = True

            if red_hair_avail == True and blue_eyes_avail == True and olive_avail == True:
                render_picture(image_ariel, 15, 250)
                button_ariel_avail = True

            if red_hair_avail == True and green_eyes_avail == True and fair_avail == True and earring_avail == True:
                render_picture(image_jessica, 550, 630)
                button_jessica_avail = True

            if red_hair_avail == True and black_eyes_avail == True and olive_avail == True and hat_avail == True:
                render_picture(image_peter, 900, 60)
                button_peter_avail = True

            if red_hair_avail == True and brown_eyes_avail == True and fair_avail == True and glasses_avail == True and hat_avail == True:
                render_picture(image_john, 725, 60)
                button_john_avail = True

            if brown_hair_avail == True and brown_eyes_avail == True and pale_avail == True:
                render_picture(image_belle, 15, 630)
                button_belle_avail = True

            if brown_hair_avail == True and brown_eyes_avail == True and tan_avail == True and facial_hair_avail == True:
                render_picture(image_flynn, 375, 630)
                button_flynn_avail = True

            if brown_hair_avail == True and green_eyes_avail == True and brown_skin_avail == True:
                render_picture(image_tarzan, 900, 630)
                button_tarzan_avail = True

            if brown_hair_avail == True and black_eyes_avail == True and tan_avail == True and glasses_avail == True:
                render_picture(image_milo, 725, 630)
                button_milo_avail = True

            if brown_hair_avail == True and violet_eyes_avail == True and tan_avail == True and earring_avail == True and ponytail_avail == True:
                render_picture(image_megara, 725, 440)
                button_megara_avail = True

            if black_hair_avail == True and black_eyes_avail == True and tan_avail == True and bignose_avail == True and facial_hair_avail == True and hat_avail == True:
                render_picture(image_captain, 200, 60)
                button_captain_avail = True

            if black_hair_avail == True and green_eyes_avail == True and brown_skin_avail == True and earring_avail == True and ponytail_avail == True:
                render_picture(image_esmeralda, 375, 250)
                button_esmeralda_avail = True

            if black_hair_avail == True and black_eyes_avail == True and brown_skin_avail == True and earring_avail == True and ponytail_avail == True:
                render_picture(image_jasmine, 550, 440)
                button_jasmine_avail = True

            if black_hair_avail == True and black_eyes_avail == True and brown_skin_avail == True and hat_avail == True and facial_hair_avail == True:
                render_picture(image_jafar, 550, 250)
                button_jafar_avail = True

            if black_hair_avail == True and brown_eyes_avail == True and pale_avail == True:
                render_picture(image_snow, 900, 440)
                button_snow_avail = True

            if white_hair_avail == True and blue_eyes_avail == True and pale_avail == True and bignose_avail == True and glasses_avail == True and elderly_avail == True:
                render_picture(image_carl, 200, 250)
                button_carl_avail = True

            if white_hair_avail == True and brown_eyes_avail == True and olive_avail == True and bignose_avail == True and elderly_avail == True and glasses_avail == True and facial_hair_avail == True and hat_avail == True:
                render_picture(image_doc, 200, 440)
                button_doc_avail = True

            if white_hair_avail == True and blue_eyes_avail == True and facial_hair_avail == True and elderly_avail == True and olive_avail == True and bignose_avail == True:
                render_picture(image_duke, 200, 630)
                button_duke_avail = True

            if white_hair_avail == True and black_eyes_avail == True and elderly_avail == True and hat_avail == True and fair_avail == True:
                render_picture(image_godmother, 375, 440)
                button_godmother_avail = True

            if white_hair_avail == True and blue_eyes_avail == True and olive_avail == True and facial_hair_avail == True and glasses_avail == True and elderly_avail == True:
                render_picture(image_geppetto, 550, 60)
                button_geppetto_avail = True

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos  # finds the mouse pos
                        # if the mouse pos matches the button and we still have guesses:
                        if button1.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button1clicked)  # button will get red
                            button1_avail = False
                            number_of_guesses -= 1  # we have one less more guesses
                            print(number_of_guesses)
                            if random_character.hair == 'blonde hair':  # if random character matches the button trait
                                print('blonde hair')
                                blonde_hair_avail = True
                                black_hair_avail = False  # deletes characters that do not match the button trait
                                brown_hair_avail = False
                                white_hair_avail = False
                                red_hair_avail = False
                            if random_character.hair != 'blonde hair':  # if random character does not match the button trait
                                print('no blonde hair')
                                blonde_hair_avail = False  # deletes characters that match this trait

                        if button2.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button2clicked)
                            button2_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.hair == 'black hair':
                                print('black hair')
                                black_hair_avail = True
                                blonde_hair_avail = False
                                brown_hair_avail = False
                                white_hair_avail = False
                                red_hair_avail = False
                            if random_character.hair != 'black hair':
                                print('no black hair')
                                black_hair_avail = False

                        if button3.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button3clicked)
                            button3_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.hair == 'brown hair':
                                print('brown hair')
                                brown_hair_avail = True
                                black_hair_avail = False
                                blonde_hair_avail = False
                                white_hair_avail = False
                                red_hair_avail = False
                            if random_character.hair != 'brown hair':
                                print('no brown hair')
                                brown_hair_avail = False

                        if button4.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button4clicked)
                            button4_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.hair == 'white hair':
                                print('white hair')
                                white_hair_avail = True
                                black_hair_avail = False
                                blonde_hair_avail = False
                                brown_hair_avail = False
                                red_hair_avail = False
                            if random_character.hair != 'white hair':
                                print('no white hair')
                                white_hair_avail = False

                        if button5.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button5clicked)
                            button5_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.hair == 'red hair':
                                print('red hair')
                                red_hair_avail = True
                                black_hair_avail = False
                                blonde_hair_avail = False
                                brown_hair_avail = False
                                white_hair_avail = False
                            if random_character.hair != 'red hair':
                                print('no red hair')
                                red_hair_avail = False

                        if button6.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button6clicked)
                            button6_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.eye == 'blue eyes':
                                print(" blue eye")
                                blue_eyes_avail = True
                                brown_eyes_avail = False
                                green_eyes_avail = False
                                black_eyes_avail = False
                                violet_eyes_avail = False
                            if random_character.eye != 'blue eyes':
                                print(' no blue eyes')
                                blue_eyes_avail = False

                        if button7.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button7clicked)
                            button7_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.eye == 'brown eyes':
                                print("brown eyes")
                                blue_eyes_avail = False
                                brown_eyes_avail = True
                                green_eyes_avail = False
                                black_eyes_avail = False
                                violet_eyes_avail = False
                            if random_character.eye != 'brown eyes':
                                print(' no brown eyes')
                                brown_eyes_avail = False

                        if button8.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button8clicked)
                            button8_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.eye == 'green eyes':
                                print("green eyes")
                                blue_eyes_avail = False
                                brown_eyes_avail = False
                                green_eyes_avail = True
                                black_eyes_avail = False
                                violet_eyes_avail = False
                            if random_character.eye != 'green eyes':
                                print(' no green eyes')
                                green_eyes_avail = False

                        if button9.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button9clicked)
                            button9_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.eye == 'black eyes':
                                print("black eyes")
                                blue_eyes_avail = False
                                brown_eyes_avail = False
                                green_eyes_avail = False
                                black_eyes_avail = True
                                violet_eyes_avail = False
                            if random_character.eye != 'black eyes':
                                print(' no black eyes')
                                black_eyes_avail = False

                        if button10.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button10clicked)
                            button10_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.eye == 'violet eyes':
                                print("violet eyes")
                                blue_eyes_avail = False
                                brown_eyes_avail = False
                                green_eyes_avail = False
                                black_eyes_avail = False
                                violet_eyes_avail = True
                            if random_character.eye != 'violet eyes':
                                print(' no violet eyes')
                                violet_eyes_avail = False

                        if button11.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button11clicked)
                            button11_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.skin == 'pale':
                                print("pale skin")
                                pale_avail = True
                                fair_avail = False
                                olive_avail = False
                                brown_skin_avail = False
                                tan_avail = False
                            if random_character.skin != 'pale':
                                print('no pale skin')
                                pale_avail = False

                        if button12.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button12clicked)
                            button12_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.skin == 'fair':
                                print("fair skin")
                                pale_avail = False
                                fair_avail = True
                                olive_avail = False
                                brown_skin_avail = False
                                tan_avail = False
                            if random_character.skin != 'fair':
                                print('no fair skin')
                                fair_avail = False

                        if button13.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button13clicked)
                            button13_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.skin == 'olive':
                                print("olive skin")
                                pale_avail = False
                                fair_avail = False
                                olive_avail = True
                                brown_skin_avail = False
                                tan_avail = False
                            if random_character.skin != 'olive':
                                print('no olive skin')
                                olive_avail = False

                        if button14.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button14clicked)
                            button14_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.skin == 'tan':
                                print("tan skin")
                                pale_avail = False
                                fair_avail = False
                                olive_avail = False
                                brown_skin_avail = False
                                tan_avail = True
                            if random_character.skin != 'tan':
                                print('no tan skin')
                                tan_avail = False

                        if button15.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button15clicked)
                            button15_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.skin == 'brown':
                                print("brown skin")
                                pale_avail = False
                                fair_avail = False
                                olive_avail = False
                                brown_skin_avail = True
                                tan_avail = False

                            if random_character.skin != 'brown':
                                print('no brown skin')
                                brown_skin_avail = False

                        if button16.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button16clicked)
                            button16_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.facial_hair == 'none':
                                print("No facial")
                                facial_hair_avail = False
                            if random_character.facial_hair == 'facial_hair':
                                print("Facial")
                                facial_hair_avail = True

                        if button17.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button17clicked)
                            button17_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.elderly == 'none':
                                print("No elderly")
                                elderly_avail = False
                            if random_character.elderly == 'elderly':
                                print("elderly")
                                elderly_avail = True
                        if button18.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button18clicked)
                            button18_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.glasses == 'none':
                                print('No glasses')
                                glasses_avail = False
                            if random_character.glasses == 'glasses':
                                print("glasses")
                                glasses_avail = True

                        if button19.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button19clicked)
                            button19_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.pony_tail == 'none':
                                print('No pony tail')
                                ponytail_avail = False
                            if random_character.pony_tail == 'pony_tail':
                                print('Pony tail')
                                ponytail_avail = True

                        if button20.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button20clicked)
                            button20_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.big_nose == 'none':
                                print('no big nose')
                                bignose_avail = False
                            if random_character.big_nose == 'big_nose':
                                print('big nose')
                                bignose_avail = True

                        if button21.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button21clicked)
                            button21_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.hats == 'none':
                                print('no hats')
                                hat_avail = False
                            if random_character.hats == 'hat':
                                print('hats')
                                bignose_avail = True

                        if button22.collidepoint(mouse_pos) and number_of_guesses > 0:
                            pygame.draw.rect(screen, RED, button22clicked)
                            button22_avail = False
                            number_of_guesses -= 1
                            print(number_of_guesses)
                            if random_character.earring == 'none':
                                print('no earrings')
                                earring_avail = False
                            if random_character.earring == 'earring':
                                print('earrings')
                                earring_avail = True

                        if button_anita_avail == True:  # guessing the character
                            if button_anita.collidepoint(mouse_pos):  # if mouse pos matches the character picture
                                if random_character.name == 'anita':  # if random characters name matches this name
                                    running_endscreen_win = True  # win screen display
                                    running_gamescreen = False

                                if random_character.name != 'anita':  # if random characters name doesnt matches this name
                                    running_endscreen_lose = True  # lose screen display
                                    running_gamescreen = False

                        if button_ariel_avail == True:
                            if button_ariel.collidepoint(mouse_pos):
                                if random_character.name == 'ariel':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'ariel':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_aurora_avail == True:
                            if button_aurora.collidepoint(mouse_pos):
                                if random_character.name == 'aurora':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'aurora':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_belle_avail == True:
                            if button_belle.collidepoint(mouse_pos):
                                if random_character.name == 'belle':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'belle':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_captain_avail == True:
                            if button_captain.collidepoint(mouse_pos):
                                if random_character.name == 'captain':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'captain':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_carl_avail == True:
                            if button_carl.collidepoint(mouse_pos):
                                if random_character.name == 'carl':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'carl':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_doc_avail == True:
                            if button_doc.collidepoint(mouse_pos):
                                if random_character.name == 'doc':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'doc':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_duke_avail == True:
                            if button_duke.collidepoint(mouse_pos):
                                if random_character.name == 'duke':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'duke':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_elsa_avail == True:
                            if button_elsa.collidepoint(mouse_pos):
                                if random_character.name == 'elsa':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'elsa':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_esmeralda_avail == True:
                            if button_esmeralda.collidepoint(mouse_pos):
                                if random_character.name == 'esmeralda':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'esmeralda':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_godmother_avail == True:
                            if button_godmother.collidepoint(mouse_pos):
                                if random_character.name == 'godmother':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'godmother':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_flynn_avail == True:
                            if button_flynn.collidepoint(mouse_pos):
                                if random_character.name == 'flynn':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'flynn':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_geppetto_avail == True:
                            if button_geppetto.collidepoint(mouse_pos):
                                if random_character.name == 'geppetto':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'geppetto':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_jafar_avail == True:
                            if button_jafar.collidepoint(mouse_pos):
                                if random_character.name == 'jafar':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'jafar':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_jasmine_avail == True:
                            if button_jasmine.collidepoint(mouse_pos):
                                if random_character.name == 'jasmine':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'jasmine':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_jessica_avail == True:
                            if button_jessica.collidepoint(mouse_pos):
                                if random_character.name == 'jessica':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'jessica':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_john_avail == True:
                            if button_john.collidepoint(mouse_pos):
                                if random_character.name == 'john':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'john':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_kristoff_avail == True:
                            if button_kristoff.collidepoint(mouse_pos):
                                if random_character.name == 'kristoff':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'kristoff':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_megara_avail == True:
                            if button_megara.collidepoint(mouse_pos):
                                if random_character.name == 'megara':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'megara':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_milo_avail == True:
                            if button_milo.collidepoint(mouse_pos):
                                if random_character.name == 'milo':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'milo':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_peter_avail == True:
                            if button_peter.collidepoint(mouse_pos):
                                if random_character.name == 'peter':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'peter':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_rapunzel_avail == True:
                            if button_rapunzel.collidepoint(mouse_pos):
                                if random_character.name == 'rapunzel':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'rapunzel':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_snow_avail == True:
                            if button_snow.collidepoint(mouse_pos):
                                if random_character.name == 'snow':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'snow':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if button_tarzan_avail == True:
                            if button_tarzan.collidepoint(mouse_pos):
                                if random_character.name == 'tarzan':
                                    running_endscreen_win = True
                                    running_gamescreen = False
                                if random_character.name != 'tarzan':
                                    running_endscreen_lose = True
                                    running_gamescreen = False

                        if guess_number == 1 and final_guess == random_computer_character:  # if we have one more guess
                            running_endscreen_lose = True  # and AI random guess is correct display lose screen
                            running_gamescreen = False

        if running_endscreen_lose:
            screen.fill(PURPLE)
            screen.blit(text_endtitle1, (250, 400))
            screen.blit(disney_title, (430, 200))
            screen.blit(text_menutext, (430, 600))
            stats = open('previous_match_statistic.txt', 'w')  # write to txt file
            guesses_taken = 8 - number_of_guesses  # number of guesses taken by the player
            stats.write("You guessed " + str(guesses_taken) + ' traits')  # write statistics of match into the txt file
            stats.write('\nYour secret character was ' + str(random_character.name))
            stats.write('\nYou lost this match!')
            stats.close()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_mainmenu = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    print("press")
                    main()  # restarts the function for playing the game again
                if event.type == pygame.QUIT:
                    # exit
                    sys.exit()

        if running_endscreen_win:
            screen.fill(GREEN)
            screen.blit(text_endtitle2, (280, 400))
            screen.blit(disney_title, (430, 200))
            screen.blit(text_menutext, (430, 600))
            stats = open('previous_match_statistic.txt', 'w')
            guesses_taken = 8 - number_of_guesses
            stats.write("You guessed " + str(guesses_taken) + ' traits')
            stats.write('\nYour secret character was ' + str(random_character.name))
            stats.write('\nYou won this match!')
            stats.close()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_mainmenu = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    main()
                if event.type == pygame.QUIT:
                    # exit
                    sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        pygame.display.update()  # update the screen


main()  # runs the function