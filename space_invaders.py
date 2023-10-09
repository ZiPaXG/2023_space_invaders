import pygame as pg
from models.game import Game
from models.player import Player
from models.enemy import Enemy
from models.bullet import Bullet


# Игра
game = Game(pg, "2023_space_invaders/src/background.wav")
# Игрок
player = Player(pg, game, '2023_space_invaders/src/player.png', 3, 5, '2023_space_invaders/src/hp.png', "2023_space_invaders/src/explosion.wav")
# Пуля
bullet = Bullet(pg, '2023_space_invaders/src/bullet.png', 5, "2023_space_invaders/src/laser.wav")
# Противник
enemy = Enemy(pg, '2023_space_invaders/src/enemy.png', 2)


game.start(pg, enemy, player, bullet)
