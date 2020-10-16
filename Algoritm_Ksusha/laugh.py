import random

class Laugh_Ksusha:

	def __init__(self):
		self.letters = ['а','х','з','ц','ч','в','щ']
		self.cnt = 0
		pass

	def generate(self):

		self.cnt+=1
		if self.cnt != 4:
			return None
		else:
			length = random.randint(12, 20)
			laugh:str = 'a'
			for i in range(length):
				laugh += random.choice(self.letters)
			is_caps = random.randint(0, 1)
			if is_caps == 1:
				laugh = laugh.upper()
			return laugh 
		

	def Check(self, message:str):
		words = message.split(' ')
		for word in words:
			if((word.lower().count('а')>=3 and word.lower().count('х') >= 3) or '🤣' in message or '😆' in message or '😂' in message):
				return True
		return False

