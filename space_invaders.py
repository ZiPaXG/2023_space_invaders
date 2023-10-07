import pygame as pg
from models.game import Game
from models.player import Player
from models.enemy import Enemy
from models.bullet import Bullet


# Игра
game = Game(pg)
# Игрок
player = Player(pg, game, 'src/player.png', 3, 5, 'src/hp.png')
# Пуля
bullet = Bullet(pg, 'src/bullet.png', 5)
# Противник
enemy = Enemy(pg, 'src/enemy.png', 2)


game.start(pg, enemy, player, bullet)
