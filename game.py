"""
Chapitre 11.1

Classes pour représenter un personnage.
"""



import random

import utils


class Weapon:

	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name

	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)



class Character:
	def __init__(self, name, max_hp, attack, defense, level, weapon, hp):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp = max_hp


	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""



def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
