import random, vk_api, vk
from setting import main_token, group_id, message_key, server_, ts_, command_name
from bot import BotCommand
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token = main_token)
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

bot = BotCommand()
#Является ли данное сообщение командой?
def Is_Command(message_):
	return command_name in str(message_).lower()

#В параметрах 1) Текст сообещния, 2) Ссылка на прикреплённый объект
def Send_Message(post, name_user = ''):
	vk.messages.send(
                    key = (message_key),
                    server = (server_),
                    ts=(ts_),
                    random_id = get_random_id(),
              	    message = name_user+post['message'],
              	    peer_id=event.object.peer_id,
              	    attachment = post['attachment'],
            	    chat_id = event.chat_id
                    )

def Check_Woman_Logic():
	try:
		Check_Woman_Logic.a += 1
	except AttributeError:
		Check_Woman_Logic.a = 0
	if(Check_Woman_Logic.a==0):
		Send_Message('Ты охуел?')
	elif(Check_Woman_Logic.a==1):
		Send_Message('Ну не хочу')
	else:
		Send_Message('Ладно...')
		Check_Woman_Logic.a = 0

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

    	id_account = event.object['message']['from_id']
    	account_info = vk.users.get(user_ids = id_account)

    	if Is_Command(event):
    		message = event.object['message']['text'].lower()

    		if bot.Hello(message):
    			if event.from_chat:
    				Send_Message(bot.Hello(),account_info[0]['first_name'])

    		elif bot.Homework(message):
    			if event.from_chat:
    				Send_Message(bot.Homework())

    		elif bot.Bebra(message):
    			if event.from_chat:
    				Send_Message(bot.Bebra(),account_info[0]['first_name'])

    		elif 'отсоси' in str(event) or 'соси' in str(event):
    			Check_Woman_Logic()

    		elif 'добавить дз :' in message:
    			Send_Message(bot.Add_Deadline(message))

    		elif 'посмотреть дз за :' in message:
    			Send_Message(bot.Get_Deadline(message))

    		else:
    			if event.from_chat:
    				response = {'message' : 'Неверная команда, иди нахуй', 'attachment' : ''}
    				Send_Message(response)
    	elif bot.Ksusha(event.object['message']['text'].lower()):
    		if event.from_chat:
    			Send_Message(bot.Ksusha())
       	
       			
       	
       			
