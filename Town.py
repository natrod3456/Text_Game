#########################################
# Contains neighborhood with houses
# @Author Natalie Rodriguez
# @version Winter 2018
#########################################

from Observe import Observable, Observer
from Characters import Person, Zombies, Vampires, Ghouls, Werewolves

class House(Observable, Observer):
	def __init__(self):
		self.monsters = []
		self.population = 0
		
		Observable.__init__(self)
		Observable.__init__(self)
		
		for i in range(randint(0,10)):
			choice = random.randint(1,4)
			if(choice == 1):
				self.monsters.append(Zombies())
				self.population += 1
			elif(choice == 2):
				self.monsters.append(Vampires())
				self.population += 1
			elif(choice == 3):
				self.monsters.append(Ghouls())
				self.population += 1
			elif(choice == 4):
				self.monsters.append(Werewolves())
				self.population += 1
		
	def update(self, target):
		self.monsters.pop(target)
		self.monsters.append(Person())
		print("Monster defeated. Turning into human!")
		self.population -= 1
			
class Neighborhood(Observer):
	def __init__(self):
		self.houses = 0
		self.neighbors = []
		
		#just going to make grid 3x4
		for i in range(12):
			self.neighbors.append(House())
	
		
	#def update(self, target):
		#check if all houses are empty 
		#if yes then game won and exit
		
	def showgrid(self):
		print("X X X X")
		print("X X X X")
		print("X X X X")
		
	
					