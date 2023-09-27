import pygame as pg
import pygame.time
import random

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

# Пуля
bulletImg = pg.image.load('src/bullet.png')
bulletWidth, bulletHeight = bulletImg.get_size()
bullet_x = 0
bullet_y = 0
bullet_dy = -5
bullet_isAlive = False

# Противник
enemyImg = pg.image.load('src/enemy.png')
enemyWidth, enemyHeight = bulletImg.get_size()
enemy_dx = 0
enemy_dy = 2
enemy_x = 0
enemy_y = 0

def model_update():
    player_model()
    bullet_model()
    enemy_model()
def player_model():
    global  player_x
    player_x += player_dx
    if player_x < 0 :
        player_x = 0
    if player_x > screen_width - playerWidth:
        player_x = screen_width - playerWidth
def bullet_model():
    """ Изменение положения пули """
    global bullet_y, bullet_isAlive
    bullet_y += bullet_dy
    if bullet_y < 0:
        bullet_isAlive = False

def enemy_model():
    """ Изменение положения противника, рассчет поражений """
    global enemy_x, enemy_y, bullet_isAlive
    enemy_x += enemy_dx
    enemy_y += enemy_dy
    if enemy_y > screen_height:
        enemy_create()

    if bullet_isAlive:
        recEnemy = pg.Rect(enemy_x, enemy_y, enemyWidth, enemyHeight)
        recBullet = pg.Rect(bullet_x, bullet_y, bulletWidth, bulletHeight)
        if recEnemy.colliderect(recBullet):
            print("BANG!")
            enemy_create()
            bullet_isAlive = False
def bullet_create():
    global bullet_x, bullet_y, bullet_isAlive
    bullet_x = player_x + bulletWidth / 2
    bullet_y = player_y - bulletHeight
    bullet_isAlive = True

def enemy_create():
    """  Создаем противника в рандомных координатах """
    global enemy_x, enemy_y
    enemy_x = random.randint(0, screen_width - enemyWidth)
    enemy_y = 0
    print(f'{enemy_x=}')

def display_redraw():
    display.blit(bg_img, (0, 0))
    display.blit(playerImg, (player_x, player_y))
    display.blit(enemyImg, (enemy_x, enemy_y))
    if bullet_isAlive:
        display.blit(bulletImg, (bullet_x, bullet_y))
    pg.display.update()

def event_processing():
    global player_dx
    isRunning = True
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
            player_dx = 0
        if event.type == pg.MOUSEBUTTONDOWN:
            key = pg.mouse.get_pressed()
            if key[0] and not(bullet_isAlive):
                bullet_create()

    clock.tick(FPS)
    return isRunning

# random.seed(77)
enemy_create()
isRunning = True
isHiddingDaniil = False
while isRunning:
    model_update()
    display_redraw()
    isRunning = event_processing()


pg.quit()