from pygame import mixer

class Bullet:
    def __init__(self, pg, srcImg, speed, laserMusic):
        self.bulletImg = pg.image.load(srcImg)
        self.bulletWidth, self.bulletHeight = self.bulletImg.get_size()
        self.bullet_x = 0
        self.bullet_y = 0
        self.bullet_dy = -speed
        self.bullet_isAlive = False
        self.laserSound = mixer.Sound(laserMusic)
        self.laserSound.set_volume(0.4)

    def update_model(self):
        self.bullet_y += self.bullet_dy
        if self.bullet_y < 0:
            self.bullet_isAlive = False

    def create(self, player):
        self.bullet_x = player.player_x + self.bulletWidth / 2
        self.bullet_y = player.player_y - self.bulletHeight
        self.bullet_isAlive = True
        self.laserSound.play()
