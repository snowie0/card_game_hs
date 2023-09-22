# Import required libraries
# Inherit required classes
# Create game screen
# Import pictures of characters
# Main menu and start button
from team3.ICS3UI.classes_disney import Person

import pygame, random, sys

# s
pygame.init()

height = 990

width = 1300
screen = pygame.display.set_mode((width, height))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (235, 64, 52)
GREEN = (48, 230, 84)
BLUE = (48, 127, 230)
GREY = (224, 223, 218)

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

anita = Person("anita", "red hair", 'black eyes', 'fair', 'none', 'none', 'glasses', 'none', 'none', 'none', 'none')
ariel = Person("ariel", 'red hair', 'blue eyes', 'olive', 'none', 'none', 'none', 'none', 'none', 'none', 'none')
aurora = Person("aurora", 'blonde hair', 'violet eyes', 'pale', 'none', 'none', 'none', 'none', 'none', 'none', 'none')
belle = Person("belle", 'brown hair', 'brown eyes', 'pale', 'none', 'none', 'none', 'none', 'none', 'none', 'none')
captain = Person("captain ", 'black hair', 'black eyes', 'tan', 'facial_hair', 'none', 'none', 'none', 'big_nose',
                 'none', 'none')
carl = Person("carl", 'white hair', 'blue eyes', 'pale', 'none', 'elderly', 'glasses', 'none', 'big_nose', 'none',
              'none')
doc = Person("doc", 'white hair', 'brown eyes', 'olive', 'facial_hair', 'elderly', 'glasses', 'none', 'big_nose',
             'none', 'none')
duke = Person("duke", 'white hair', 'blue eyes', 'olive', 'facial_hair', 'elderly', 'none', 'none', 'big_nose', 'none',
              'none')
elsa = Person("elsa", 'blonde hair', 'blue eyes', 'pale', 'none', 'none', 'none', 'pony_tail', 'none', 'none', 'none')
esmeralda = Person("esmeralda", 'black hair', 'green eyes', 'brown', 'none', 'none', 'none', 'pony_tail', 'none',
                   'none', 'earring')
godmother = Person("godmother", 'white hair', 'black eyes', 'fair', 'none', 'elderly', 'none', 'none', 'none', 'none',
                   'none')
flynn = Person("flynn", 'brown hair', 'brown eyes', 'tan', 'facial_fair', 'none', 'none', 'none', 'none', 'none',
               'none')
geppetto = Person("geppetto", 'white hair', 'blue eyes', 'olive', 'facial_hair', 'elderly', 'glasses', 'none', 'none',
                  'none', 'none')
jafar = Person("jafar", 'black hair', 'black eyes', 'brown ', 'facial_hair', 'none', 'none', 'none', 'none', 'hat',
               'none')
jasmine = Person("jasmine", 'black hair', 'black eyes', 'brown', 'none', 'none', 'none', 'pony_tail', 'none', 'none',
                 'earring')
jessica = Person("jessica", 'red hair', 'green eyes', 'fair', 'none', 'none', 'none', 'none', 'none', 'none', 'earring')
john = Person("john", 'red hair', 'brown eyes', 'fair', 'none', 'none', 'glasses', 'none', 'none', 'hat', 'none')
kristoff = Person("kristoff", 'blonde hair', 'brown eyes', 'fair', 'none', 'none', 'none''none', 'none', 'none', 'none',
                  'none')
megara = Person("megara", 'brown hair', 'violet eyes', 'tan', 'none', 'none', 'none', 'pony_tail', 'none', 'none',
                'none')
milo = Person("milo", 'brown hair', 'black eyes', 'tan', 'none', 'none', 'glasses', 'none', 'none', 'none', 'none')
peter = Person("peter", 'red hair', 'black eyes', 'olive', 'none', 'none', 'none', 'none', 'none', 'hats', 'none')
rapunzel = Person("rapunzel", 'blonde hair', 'green eyes', 'fair', 'none', 'none', 'none', 'none', 'none', 'none',
                  'none')
snow = Person("snow white", 'black hair', 'brown eyes', 'pale', 'none', 'none', 'none', 'none', 'none', 'none', 'none')
tarzan = Person("tarzan", 'brown hair', 'green eyes', 'brown', 'none', 'none', 'none', 'none', 'none', 'none', 'none')

# check point 1
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

font_trait = pygame.font.SysFont(None, 30)
lilfont_trait = pygame.font.SysFont(None, 20)

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


def render_picture(character, x, y):
    screen.blit(character, (x, y))


disney_title = pygame.image.load('disney.png')
carl_title = pygame.image.load('carl fredricksen.png')
elsa_title = pygame.image.load('elsa.png')
gepetto_title = pygame.image.load('gepetto.png')
beauty_title = pygame.image.load('beauty.png')

font_menutitle1 = pygame.font.SysFont(None, 120)
text_menutitle1 = font_menutitle1.render("GUESS WHO?", True, RED)

font_menutext = pygame.font.SysFont(None, 40)
text_menutext = font_menutext.render("Press Enter to continue.", True, BLACK)

# Arrays start here


main_loop = True
running_mainmenu = True
running_gamescreen = False
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

character_traits = ['blonde hair', 'black hair', 'brown hair', 'white hair', 'red hair', 'blue hair', 'blue eyes',
                    'brown eyes',
                    'green eyes', 'black eyes', 'violet eyes', 'pale skin', 'fair skin', 'olive skin', 'tan skin',
                    'brown skin',
                    'facial hair', 'elderly', 'glasses', 'Ponytail/Done up hair', 'big nose', 'hat', 'earring']

characters = [snow, ariel, jafar, captain, tarzan, milo, peter, elsa, carl,
              geppetto, godmother, duke, doc, jessica, john, rapunzel, anita,
              belle, esmeralda, flynn, kristoff, jasmine, megara, aurora]

Blonde_hair = [snow, rapunzel, aurora, kristoff]
Black_hair = [snow, jafar, captain, esmeralda, jasmine]
Brown_hair = [tarzan, milo, belle, flynn, megara]
White_hair = [carl, geppetto, godmother, duke, doc]
Red_hair = [ariel, jessica, peter, john, anita]
Blue_eye = [ariel, duke, elsa, carl, geppetto]
Brown_eye = [snow, doc, belle, flynn, jasmine, kristoff, john]
Green_eye = [tarzan, rapunzel, esmeralda, jessica]
Black_eye = [jafar, captain, milo, peter, anita]
Violet_eye = [megara, aurora]
Pale_skin = [snow, elsa, aurora, carl, belle]
Fair_skin = [jessica, godmother, kristoff, john, rapunzel, anita]
Olive = [geppetto, duke, doc, ariel, peter]
Tan = [megara, flynn, captain, milo]
Brown = [esmeralda, jafar, jasmine, tarzan]
Facial_hair = [jafar, captain, duke, geppetto, flynn]
Elderly = [carl, geppetto, godmother, duke, doc]
Glasses = [milo, geppetto, carl, doc, john, anita]
Ponytail = [elsa, belle, megara, jasmine, esmeralda]
Big_nose = [captain, carl, duke, doc]
Hats = [jafar, captain, doc, john, peter, godmother]
Earring = [jessica, esmeralda, jasmine, megara]

random_character = random.choice(characters)
# random_trait = random.choice(character_traits)


print(random_character)


def delete_character(chosentrait, ):
    pass


number_of_guesses = 0

while main_loop:
    if running_mainmenu:
        screen.fill(BLUE)
        screen.blit(text_menutitle1, (500, 100))
        screen.blit(disney_title, (150, 30))
        screen.blit(text_menutext, (430, 500))
        screen.blit(carl_title, (80, 600))
        screen.blit(elsa_title, (800, 600))
        screen.blit(gepetto_title, (30, 400))
        screen.blit(beauty_title, (980, 380))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_mainmenu = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running_gamescreen = True
                running_mainmenu = False
            if event.type == pygame.QUIT:
                # exit
                sys.exit()

    if running_gamescreen:
        screen.fill(GREEN)

        # check point 2
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

        if blonde_hair_avail == True and violet_eyes_avail == True:
            render_picture(image_aurora, 15, 440)

        if blonde_hair_avail == True and blue_eyes_avail == True:
            render_picture(image_elsa, 375, 60)

        if blonde_hair_avail == True and green_eyes_avail == True:
            render_picture(image_rapunzel, 900, 250)

        if blonde_hair_avail == True and brown_eyes_avail == True:
            render_picture(image_kristoff, 725, 250)

        if red_hair_avail == True and black_eyes_avail == True:
            render_picture(image_anita, 15, 60)

        if red_hair_avail == True and blue_eyes_avail == True:
            render_picture(image_ariel, 15, 250)

        if red_hair_avail == True and green_eyes_avail == True:
            render_picture(image_jessica, 550, 630)

        if red_hair_avail == True and black_eyes_avail == True:
            render_picture(image_peter, 900, 60)

        if red_hair_avail == True and brown_eyes_avail == True:
            render_picture(image_john, 725, 60)

        if brown_hair_avail == True and brown_eyes_avail == True:
            render_picture(image_belle, 15, 630)

        if brown_hair_avail == True and brown_eyes_avail == True:
            render_picture(image_flynn, 375, 630)

        if brown_hair_avail == True and green_eyes_avail == True:
            render_picture(image_tarzan, 900, 630)

        if brown_hair_avail == True and black_eyes_avail == True:
            render_picture(image_milo, 725, 630)

        if brown_hair_avail == True and violet_eyes_avail == True:
            render_picture(image_megara, 725, 440)

        if black_hair_avail == True and black_eyes_avail == True:
            render_picture(image_captain, 200, 60)

        if black_hair_avail == True and green_eyes_avail == True:
            render_picture(image_esmeralda, 375, 250)

        if black_hair_avail == True and black_eyes_avail == True:
            render_picture(image_jasmine, 550, 440)

        if black_hair_avail == True and black_eyes_avail == True:
            render_picture(image_jafar, 550, 250)

        if black_hair_avail == True and brown_eyes_avail == True:
            render_picture(image_snow, 900, 440)

        if white_hair_avail == True and blue_eyes_avail == True:
            render_picture(image_carl, 200, 250)

        if white_hair_avail == True and brown_eyes_avail == True:
            render_picture(image_doc, 200, 440)

        if white_hair_avail == True and blue_eyes_avail == True:
            render_picture(image_duke, 200, 630)

        if white_hair_avail == True and black_eyes_avail == True:
            render_picture(image_godmother, 375, 440)

        if white_hair_avail == True and blue_eyes_avail == True:
            render_picture(image_geppetto, 550, 60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button1.collidepoint(mouse_pos):
                        print('button 1 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button1clicked)
                        button1_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.hair == 'blonde hair':
                            print('blonde hair')
                            blonde_hair_avail = True
                            black_hair_avail = False
                            brown_hair_avail = False
                            white_hair_avail = False
                            red_hair_avail = False
                        if random_character.hair != 'blonde hair':
                            print('no blonde hair')
                            blonde_hair_avail = False

                    if button2.collidepoint(mouse_pos):
                        print('button 2 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button2clicked)
                        button2_avail = False
                        number_of_guesses += 1
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

                    if button3.collidepoint(mouse_pos):
                        print('button 3 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button3clicked)
                        button3_avail = False
                        number_of_guesses += 1
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

                    if button4.collidepoint(mouse_pos):
                        print('button 4 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button4clicked)
                        button4_avail = False
                        number_of_guesses += 1
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

                    if button5.collidepoint(mouse_pos):
                        print('button 5 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button5clicked)
                        button5_avail = False
                        number_of_guesses += 1
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

                    if button6.collidepoint(mouse_pos):
                        print('button 6 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button6clicked)
                        button6_avail = False
                        number_of_guesses += 1
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

                    if button7.collidepoint(mouse_pos):
                        print('button 7 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button7clicked)
                        button7_avail = False
                        number_of_guesses += 1
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

                    if button8.collidepoint(mouse_pos):
                        print('button 8 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button8clicked)
                        button8_avail = False
                        number_of_guesses += 1
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

                    if button9.collidepoint(mouse_pos):
                        print('button 9 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button9clicked)
                        button9_avail = False
                        number_of_guesses += 1
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

                    if button10.collidepoint(mouse_pos):
                        print('button 10 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button10clicked)
                        button10_avail = False
                        number_of_guesses += 1
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

                    if button11.collidepoint(mouse_pos):
                        print('button 11 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button11clicked)
                        button11_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.skin == 'pale':
                            print("pale skin")
                        if random_character.eye != 'pale':
                            print('no pale skin')

                    if button12.collidepoint(mouse_pos):
                        print('button 12 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button12clicked)
                        button12_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.skin == 'fair':
                            print("fair skin")
                        if random_character.eye != 'fair':
                            print('no fair skin')

                    if button13.collidepoint(mouse_pos):
                        print('button 13 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button13clicked)
                        button13_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.skin == 'olive':
                            print("olive skin")
                        if random_character.eye != 'olive':
                            print('no olive skin')

                    if button14.collidepoint(mouse_pos):
                        print('button 14 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button14clicked)
                        button14_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.skin == 'tan':
                            print("tan skin")
                        if random_character.eye != 'tan':
                            print('no tan skin')

                    if button15.collidepoint(mouse_pos):
                        print('button 15 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button15clicked)
                        button15_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.skin == 'brown':
                            print("brown skin")
                        if random_character.eye != 'brown':
                            print('no brown skin')

                    if button16.collidepoint(mouse_pos):
                        print('button 16 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button16clicked)
                        button16_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.facial_hair == 'none':
                            print("No facial")
                        if random_character.facial_hair == 'facial_hair':
                            print("Facial")

                    if button17.collidepoint(mouse_pos):
                        print('button 17 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button17clicked)
                        button17_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.elderly == 'none':
                            print("No elderly")
                        if random_character.elderly == 'elderly':
                            print("elderly")

                    if button18.collidepoint(mouse_pos):
                        print('button 18 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button18clicked)
                        button18_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.glasses == 'none':
                            print('No glasses')
                        if random_character.glasses == 'glasses':
                            print("glasses")

                    if button19.collidepoint(mouse_pos):
                        print('button 19 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button19clicked)
                        button19_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.pony_tail == 'none':
                            print('No pony tail')
                        if random_character.pony_tail == 'pony_tail':
                            print('Pony tail')

                    if button20.collidepoint(mouse_pos):
                        print('button 20 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button20clicked)
                        button20_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.big_nose == 'none':
                            print('no big nose')
                        if random_character.big_nose == 'big_nose':
                            print('big nose')

                    if button21.collidepoint(mouse_pos):
                        print('button 21 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button21clicked)
                        button21_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.hats == 'none':
                            print('no hats')
                        if random_character.hats == 'hat':
                            print('hats')

                    if button22.collidepoint(mouse_pos):
                        print('button 22 was pressed at {0}'.format(mouse_pos))
                        pygame.draw.rect(screen, RED, button22clicked)
                        button22_avail = False
                        number_of_guesses += 1
                        print(number_of_guesses)
                        if random_character.earring == 'none':
                            print('no earrings')
                        if random_character.earring == 'earring':
                            print('earrings')
        # till here
        # ddd

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.display.update()
