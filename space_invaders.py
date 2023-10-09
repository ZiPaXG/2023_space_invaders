import pygame as pg
from models.game import Game
from models.player import Player
from models.enemy import Enemy
from models.bullet import Bullet
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
# Игра
game = Game(pg, f'{path}\\background.wav', path)
# Игрок
player = Player(pg, game, f'{path}\\player.png', 3, 5, f'{path}\\hp.png', f'{path}\\explosion.wav')
# Пуля
bullet = Bullet(pg, f'{path}\\bullet.png', 5, f'{path}\\laser.wav')
# Противник
enemy = Enemy(pg, f'{path}\\enemy.png', 2)


game.start(pg, enemy, player, bullet)
