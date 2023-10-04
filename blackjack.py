
import random 
"""
playable blackjack game (I don't know how to play blackjack exactly, so this is to the best of my understanding )
run with python3 blackjack.py
"""

values  = {"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":11,"queen":12,"king":13,"ace":14}

class card:
	def __init__(self, suit, rank ):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return f"the {self.rank} of {self.suit}"
class deck:
	suits = ("hearts","diamonds","clubs","spades")
	ranks = ("two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace")
	

	def __init__(self):
		self.all_cards = []
		for suit in deck.suits:
			for rank in deck.ranks:
				self.all_cards.append(card(suit,rank))

	def shuffle(self):
		random.shuffle(self.all_cards)
	def deal_one(self):
		return self.all_cards.pop(-1) 


class player:

	def __init__(self, name, money):
		self.money = money
		self.all_cards = []
		self.name = name

	def calc_card_total(self):
		_sum = 0
		for card in self.all_cards:
			_sum+= values[card.rank]
		return _sum
	def make_wager(self):
		try:
			wager = int(input(f"Your current balance is ${self.money}. How much will you wager for this round?    "))
		except:
			print("Invalid input. Please enter a number representing your wager.   ")
			self.make_wager()
		else:
			if( wager > self.money):
				print("Sorry, you don't have enough money to make that wager.    ")
				self.make_wager()
			else:
				self.money -= wager
				return wager
	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)
	def reset_cards(self):
		self.all_cards = []

	def hasMoney(self):
		if self.money > 0:
			return True
		else:
			return False

	def add_money(self,amount):
		self.money+=amount
class dealer:
	def __init__(self,name):
		self.all_cards = []
		self.dealer_deck = deck().shuffle()
		self.name = name
	def deal_one(self):
		return self.dealer_deck.deal_one()
	def calc_card_total(self):
		_sum = 0
		for card in self.all_cards:
			_sum+= values[card.rank]
		return _sum
	def add_cards(self,new_cards):
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def reset_cards(self):
		self.dealer_deck = deck()
		self.all_cards = []
		return
	def shuffle_cards(self):
		self.dealer_deck.shuffle()
		return

def play_game():
	game_is_valid = True
	player_one = player("Player 1", 500)
	dealer_one = dealer("Mr. Dealer")
	while game_is_valid:
		print('------------------------------------')
		print("----------     New round starts   ----------")

		print("        %s      vs        %s"%(player_one.name, dealer_one.name))
		print("                %s has $%i         "%(player_one.name,player_one.money)  )
		print("\n")
		dealer_one.reset_cards()
		player_one.reset_cards()

		dealer_one.shuffle_cards()

		dealer_one.add_cards(dealer_one.deal_one())
		player_one.add_cards(dealer_one.deal_one())
		dealer_one.add_cards(dealer_one.deal_one())
		player_one.add_cards(dealer_one.deal_one())


		wager = player_one.make_wager()
		
		#show player their cards and the card of the dealer
 
		print("%s draws "%player_one.name)
		for card in player_one.all_cards:
			print( "%s (%s)"%(str(card), values[card.rank]) )
		print("%s card total is %i"%(player_one.name,player_one.calc_card_total()))
		print("dealer has %s (%s)"%(str(dealer_one.all_cards[0]), values[dealer_one.all_cards[0].rank]) )
		not_standing = True
		while not_standing:


			# ask player what they want to do
			valid_choice = False
			choice = None
			if (player_one.calc_card_total() > 16 and player_one.calc_card_total()  < 22):

				while not valid_choice:
					choice = input("Do you want to hit or stand?   ")

					if choice == "stand":
						valid_choice = True
					elif choice == "hit":
						valid_choice = True
					else:
						print("Invalid move choice. Type 'hit' or 'stand'")

			if player_one.calc_card_total()  < 17:
				player_under_17 = True
				while player_under_17:
					print("%s's card total was under 17, so they are obliged to draw another card."%player_one.name)
					#print("card added is %s"%str(dealer_one.dealer_deck.all_cards[-1]))
					player_one.add_cards(dealer_one.deal_one())
					#for card in player_one.all_cards:
					#	print(str(card))
					print("%s draws %s "%(player_one.name,str(player_one.all_cards[-1]))) 
					print("The new total is %i"%player_one.calc_card_total())
					if player_one.calc_card_total() > 16:
						player_under_17 = False
				
				print("%s current card total is %i"%(player_one.name,player_one.calc_card_total()))

			elif player_one.calc_card_total()  > 21:
				print("%s's cards are over 21. %s loses!"%(player_one.name,player_one.name))
				not_standing = False

			## evaluate the voice
			elif choice == "stand":
				print("The dealer shows their second card: %s (%s)"%(str(dealer_one.all_cards[1]), values[dealer_one.all_cards[1].rank]) ) 

				print("%s's total: %s"%(player_one.name,player_one.calc_card_total() ) ) 
				print("dealer total: %s"%dealer_one.calc_card_total())

				dealer_under_17 = False
				if dealer_one.calc_card_total() < 17:
					print("dealer must draw another card")
					dealer_under_17 = True


				while dealer_under_17:
					dealer_one.add_cards(dealer_one.deal_one())
					print("dealer draws %s (%i)"%(str(dealer_one.all_cards[-1]), values[ dealer_one.all_cards[-1].rank] ))
					if dealer_one.calc_card_total() > 16:
						dealer_under_17 = False

				print("%s's total: %s"%(player_one.name,player_one.calc_card_total() ) ) 
				print("dealer's total: %s"%dealer_one.calc_card_total())
				# win/loss scenarios
			
				if player_one.calc_card_total()  > 21 and dealer_one.calc_card_total() > 21:
					print("Both %s and dealer bust. %s loses."%(player_one.name,player_one.name))
				elif player_one.calc_card_total()  < 21 and dealer_one.calc_card_total() < 21 and player_one.calc_card_total()  > dealer_one.calc_card_total():
					print("%s wins! $%i won."%(player_one.name,2*wager))
					player_one.add_money(2*wager)
				elif player_one.calc_card_total()  < 21 and dealer_one.calc_card_total() > 21:
					print("%s wins! $%i won."%(player_one.name,2*wager))
					player_one.add_money(2*wager)
				elif player_one.calc_card_total()  < 21 and dealer_one.calc_card_total() < 21 and player_one.calc_card_total()  < dealer_one.calc_card_total():
					print("Dealer wins!")
				elif player_one.calc_card_total()  == 21 and dealer_one.calc_card_total() != 21:
					print("%s wins! $%i won."%(player_one.name,2*wager))
					player_one.add_money(2*wager)
				elif player_one.calc_card_total()  != 21 and dealer_one.calc_card_total() == 21:
					print("Dealer wins!")
				elif player_one.calc_card_total()  == 21 and dealer_one.calc_card_total() == 21:
					print("Standoff: neither wins and bets are returned.")
				elif player_one.calc_card_total()  ==  dealer_one.calc_card_total():
					print("Standoff: neither wins and bets are returned.")
					player_one.add_money(wager)

				not_standing = False
			elif choice == "hit" :
				player_one.add_cards(dealer_one.deal_one())
				print("You drew %s "%(str(player_one.all_cards[-1])))
				print("%s current card total is %i"%(player_one.name,player_one.calc_card_total()))

			elif choice == "exit" or  choice == "Exit": 
				break
			else:
				print("invalid choice, resetting round ...")
				player_one.add_money(wager)
				not_standing = False
		game_is_valid = player_one.hasMoney()
		print("--------------- End of Round ---------------")

def main():
	play_game()




if __name__ == "__main__":
	main()