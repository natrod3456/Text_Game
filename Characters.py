#########################################
# Contains all NPCs and Player 
# @Author Natalie Rodriguez
# @version Winter 2018
#########################################
import random
from Observe import Observable
from Weapons import HersheyKiss, SourStraw, ChocolateBar, NerdBomb

class NPC(Observable):
	def __init__(self, name, hp, atk):
		self.name = name
		self.hp = hp
		self.atk = atk
		
	#def damage(self, damage):
	#	if(self.name != "Person"):
	#		self.hp -= damage
	#			if(self.hp <= 0):
	#				Observable.update(self)
			
		
class Player(Observable):
	def __init__(self):
		self.hp = random.randint(100,125)
		self.atk = random.randint(10,20)
		self.weapons = [HersheyKiss()]
		for i in range(9):
			choice = random.randint(1,4)
			if(choice == 1):
				self.weapons.append(HersheyKiss())
			elif(choice == 2):
				self.weapons.append(SourStraw())
			elif(choice == 3):
				self.weapons.append(ChocolateBar())
			elif(choice == 4):
				self.weapons.append(NerdBomb())
		
		#def damage(self, damage):
		#	self.hp = self.hp - damage
		#		if(self.hp <= 0):
		#			Observable.update(self)
		
		#attacking with a random weapon because couldn't figure out how to select one :-)			
		def attack(self):
			choice = random.randint(1,4)
			self.weapons[choice].durability -= 1
			if(self.weapons[choice].durability == 0):
				self.weapons.pop(choice)
			power = self.weapons[choice].modifier * self.atk
			return power
		
class Person(NPC):
	def __init__(self):
		NPC.__init__(self,"Person",100,-1,)
		
class Zombies(NPC):
	def __init__(self):
		NPC.__init__(self,"Zombie",random.randint(50,100),random.randint(0,10))	
	
class Vampires(NPC):
	def __init__(self):
		NPC.__init__(self,"Vampire",random.randint(100,200),random.randint(10,20))
	
class Ghouls(NPC):
	def __init__(self):
		NPC.__init__(self,"Ghoul",random.randint(40,80),random.randint(15,30))
	
class Werewolves(NPC):
	def __init__(self):
		NPC.__init__(self,"Werewolf",200,random.randint(0,40))
	
