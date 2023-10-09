import random

class Enemy:
    def __init__(self, pg, srcImg, speed):
        self.enemyImg = pg.image.load(srcImg)
        self.enemyWidth, self.enemyHeight = self.enemyImg.get_size()
        self.enemy_dx = 0
        self.enemy_dy = speed
        self.enemy_x = 0
        self.enemy_y = 0
        self.enemy_isAlive = False

    def update_model(self, pg, game, player, bullet):
        self.enemy_x += self.enemy_dx
        self.enemy_y += self.enemy_dy
        if self.enemy_y > game.screen_height or not self.enemy_isAlive:
            self.create(game)

        if bullet.bullet_isAlive:
            recEnemy = pg.Rect(self.enemy_x, self.enemy_y, self.enemyWidth, self.enemyHeight)
            recBullet = pg.Rect(bullet.bullet_x, bullet.bullet_y, bullet.bulletWidth, bullet.bulletHeight)
            if recEnemy.colliderect(recBullet):
                self.create(game)
                bullet.bullet_isAlive = False
                player.score += 50

    def create(self, game):
        self.enemy_x = random.randint(0, game.screen_width - self.enemyWidth)
        self.enemy_y = 0
        self.enemy_isAlive = True