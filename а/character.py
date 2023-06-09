from colorama import Fore, Style
import time

class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0
    color = Fore.LIGHTWHITE_EX

    def __init__(self, name='', health=100, damage=1, defence=0, color=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.color = color

    def __str__(self):
        return self.get_stars()

    def get_stars(self):
        return \
            f'{self.color}' \
            f'name: {self.name}\n' \
            f'health: {self.health}\n' \
            f'damage: {self.damage}\n' \
            f'defence: {self.defence}\n' \
            f'{Style.RESET_ALL}'

    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)

    def attack(self, target):
        print(f'{self.name} атакует {target.name}')
        target.take_damage(self.damage)
        time.sleep(1)

    def is_alive(self):
        return self.health > 0
