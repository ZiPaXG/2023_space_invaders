from pygame import mixer


class Game:
    def __init__(self, pg, gameMusic, path):
        pg.init()

        """ Создание дисплея с настройками """
        self.screen_width, self.screen_height = 800, 600
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.sysfont = pg.font.SysFont('arial', 34)
        self.font = pg.font.Font(f'{path}\\04B_19.TTF', 48)
        self.bg_img = pg.image.load(f'{path}\\background.png')
        self.icon_img = pg.image.load(f'{path}\\ufo.png')
        self.display = pg.display.set_mode((self.screen_width, self.screen_height))
        self.game_over_text = self.font.render('Game Over', True, 'red')
        self.w, self.h = self.game_over_text.get_size()
        self.pause_text = self.font.render('Pause', True, 'white')
        self.wPause, self.hPause = self.pause_text.get_size()
        pg.display.set_icon(self.icon_img)
        pg.display.set_caption('Space Invaders')

        """ Создание фоновой музыки """
        self.gameSound = mixer.Sound(gameMusic)
        self.gameSound.set_volume(0.4)

        """ Создание игровых процессов """
        self.isGameOver = False
        self.isPaused = False


    # Логика моделей
    def model_update(self, pg, player, enemy, bullet):
        if not self.isGameOver and not self.isPaused:
            player.update_model(pg, self, enemy)
            bullet.update_model()
            enemy.update_model(pg, self, player, bullet)

    # Отрисовка кадра
    def display_redraw(self, pg, player, enemy, bullet):
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
            self.gameSound.fadeout(1000)
        else:
            self.display.blit(self.pause_text, (self.screen_width / 2 - self.wPause / 2, self.screen_height / 2 - self.hPause / 2))
        pg.display.update()

    def event_processing(self, pg, player, bullet):
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
                if event.key == pg.K_p and not self.isGameOver:
                    self.isPaused = not self.isPaused
                    self.gameSound.fadeout(500)
            if event.type == pg.KEYUP:
                player.player_dx = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                key = pg.mouse.get_pressed()
                if key[0] and not bullet.bullet_isAlive:
                    bullet.create(player)

        self.clock.tick(self.FPS)
        return isRunning

    def start(self, pg, enemy, player, bullet):
        isRunning = True
        while isRunning:
            if not mixer.get_busy() and not self.isPaused and not self.isGameOver:
                self.gameSound.play()
            self.model_update(pg, player, enemy, bullet)
            self.display_redraw(pg, player, enemy, bullet)
            isRunning = self.event_processing(pg, player, bullet)
        pg.quit()
