from commands import commands
class BotCommand:
	

	def __init__(self):
		self.Ksusha_cnt = 0
		pass
	
	def __get_reponse(self,name_of_command:str):
		response = {'message': commands[name_of_command]['message'],'attachment': commands[name_of_command]['attachment']}
		return response

	def __is_has_trigged_word_in_command(self,command,message_):
		words = message_.split(' ')
		triggered:bool = False 
		for word in words: 
			try:
				if word in commands[command]['triggers']:
					triggered = True
					break	
			except:
				print('null')
		return triggered


	def Hello(self, message_ = None):
		if message_ != None:
			return self.__is_has_trigged_word_in_command('hello',message_)
		else:
			return self.__get_reponse('hello')
		
	def Bebra(self, message_ = None):
		if message_!= None:
			return commands['bebra']['triggers'][0] and commands['bebra']['triggers'][1] in message_
		else:
			return self.__get_reponse('bebra')


	def Ksusha(self, message_ = None):
		if message_ != None:
			return self.__is_has_trigged_word_in_command('Ksusha',message_)
		else:
			if self.Ksusha_cnt >= 5:
				self.Ksusha_cnt = 0
				return self.__get_reponse('Ksusha')
			else:
				self.Ksusha_cnt += 1
				return None
			

	def Tekstilshik(self, message_ = None):
		if message_ != None:
			return self.__is_has_trigged_word_in_command('Tekstilshik',message_)
		else:
			return self.__get_reponse('Tekstilshik')


	def Homework(self, message_ = None):
		if message_ != None:
			return commands['homework']['triggers'][0] and (commands['homework']['triggers'][1] or commands['homework']['triggers'][2]) in message_
		else:
			return self.__get_reponse('homework')

	

	def We_are_Bitches(self):
		return self.__get_reponse('we_are_bitches')