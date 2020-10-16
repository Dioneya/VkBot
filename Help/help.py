class Help:
	def __init__(self):
		self.get_comands_list()
		pass

	commands = [
	'◂ Приветствие - Оксения, (привет; ку; хай; хелло; хеллоу)',
	'◂ Вызов списка команд - Оксения, help ; Оксения, команды',
	'◂ Добавить дз - синтаксис команды "Оксения, добавить дз : на_какое_событие : название_предмета : домашнее задание"',
	'◂ Посмотреть дз - синтаксис команды "Оксения, посмотреть дз за : на_какое_событие"',
	'◂ Выбрать наугад участника беседы - Оксения, сделай рандом"'
	]

	triggers = [
	'нюхай бебру, Ксюша, Текстильщик, дз скинули'
	]

	def get_comands_list(self):
		help_str:str = "❗Список команд бота по обращению:❗\n&#12288;\n".upper()
		for command in self.commands:
			help_str += command +'\n'

		help_str += "&#12288;\n❗Тригеррные слова и выражения для бота:❗\n&#12288;\n".upper()

		for trigger in self.triggers:
			help_str += trigger +'; '

		response = {'message':help_str, 'attachment': ''}
		return response
