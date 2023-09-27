import pygame as pg
import pygame.time

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
player_gap = 10
player_velocity = 10
player_dx = 0
player_x = screen_width/2 - playerWidth/2
player_y = screen_height - playerHeight - player_gap


isRunning = True
isHiddingDaniil = False
while isRunning:
    player_x += player_dx
    if player_x < 0 :
        player_x = 0
    if player_x > screen_width - playerWidth:
        player_x = screen_width - playerWidth


    # redraw
    display.blit(bg_img, (0, 0))
    display.blit(playerImg, (player_x, player_y))
    pg.display.update()

    for event in pg.event.get():
        # Нажатие на крестик
        if (event.type == pg.QUIT):
            isRunning = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                isRunning = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player_dx = -player_velocity
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                player_dx = player_velocity
        if event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player_dx = 0
            elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                player_dx = 0


    clock.tick(FPS)
pg.quit()