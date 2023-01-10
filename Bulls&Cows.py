import pygame
from pygame.locals import *
import sys
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
trial = 0

pygame.init()
screen = pygame.display.set_mode((360, 480))
fpsClock = pygame.time.Clock()

text = ''
guss = ['', '', '', '', '', '', '', '', '']
hints = ['', '', '', '', '', '', '', '', '']
font1 = pygame.font.SysFont('arial', 36)
img = font1.render(text, True, BLACK)
font2 = pygame.font.SysFont('arial', 34)
font3 = pygame.font.SysFont('arial', 20)
inpt = font3.render('Input: ', True, BLACK)
gss = font3.render('Guess', True, BLACK)
rslt = font3.render('Result', True, BLACK)
trl = font3.render('Trial', True, BLACK)
inptbool = False
inptcphr = font3.render('Input Cypher: ', True, BLACK)
inptcphrbool = False
cyphrkey = False
win = font2.render('You Win :)', True, BLACK)
loose = font2.render('You Loose :(', True, BLACK)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
mmind = font2.render('MasterMind', True, BLACK)
auto = font3.render('AUTO', True, WHITE)
manual = font3.render('MANUAL', True, WHITE)

rect = img.get_rect()
rect.topleft = (140, 36)

background = WHITE


while True:
    pygame.draw.rect(screen, [150, 150, 150], [130, 36, 105, 40], 2, border_radius=10)
    screen.blit(mmind, (90, 0))
    screen.blit(gss, (150, 90))
    screen.blit(rslt, (275, 90))
    screen.blit(trl, (30, 90))
    pygame.draw.line(screen, [150, 150, 150], (0, 32), (360, 32))

    mouse = pygame.mouse.get_pos()
    if 0 <= mouse[0] <= 80 and 0 <= mouse[1] <= 32:
        pygame.draw.rect(screen, GRAY, [0, 0, 80, 32])
    else:
        pygame.draw.rect(screen, BLACK, [0, 0, 80, 32])
    if 280 <= mouse[0] <= 360 and 0 <= mouse[1] <= 30:
        pygame.draw.rect(screen, GRAY, [280, 0, 80, 32])
    else:
        pygame.draw.rect(screen, BLACK, [280, 0, 80, 32])
    screen.blit(auto, (10, 5))
    screen.blit(manual, (280, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 80 and 0 <= mouse[1] <= 32:
                trial = 0
                inptcphrbool = False
                inptbool = True
                cipher = str(randint(0, 10000))
                if len(cipher) < 4:
                    for i in range(4 - len(cipher)):
                        cipher = '0' + cipher
                print(cipher)

            if 280 <= mouse[0] <= 360 and 0 <= mouse[1] <= 32:
                trial = 0
                inptbool = False
                cyphrkey  = True
                inptcphrbool = True


        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            elif event.key == K_RETURN:
                if cyphrkey:
                    cipher = text
                    cyphrkey = False
                    print(cipher)
                else:
                    trial += 1
                    for i in range(1, 9):
                        if i == trial:
                            guss[i] = text

                text = ""

            else:
                text += event.unicode
            img = font1.render(text, True, BLACK)

            rect.size = img.get_size()

    if inptbool:
        screen.blit(inpt, (20, 44))

        for i in range(1, 9):
            nrs = font2.render(numbers[i], True, BLACK)
            answ = font2.render(guss[i], True, BLACK)

            if trial >= i:
                dictnr = list(cipher)
                guess = guss[i]
                fpositions = 0
                tpositions = 0
                for k in range(4):
                    if guess[k] in dictnr:
                        fpositions += 1
                        dictnr.remove(guess[k])
                    if guess[k] == cipher[k]:
                        tpositions += 1
                hints[i] = str(tpositions) + "A" + str(fpositions - tpositions) + "B"
                hnts = font2.render(hints[i], True, BLACK)
                screen.blit(nrs, (35, 90+36*i))
                screen.blit(answ, (140, 90+36*i))
                if tpositions < 4:
                    screen.blit(hnts, (260, 90+36*i))
                    if trial >= 8:
                        screen.blit(loose, (100, 420))
                else:
                    screen.blit(win, (100, 420))
    if inptcphrbool:
        screen.blit(inptcphr, (0, 44))
        for i in range(1, 9):
            nrs = font2.render(numbers[i], True, BLACK)
            answ = font2.render(guss[i], True, BLACK)

            if trial >= i:
                dictnr = list(cipher)
                guess = guss[i]
                fpositions = 0
                tpositions = 0
                for k in range(4):
                    if guess[k] in dictnr:
                        fpositions += 1
                        dictnr.remove(guess[k])
                    if guess[k] == cipher[k]:
                        tpositions += 1
                hints[i] = str(tpositions) + "A" + str(fpositions - tpositions) + "B"
                hnts = font2.render(hints[i], True, BLACK)
                screen.blit(nrs, (20, 90+36*i))
                screen.blit(answ, (140, 90+36*i))
                if tpositions < 4:
                    screen.blit(hnts, (260, 90+36*i))
                    if trial >= 8:
                        screen.blit(loose, (100, 420))
                else:
                    screen.blit(win, (100, 420))

    pygame.display.flip()
    screen.fill(background)
    screen.blit(img, rect)




    fpsClock.tick(60)

pygame.quit()
