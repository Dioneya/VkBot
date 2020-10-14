from commands import commands
from homework import HomeWork
class BotCommand:
	deadlines = dict() #Словарь всех дедлайнов

	def __init__(self):
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
			return self.__get_reponse('Ksusha')

	def Homework(self, message_ = None):
		if message_ != None:
			return commands['homework']['triggers'][0] and (commands['homework']['triggers'][1] or commands['homework']['triggers'][2]) in message_
		else:
			return self.__get_reponse('homework')
	
	def Add_Deadline(self, message_:str):
		words=message_.split(' : ')
		try:
			if words[1] in self.deadlines:
				self.deadlines[words[1]].append(HomeWork(words[2], words[3]))
			else:
				self.deadlines[words[1]] = [HomeWork(words[2], words[3])]
			response = {'message': commands['add_deadline']['message'][0],'attachment': commands['add_deadline']['attachment']}
			return response
		except BaseException:
			response = {'message': commands['add_deadline']['message'][1],'attachment': commands['add_deadline']['attachment']}
			return response

	def Get_Deadline(self, message_:str):
		words=message_.split(' : ')
		try:
			message:str = ''
			if words[1] in self.deadlines:
				message = 'Список дз за: '+words[1]+'\n\n'
				for subj in self.deadlines[words[1]]:
					message+=subj.get_subject()+':\n'+subj.get_homework()+'\n\n'
			else:
				message = 'На данный день ничего нет, пиздуй-бороздуй!'
			response = {'message': message, 'attachment': ''}
			return response
		except:
			response = {'message': 'Произошла какая-то блять ошибка...', 'attachment': ''}
			return response

