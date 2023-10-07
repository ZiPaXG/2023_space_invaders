import pygame as pg
import pygame.time
import random


class Game:
    def __init__(self):
        pg.init()
        self.screen_width, self.screen_height = 800, 600
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.isGameOver = False
        self.isPaused = False
        self.sysfont = pg.font.SysFont('arial', 34)
        self.font = pg.font.Font('src/04B_19.TTF', 48)
        self.bg_img = pg.image.load('src/background.png')
        self.icon_img = pg.image.load('src/ufo.png')
        self.display = pg.display.set_mode((self.screen_width, self.screen_height))
        self.game_over_text = self.font.render('Game Over', True, 'red')
        self.w, self.h = self.game_over_text.get_size()
        self.pause_text = self.font.render('Pause', True, 'white')
        self.wPause, self.hPause = self.pause_text.get_size()
        pg.display.set_icon(self.icon_img)
        pg.display.set_caption('Space Invaders')

    # Логика моделей
    def model_update(self):
        if not self.isGameOver and not self.isPaused:
            player.update_model()
            bullet.update_model()
            enemy.update_model()

    # Отрисовка кадра
    def display_redraw(self):
        if not self.isGameOver and not self.isPaused:
            self.display.blit(self.bg_img, (0, 0))
            self.display.blit(player.playerImg, (player.player_x, player.player_y))
            if enemy.enemy_isAlive:
                self.display.blit(enemy.enemyImg, (enemy.enemy_x, enemy.enemy_y))
            if bullet.bullet_isAlive:
                self.display.blit(bullet.bulletImg, (bullet.bullet_x, bullet.bullet_y))
            score_img = self.sysfont.render(f"Score: {player.score}", True, 'white')
            self.display.blit(score_img, (40, 40))
            for i in range(player.countHP):
                self.display.blit(player.hpImg, (500 + i * 100, 40))
        elif self.isGameOver:
            self.display.blit(self.bg_img, (0, 0))
            self.display.blit(self.game_over_text, (self.screen_width / 2 - self.w / 2, self.screen_height / 2 - self.h / 2))
        else:
            self.display.blit(self.pause_text, (self.screen_width / 2 - self.wPause / 2, self.screen_height / 2 - self.hPause / 2))
        pg.display.update()

    def event_processing(self):
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
                    player.player_dx = -player.player_velocity
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    player.player_dx = player.player_velocity
                if event.key == pg.K_p and not game.isGameOver:
                    game.isPaused = not game.isPaused
            if event.type == pg.KEYUP:
                player.player_dx = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                key = pg.mouse.get_pressed()
                if key[0] and not bullet.bullet_isAlive:
                    bullet.create()

        game.clock.tick(game.FPS)
        return isRunning

    def start(self):
        enemy.create()
        isRunning = True
        while isRunning:
            self.model_update()
            self.display_redraw()
            isRunning = self.event_processing()
        pg.quit()


class Player:
    def __init__(self, srcImg, countHP, speed, srcHP):
        self.playerImg = pg.image.load(srcImg)
        self.playerWidth, self.playerHeight = self.playerImg.get_size()
        self.score = 0
        self.player_gap = 10
        self.player_velocity = speed
        self.player_dx = 0
        self.player_x = game.screen_width / 2 - self.playerWidth / 2
        self.player_y = game.screen_height - self.playerHeight - self.player_gap
        self.countHP = countHP
        self.hpImg = pg.image.load(srcHP)

    def update_model(self):
        self.player_x += self.player_dx
        if self.player_x < 0:
            self.player_x = 0
        if self.player_x > game.screen_width - self.playerWidth:
            self.player_x = game.screen_width - self.playerWidth

        if not game.isGameOver:
            recEnemy = pg.Rect(enemy.enemy_x, enemy.enemy_y, enemy.enemyWidth, enemy.enemyHeight)
            recPlayer = pg.Rect(self.player_x, self.player_y, self.playerWidth, self.playerHeight)
            if recEnemy.colliderect(recPlayer):
                if self.countHP == 1:
                    game.isGameOver = True
                else:
                    self.countHP -= 1
                    enemy.enemy_isAlive = False


class Enemy:
    def __init__(self, srcImg, speed):
        self.enemyImg = pg.image.load(srcImg)
        self.enemyWidth, self.enemyHeight = self.enemyImg.get_size()
        self.enemy_dx = 0
        self.enemy_dy = speed
        self.enemy_x = 0
        self.enemy_y = 0
        self.enemy_isAlive = False

    def update_model(self):
        self.enemy_x += self.enemy_dx
        self.enemy_y += self.enemy_dy
        if self.enemy_y > game.screen_height or not self.enemy_isAlive:
            self.create()

        if bullet.bullet_isAlive:
            recEnemy = pg.Rect(self.enemy_x, self.enemy_y, self.enemyWidth, self.enemyHeight)
            recBullet = pg.Rect(bullet.bullet_x, bullet.bullet_y, bullet.bulletWidth, bullet.bulletHeight)
            if recEnemy.colliderect(recBullet):
                self.create()
                bullet.bullet_isAlive = False
                player.score += 50

    def create(self):
        self.enemy_x = random.randint(0, game.screen_width - self.enemyWidth)
        self.enemy_y = 0
        self.enemy_isAlive = True


class Bullet:
    def __init__(self, srcImg, speed):
        self.bulletImg = pg.image.load(srcImg)
        self.bulletWidth, self.bulletHeight = self.bulletImg.get_size()
        self.bullet_x = 0
        self.bullet_y = 0
        self.bullet_dy = -speed
        self.bullet_isAlive = False

    def update_model(self):
        self.bullet_y += self.bullet_dy
        if self.bullet_y < 0:
            self.bullet_isAlive = False

    def create(self):
        self.bullet_x = player.player_x + self.bulletWidth / 2
        self.bullet_y = player.player_y - self.bulletHeight
        self.bullet_isAlive = True


# Игра
game = Game()
# Игрок
player = Player('src/player.png', 3, 5, 'src/hp.png')
# Пуля
bullet = Bullet('src/bullet.png', 5)
# Противник
enemy = Enemy('src/enemy.png', 2)


game.start()
