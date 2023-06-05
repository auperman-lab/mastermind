import pygame
from pygame.locals import *
import sys
from random import randint
from constants import *


def win():
    for col in range(4):
        screen.blit(font40.render('Y', True, BLACK), (203 + 74 * col, 82))
    for col in range(4):
        screen.blit(font40.render('O', True, BLACK), (201 + 74 * col, 82+76))
    for col in range(4):
        screen.blit(font40.render('U', True, BLACK), (202 + 74 * col, 84+76*2))
    for col in range(4):
        screen.blit(font40.render('W', True, BLACK), (202 + 74 * col, 86+76*4))
    for col in range(4):
        screen.blit(font40.render('I', True, BLACK), (204 + 74 * col, 88+76*5))
    for col in range(4):
        screen.blit(font40.render('N', True, BLACK), (202 + 74 * col, 89+76*6))
    for col in range(4):
        screen.blit(font40.render('!', True, BLACK), (202 + 74 * col, 89+76*7))


def lose():
    for col in range(4):
        screen.blit(font40.render('Y', True, BLACK), (203 + 74 * col, 82))
    for col in range(4):
        screen.blit(font40.render('O', True, BLACK), (201 + 74 * col, 82+76))
    for col in range(4):
        screen.blit(font40.render('U', True, BLACK), (202 + 74 * col, 84+76*2))
    for col in range(4):
        screen.blit(font40.render('L', True, BLACK), (205 + 74 * col, 86+76*4))
    for col in range(4):
        screen.blit(font40.render('O', True, BLACK), (202 + 74 * col, 89+76*5))
    for col in range(4):
        screen.blit(font40.render('S', True, BLACK), (202 + 74 * col, 89+76*6))
    for col in range(4):
        screen.blit(font40.render('E', True, BLACK), (205 + 74 * col, 90+76*7))


# genertes cypher with no repetition in color
def no_rep_code():
    used_colors = []
    code = ''
    cod = 0
    while cod in range(4):
        col = collors[randint(0, 5)]
        if col not in used_colors:
            code += col
            used_colors.append(code[-1])
            cod += 1
    return code


# genertes cypher with repetition in color
def rep_code():
    code = ''
    for cod in range(4):
        code += collors[randint(0, 5)]
    return code


def restore_board():
    for j in range(8):
        for i in range(4):
            if i == 0:
                draw_token(BLACK, 103 + 415, 88 + 78 * j)
                draw_token(BLACK, 103, 88 + 78 * j)
            elif i == 1:
                draw_token(BLACK, 103 + 415 + 35, 88 + 78 * j)
                draw_token(BLACK, 103 + 35, 88 + 78 * j)
            elif i == 2:
                draw_token(BLACK, 103 + 415, 88 + 35 + 78 * j)
                draw_token(BLACK, 103, 88 + 35 + 78 * j)
            elif i == 3:
                draw_token(BLACK, 103 + 415 + 35, 88 + 35 + 78 * j)
                draw_token(BLACK, 103 + 35, 88 + 35 + 78 * j)


def draw_big_circle(color, x, y, w=4, h=4):
    # x => x coordinate for drawing
    # y => y coordinate for drawing
    # w => width
    # h => height
    pygame.draw.rect(screen, color, pygame.Rect(x - 12 * w, y, 2 * 12 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 11 * w, y + 3 * h, 2 * 11 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 10 * w, y + 5 * h, 2 * 10 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 9 * w, y + 7 * h, 2 * 9 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y + 8 * h, 2 * 8 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y + 9 * h, 2 * 7 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y + 10 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y + 11 * h, 2 * 3 * w, 1 * h))

    pygame.draw.rect(screen, color, pygame.Rect(x - 12 * w, y - 3 * h, 2 * 12 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 11 * w, y - 5 * h, 2 * 11 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 10 * w, y - 7 * h, 2 * 10 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 9 * w, y - 8 * h, 2 * 9 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y - 9 * h, 2 * 8 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y - 10 * h, 2 * 7 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y - 11 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y - 12 * h, 2 * 3 * w, 1 * h))


def draw_small_circle(color, x, y, w=4, h=4):
    # x => x coordinate for drawing
    # y => y coordinate for drawing
    # w => width
    # h => height
    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y, 2 * 8 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y + 3 * h, 2 * 7 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 6 * w, y + 5 * h, 2 * 6 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y + 6 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y + 7 * h, 2 * 3 * w, 1 * h))

    pygame.draw.rect(screen, color, pygame.Rect(x - 8 * w, y - 3 * h, 2 * 8 * w, 3 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 7 * w, y - 5 * h, 2 * 7 * w, 2 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 6 * w, y - 6 * h, 2 * 6 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 5 * w, y - 7 * h, 2 * 5 * w, 1 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y - 8 * h, 2 * 3 * w, 1 * h))


def draw_token(color, x, y, w=4, h=4):
    # x => x coordinate for drawing
    # y => y coordinate for drawing
    # w => width
    # h => height
    pygame.draw.rect(screen, color, pygame.Rect(x - 4 * w, y - 2 * h, 8 * w, 4 * h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y - 3 * h, 6 * w, h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 2 * w, y - 4 * h, 4 * w, h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 3 * w, y + 2 * h, 6 * w, h))
    pygame.draw.rect(screen, color, pygame.Rect(x - 2 * w, y + 3 * h, 4 * w, h))


def draw_box(x, y, w, h, p):
    # x => x coordinate for drawing
    # y => y coordinate for drawing
    # w => width of the drawn box
    # h => height of the drawn box
    # p => level of concavity of margins

    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y + h/2), (x + w/2 - 2*w/p, y + h/2))
    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y - h/2), (x + w/2 - 2*w/p, y - h/2))
    pygame.draw.line(screen, WHITE, (x - w/2, y + h/2 - 2*h/p), (x - w/2, y - h/2 + 2*h/p))
    pygame.draw.line(screen, WHITE, (x + w/2, y + h/2 - 2*h/p), (x + w/2, y - h/2 + 2*h/p))

    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y + h/2), (x - w/2 + 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y + h/2 - h/p), (x - w/2 + w/p, y + h/2 - 2*h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y + h/2 - h/p), (x - w/2 + 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x - w/2, y + h/2 - 2*h/p), (x - w/2 + w/p, y + h/2 - 2*h/p))

    pygame.draw.line(screen, WHITE, (x + w/2 - 2*w/p, y + h/2), (x + w/2 - 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y + h/2 - h/p), (x + w/2 - w/p, y + h/2 - 2*h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y + h/2 - h/p), (x + w/2 - 2*w/p, y + h/2 - h/p))
    pygame.draw.line(screen, WHITE, (x + w/2, y + h/2 - 2*h/p), (x + w/2 - w/p, y + h/2 - 2*h/p))

    pygame.draw.line(screen, WHITE, (x + w/2 - 2*w/p, y - h/2), (x + w/2 - 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y - h/2 + h/p), (x + w/2 - w/p, y - h/2 + 2*h/p))
    pygame.draw.line(screen, WHITE, (x + w/2 - w/p, y - h/2 + h/p), (x + w/2 - 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x + w/2, y - h/2 + 2*h/p), (x + w/2 - w/p, y - h/2 + 2*h/p))

    pygame.draw.line(screen, WHITE, (x - w/2 + 2*w/p, y - h/2), (x - w/2 + 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y - h/2 + h/p), (x - w/2 + w/p, y - h/2 + 2*h/p))
    pygame.draw.line(screen, WHITE, (x - w/2 + w/p, y - h/2 + h/p), (x - w/2 + 2*w/p, y - h/2 + h/p))
    pygame.draw.line(screen, WHITE, (x - w/2, y - h/2 + 2*h/p), (x - w/2 + w/p, y - h/2 + 2*h/p))


########################################################################################################################
pygame.init()

font40 = pygame.font.Font('PixelEmulator.ttf', 40)
font30 = pygame.font.Font('PixelEmulator.ttf', 30)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BLACK)

######################################################## text ##########################################################
logo = font40.render('MasterMind', True, WHITE)
screen.blit(logo, logo.get_rect(center=(325, 15)))

######################################################## grid ##########################################################
pygame.draw.line(screen, WHITE, (0, 36), (SCREEN_WIDTH, 36))
pygame.draw.line(screen, WHITE, (164, 65), (164, 685))
pygame.draw.line(screen, WHITE, (488, 65), (488, 685))
for i in range(1, 8):
    pygame.draw.line(screen, WHITE, (35, 65+78*i), (615, 65+78*i))

###################################################### border ##########################################################
draw_box(325, 375, 600, 640, 30)
draw_box(325, 375, 580, 620, 30)

##################################################### variables ########################################################
cipher_input = False
all_attempts = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'],
                ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]
your_try = ''
hint = ''
try_nr = 0
########################################################################################################################
while True:

    mouse = pygame.mouse.get_pos()

##################################################### render buttons ###################################################
    if 0 <= mouse[0] <= 150 and 0 <= mouse[1] <= 36:  # automatic cipher button hover
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, 150, 36))
        screen.blit(font30.render('auto', True, WHITE), (30, 0))
    else:
        pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 150, 36))
        screen.blit(font30.render('auto', True, BLACK), (30, 0))

    if 500 <= mouse[0] <= 650 and 0 <= mouse[1] <= 36:  # manual cipher button hover
        pygame.draw.rect(screen, BLACK, pygame.Rect(500, 0, 150, 36))
        screen.blit(font30.render('MANUAL', True, WHITE), (505, 0))
    else:
        pygame.draw.rect(screen, WHITE, pygame.Rect(500, 0, 150, 36))
        screen.blit(font30.render('MANUAL', True, BLACK), (505, 0))

    if 10 <= mouse[0] <= 110 and 710 <= mouse[1] <= 810 and len(your_try) < 4:  # RED button hover
        draw_big_circle(WHITE, 60, 760)
        screen.blit(font40.render('R', True, RED), (47, 735))
    else:
        draw_big_circle(RED, 60, 760)
        screen.blit(font40.render('R', True, BLACK), (47, 735))

    if 120 <= mouse[0] <= 220 and 710 <= mouse[1] <= 810 and len(your_try) < 4:  # WHITE button hover
        draw_big_circle(WHITE, 60 + 106, 760)
        screen.blit(font40.render('O', True, ORANGE), (47 + 106, 735))
    else:
        draw_big_circle(ORANGE, 60 + 106, 760)
        screen.blit(font40.render('O', True, BLACK), (47+106, 735))

    if 230 <= mouse[0] <= 330 and 710 <= mouse[1] <= 810 and len(your_try) < 4:  # PINK button hover
        draw_big_circle(WHITE, 60 + 106 * 2, 760)
        screen.blit(font40.render('P', True, PINK), (48 + 106 * 2, 735))
    else:
        draw_big_circle(PINK, 60 + 106 * 2, 760)
        screen.blit(font40.render('P', True, BLACK), (48 + 106 * 2, 735))

    if 340 <= mouse[0] <= 440 and 710 <= mouse[1] <= 810 and len(your_try) < 4:  # CYAN button hover
        draw_big_circle(WHITE, 60 + 106 * 3, 760)
        screen.blit(font40.render('C', True, CYAN), (45 + 106 * 3, 735))
    else:
        draw_big_circle(CYAN, 60 + 106 * 3, 760)
        screen.blit(font40.render('C', True, BLACK), (45 + 106 * 3, 735))

    if 450 <= mouse[0] <= 550 and 710 <= mouse[1] <= 810 and len(your_try) < 4:  # GREEN button hover
        draw_big_circle(WHITE, 60 + 106 * 4, 760)
        screen.blit(font40.render('G', True, GREEN), (45 + 106 * 4, 735))
    else:
        draw_big_circle(GREEN, 60 + 106 * 4, 760)
        screen.blit(font40.render('G', True, BLACK), (45 + 106 * 4, 735))

    if 560 <= mouse[0] <= 660 and 710 <= mouse[1] <= 810 and len(your_try) < 4:  # YELLOW button hover
        draw_big_circle(WHITE, 60 + 106 * 5, 760)
        screen.blit(font40.render('Y', True, YELLOW), (48 + 106 * 5, 735))
    else:
        draw_big_circle(YELLOW, 60 + 106 * 5, 760)
        screen.blit(font40.render('Y', True, BLACK), (48 + 106 * 5, 735))


########################################### logic behind buttons #######################################################

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 150 and 0 <= mouse[1] <= 36:  # automatic cypher mode

                restore_board()

                cipher_input = False  #  restore variables
                all_attempts = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'],
                                ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]
                your_try = ''
                hint = ''
                try_nr = 0

                cypher = no_rep_code()  # algorithm for cypher generation(u can chose it)
                print(cypher)
            if 500 <= mouse[0] <= 650 and 0 <= mouse[1] <= 36:  # manual cypher mode
                restore_board()

                #  restore variables
                cipher_input = True

                all_attempts = [['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'],
                                ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '0', '0', '0']]
                your_try = ''
                hint = ''
                try_nr = 0

            #  get user input
            if 10 <= mouse[0] <= 110 and 710 <= mouse[1] <= 810 and len(your_try) < 4:
                your_try += 'r'
            if 120 <= mouse[0] <= 220 and 710 <= mouse[1] <= 810 and len(your_try) < 4:
                your_try += 'o'
            if 230 <= mouse[0] <= 330 and 710 <= mouse[1] <= 810 and len(your_try) < 4:
                your_try += 'p'
            if 340 <= mouse[0] <= 440 and 710 <= mouse[1] <= 810 and len(your_try) < 4:
                your_try += 'c'
            if 450 <= mouse[0] <= 550 and 710 <= mouse[1] <= 810 and len(your_try) < 4:
                your_try += 'g'
            if 560 <= mouse[0] <= 660 and 710 <= mouse[1] <= 810 and len(your_try) < 4:
                your_try += 'y'

################################################ render input ##########################################################

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:  # delete last input color
                if len(your_try) > 0:
                    your_try = your_try[:-1]
            elif event.key == K_RETURN:
                if cipher_input:  # get the input for manual cipher
                    cypher = your_try
                    your_try = ''
                    cipher_input = False
                else:
                    # change and restore variables
                    all_attempts[try_nr] = list(your_try)
                    hint = ''
                    delleted = ''
                    guess_used_colors = list(cypher)

                    for i in range(len(your_try)):  # check for true guesses
                        if your_try[i] == cypher[i]:
                            hint += 'r'
                            guess_used_colors.remove(your_try[i])
                            delleted += your_try[i]
                    for letter in delleted:
                        your_try = your_try.replace(letter, '', 1)

                    for letter in your_try:
                        if letter in cypher and letter in guess_used_colors:
                            hint += 'w'
                            guess_used_colors.remove(letter)

                    for hn in range(len(hint)):  # draw the true guesses
                            if hint[hn] == 'r':
                                if hn == 0:
                                    draw_token(RED, 103 + 415, 88 + 78 * try_nr)
                                elif hn == 1:
                                    draw_token(RED, 103 + 35 + 415, 88 + 78 * try_nr)
                                elif hn == 2:
                                    draw_token(RED, 103 + 415, 88 + 35 + 78 * try_nr)
                                elif hn == 3:
                                    draw_token(RED, 103 + 35 + 415, 88 + 35 + 78 * try_nr)
                            else:
                                if hn == 0:
                                    draw_token(WHITE, 103 + 415, 88 + 78 * try_nr)
                                elif hn == 1:
                                    draw_token(WHITE, 103 + 35 + 415, 88 + 78 * try_nr)
                                elif hn == 2:
                                    draw_token(WHITE, 103 + 415, 88 + 35 + 78 * try_nr)
                                elif hn == 3:
                                    draw_token(WHITE, 103 + 35 + 415, 88 + 35 + 78 * try_nr)

                    for i in range(4 - len(hint)):
                            if 4 - len(your_try) == 4:
                                if i == 0:
                                    draw_token(BLACK, 103 + 415, 88 + 78 * try_nr)
                                elif i == 1:
                                    draw_token(BLACK, 103 + 415 + 35, 88 + 78 * try_nr)
                                elif i == 2:
                                    draw_token(BLACK, 103 + 415, 88 + 35 + 78 * try_nr)
                                elif i == 3:
                                    draw_token(BLACK, 103 + 415 + 35, 88 + 35 + 78 * try_nr)
                            elif 4 - len(your_try) == 3:
                                if i == 0:
                                    draw_token(BLACK, 103 + 415 + 35, 88 + 78 * try_nr)
                                elif i == 1:
                                    draw_token(BLACK, 103 + 415, 88 + 35 + 78 * try_nr)
                                elif i == 2:
                                    draw_token(BLACK, 103 + 415 + 35, 88 + 35 + 78 * try_nr)
                            elif 4 - len(your_try) == 2:
                                if i == 0:
                                    draw_token(BLACK, 103 + 415, 88 + 35 + 78 * try_nr)
                                elif i == 1:
                                    draw_token(BLACK, 103 + 415 + 35, 88 + 35 + 78 * try_nr)
                            else:
                                draw_token(BLACK, 103 + 415 + 35, 88 + 35 + 78 * try_nr)

                    your_try = ''

                    try_nr += 1
            elif len(your_try) < 4:
                your_try += event.unicode
##################################################### render input #####################################################
    for letter in range(len(your_try)):  # render your guess
            if your_try[letter] == 'g':
                if letter == 0:
                    draw_token(GREEN, 103, 88+78*try_nr)
                elif letter == 1:
                    draw_token(GREEN, 103+35, 88+78*try_nr)
                elif letter == 2:
                    draw_token(GREEN, 103, 88+35+78*try_nr)
                elif letter == 3:
                    draw_token(GREEN, 103+35, 88+35+78*try_nr)
            elif your_try[letter] == 'r':
                if letter == 0:
                    draw_token(RED, 103, 88+78*try_nr)
                elif letter == 1:
                    draw_token(RED, 103+35, 88+78*try_nr)
                elif letter == 2:
                    draw_token(RED, 103, 88+35+78*try_nr)
                elif letter == 3:
                    draw_token(RED, 103+35, 88+35+78*try_nr)
            elif your_try[letter] == 'p':
                if letter == 0:
                    draw_token(PINK, 103, 88+78*try_nr)
                elif letter == 1:
                    draw_token(PINK, 103+35, 88+78*try_nr)
                elif letter == 2:
                    draw_token(PINK, 103, 88+35+78*try_nr)
                elif letter == 3:
                    draw_token(PINK, 103+35, 88+35+78*try_nr)
            elif your_try[letter] == 'c':
                if letter == 0:
                    draw_token(CYAN, 103, 88+78*try_nr)
                elif letter == 1:
                    draw_token(CYAN, 103 + 35, 88+78*try_nr)
                elif letter == 2:
                    draw_token(CYAN, 103, 88 + 35+78*try_nr)
                elif letter == 3:
                    draw_token(CYAN, 103 + 35, 88 + 35+78*try_nr)
            elif your_try[letter] == 'o':
                if letter == 0:
                    draw_token(ORANGE, 103, 88+78*try_nr)
                elif letter == 1:
                    draw_token(ORANGE, 103+35, 88+78*try_nr)
                elif letter == 2:
                    draw_token(ORANGE, 103, 88+35+78*try_nr)
                elif letter == 3:
                    draw_token(ORANGE, 103+35, 88+35+78*try_nr)
            elif your_try[letter] == 'y':
                if letter == 0:
                    draw_token(YELLOW, 103, 88+78*try_nr)
                elif letter == 1:
                    draw_token(YELLOW, 103+35, 88+78*try_nr)
                elif letter == 2:
                    draw_token(YELLOW, 103, 88+35+78*try_nr)
                elif letter == 3:
                    draw_token(YELLOW, 103+35, 88+35+78*try_nr)

    for j in range(8):  # restore empty cell if u delete a input
        if j == try_nr:
            for i in range(4 - len(your_try)):
                if 4 - len(your_try) == 4:
                    if i == 0:
                        draw_token(GRAY, 103, 88+78*try_nr)
                    elif i == 1:
                        draw_token(GRAY, 103+35, 88+78*try_nr)
                    elif i == 2:
                        draw_token(GRAY, 103, 88+35+78*try_nr)
                    elif i == 3:
                        draw_token(GRAY, 103+35, 88+35+78*try_nr)
                elif 4 - len(your_try) == 3:
                    if i == 0:
                        draw_token(GRAY, 103+35, 88+78*try_nr)
                    elif i == 1:
                        draw_token(GRAY, 103, 88+35+78*try_nr)
                    elif i == 2:
                        draw_token(GRAY, 103+35, 88+35+78*try_nr)
                elif 4 - len(your_try) == 2:
                    if i == 0:
                        draw_token(GRAY, 103, 88+35+78*try_nr)
                    elif i == 1:
                        draw_token(GRAY, 103+35, 88+35+78*try_nr)
                else:
                    draw_token(GRAY, 103 + 35, 88 + 35+78*try_nr)
            break
        else:
            draw_token(BLACK, 103, 88 + 78 * j)
            draw_token(BLACK, 103+35, 88 + 78 * j)
            draw_token(BLACK, 103+35, 88+35 + 78 * j)
            draw_token(BLACK, 103, 88+35 + 78 * j)


##################################################### print guess ###################################################
    for row in range(len(all_attempts)):
        for color in range(4):
            if all_attempts[row][color] == 'g':
                draw_small_circle(GREEN, 215 + 74 * color, 105 + 78 * row)
            elif all_attempts[row][color] == 'r':
                draw_small_circle(RED, 215 + 74 * color, 105 + 78 * row)
            elif all_attempts[row][color] == 'p':
                draw_small_circle(PINK, 215 + 74 * color, 105 + 78 * row)
            elif all_attempts[row][color] == 'c':
                draw_small_circle(CYAN, 215 + 74 * color, 105 + 78 * row)
            elif all_attempts[row][color] == 'o':
                draw_small_circle(ORANGE, 215 + 74 * color, 105 + 78 * row)
            elif all_attempts[row][color] == 'y':
                draw_small_circle(YELLOW, 215 + 74 * color, 105 + 78 * row)
            else:
                draw_small_circle(GRAY, 215 + 74 * color, 105 + 78 * row)

    if hint == 'rrrr':  # win/lose condition
        win()
    if try_nr == 8 and hint != 'rrrr':
        lose()

    pygame.display.flip()
