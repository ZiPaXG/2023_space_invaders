import pygame as pg
import pygame.time

#ДЗ 3 lvl

def changeStateLetter(key, strN):
    strN = list(strN)
    indexElem = listLetter.index(key)
    lettersStates = allLettersStates[allLetterName[indexElem]][1]
    if allLettersStates[allLetterName[indexElem]][2] == False:
        lettersStates[lettersStates.index(True)] = False
        if lettersStates.count(True) == 0:
            allLettersStates[allLetterName[indexElem]][2] = True
    else:
        lettersStates[lettersStates.index(False)] = True
        if lettersStates.count(False) == 0:
            allLettersStates[allLetterName[indexElem]][2] = False

    for k, v in allLettersStates.items():
        for i in range(len(v[1])):
            if v[1][i]:
                strN[v[0][i]] = k
            else:
                strN[v[0][i]] = " "

    return ''.join(strN)

pg.init()
screen_width, screen_height = 800, 600
FPS = 24
clock = pygame.time.Clock()

sysfont = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 48)

bg_img = pg.image.load('src/background.png')
icon_img = pg.image.load('src/ufo.png')

display = pg.display.set_mode((screen_width, screen_height))

#display.fill('blue', (0, 0, screen_width, screen_height))
display.blit(bg_img, (0, 0))

# Score
#text_img = sysfont.render('Score 123', True, 'white')
#display.blit(text_img, (100, 50))

# Game over
#game_over_text = font.render('Game Over', True, 'red')
#w, h = game_over_text.get_size()
#display.blit(game_over_text, (screen_width/2 - w/2, screen_height / 2 - h/2))

pg.display.set_icon(icon_img)
pg.display.set_caption('Space Invaders')

# Игрок
playerImg = pg.image.load('src/player.png')
playerWidth, playerHeight = playerImg.get_size()

# ДЗ 1 lvl
listLetter = [pg.K_l, pg.K_f, pg.K_y, pg.K_b, pg.K_b, pg.K_k]

# Этот список нужен для того, чтобы обращаться к словарю allLettersStates, чтобы изменить состояние буквы на True или False
allLetterName = ["д", "а", "н", "и", "и", "л"]

# Этот словарь содержит информацию о том:
# видна ли буква,
# список индексов, где располагается буква (буква может повторяться),
# а также False, если при нажатии на клавишу буква исчезает, или True, если при нажатии на клавишу буква появляется
allLettersStates = {
    "д" : [[0], [True], False],
    "а" : [[1], [True], False],
    "н" : [[2], [True], False],
    "и" : [[3, 4], [True, True], False],
    "л" : [[5], [True], False]
}
strName = "даниил"
strNameDaniil = sysfont.render(strName.capitalize(), True, 'red')
w, h = strNameDaniil.get_size()
a = display.blit(strNameDaniil, (screen_width / 2 - w / 2, screen_height - h))

isRunning = True
isHiddingDaniil = False
while isRunning:
    pg.display.update()
    for event in pg.event.get():
        # Нажатие на крестик
        if (event.type == pg.QUIT):
            isRunning = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                display.blit(bg_img, (0, 0))
            # ДЗ 2 lvl
            #if event.key == pg.K_SPACE or event.key == pg.K_l:
            #    if isHiddingDaniil:
            #        isHiddingDaniil = False
            #        display.blit(strNameDaniil, (screen_width / 2 - w / 2, screen_height - h))
            #    else:
            #        isHiddingDaniil = True
            #        display.blit(bg_img, (0, 0))
            # -----------------------------------------------------------------------------
            # ДЗ 3 lvl
            if event.key in listLetter:
                strName = changeStateLetter(event.key, strName)
                strNameDaniil = sysfont.render(strName.capitalize(), True, 'red')
                display.blit(bg_img, (0, 0))
                display.blit(strNameDaniil, (screen_width / 2 - w / 2, screen_height - h))
    clock.tick(FPS)
pg.quit()