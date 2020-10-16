from commands import commands
from Deadline.homework import HomeWork

class Deadlines:
	deadlines = dict() #Словарь всех дедлайнов

	def __init__(self):
		pass

	def Add_Deadline(self, message_:str, conversation_id):
		print(conversation_id)
		try: 
			if conversation_id not in self.deadlines:
				self.deadlines[conversation_id] = dict()
		except:
			pass
		words=message_.split(' : ')

		try:
			if words[1] in self.deadlines[conversation_id]:
				self.deadlines[conversation_id][words[1]].append(HomeWork(words[2], words[3]))
			else:
				self.deadlines[conversation_id][words[1]] = [HomeWork(words[2], words[3])]
			response = {'message': commands['add_deadline']['message'][0],'attachment': commands['add_deadline']['attachment']}
			return response
		except BaseException:
			response = {'message': commands['add_deadline']['message'][1],'attachment': commands['add_deadline']['attachment']}
			return response

	def Get_Deadline(self, message_:str, conversation_id):
		words=message_.split(' : ')
		print(conversation_id)
		try:
			message:str = ''
			if words[1] in self.deadlines[conversation_id]:
				message = '📌 Список дз на: '+words[1]+' 📌\n\n'
				for subj in self.deadlines[conversation_id][words[1]]:
					message+='● '+subj.get_subject()+':\n&#12288; &#12288;'+subj.get_homework()+'\n\n'
			else:
				message = 'На данный день ничего нет, пиздуй-бороздуй!'
			response = {'message': message, 'attachment': ''}
			return response
		except:
			response = {'message': 'В этой беседе нет, блять, ни единой записи!', 'attachment': ''}
			return response

	def Delete_Deadline_Subject(self, message_:str, conversation_id):
		
		try:
			words=message_.split(' : ')
			message: str = ''
			if words[1] in self.deadlines[conversation_id]:
				finded_homework = self.Check(self.deadlines[conversation_id][words[1]],words[2])
				if finded_homework != None :
					self.deadlines[conversation_id][words[1]].remove(finded_homework)
					message = 'Удаление прошло успешно!'
				else:
					message = 'Такого предмета не существует на этот день, проверь на ошибочки, булочка, и не беси меня больше....'
			else:
				message = 'На данный день ничего нет, что ты, пизда копченая, хочешь удалить?'
			response = {'message': message, 'attachment': ''}
			return response
			
		except:
			response = {'message': 'В этой беседе нет, блять, ни единой записи!', 'attachment': ''}
			return response

	def Delete_Deadline(self, message_:str, conversation_id):
		try:
			words=message_.split(' : ')
			message: str = ''
			if words[1] in self.deadlines[conversation_id]:
				del self.deadlines[conversation_id][words[1]]
				message = 'Удаление прошло успешно!'
			else:
				message = 'На данный день ничего нет, что ты, пизда копченая, хочешь удалить?'
			response = {'message': message, 'attachment': ''}
			return response
		except:
			response = {'message': 'В этой беседе нет, блять, ни единой записи!', 'attachment': ''}
			return response


	def Check(self, day,subj):
		for homework in day:
			if homework.get_subject() == subj:
				return homework
		return None
