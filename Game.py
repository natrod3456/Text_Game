#########################################
# python file with main method to run game
# @Author Natalie Rodriguez
# @version Winter 2018
#########################################
from Town import Neighborhood
from Characters import Player

class Zork:
	def __init__(self):
		 self.myPlayer = Player()
		 self.grid = Neighborhood()
		 
	def splashScreen(self):
		print("Welcome to Zork!")
		print("Just attack some houses and see if you survive")
		print("You only have an HP from 100-125 so watch out")
		
	
	def play(self):
		while self.hp <= 0:
			print("You can attack one house at a time")
			print("A weapon will be randomly chosen for you")
			print("Choices:")
			print("Attack")
			print("Run")
			i = raw_input("What would you like to do?")
			self.input(i)
	
	def input(self, i):
		if (n == "Attack"):
			power = self.myPlayer.attack()
			#use this power to attack all monsters in a house
			
			
		elif (n == "Run"):
			sys.exit("At least you tried")	
		
		else:
			print("Not a valid command")
	
def main():
	game = Game()
	p = game.myPlayer
	n = game.grid
	
	game.splashScreen()
	game.play()	