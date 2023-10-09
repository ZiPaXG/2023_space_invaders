import pygame.mixer

class Player:
    def __init__(self, pg, game, srcImg, countHP, speed, srcHP, explosionMusic):
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
        self.explosionSound = pygame.mixer.Sound(explosionMusic)

    def update_model(self, pg, game, enemy):
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
                    self.explosionSound.play()
                    game.isGameOver = True
                else:
                    self.countHP -= 1
                    enemy.enemy_isAlive = False
                    self.explosionSound.play()
