import random, vk_api, vk
from setting import main_token, group_id, message_key, server_, ts_, command_name
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token = main_token)
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, group_id)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

#Является ли данное сообщение командой?
def Is_Command(message_):
	return command_name in str(message_).lower()

#В параметрах 1) Текст сообещния, 2) Ссылка на прикреплённый объект
def Send_Message(message_, link_attachment = ''):
	vk.messages.send(
                    key = (message_key),
                    server = (server_),
                    ts=(ts_),
                    random_id = get_random_id(),
              	    message = message_,
              	    peer_id=event.object.peer_id,
              	    attachment = link_attachment,
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
    	print(account_info)
    	print(account_info[0]['first_name'])
    	if Is_Command(event):
    		if ('ку' in str(event).lower() or 'привет' in str(event).lower() or 'хай' in str(event).lower() or 'хелло' in str(event).lower() or 'хеллоу' in str(event).lower()):
    			if event.from_chat:
    				Send_Message(account_info[0]['first_name']+', привет!')
    		elif 'дз' and 'скинули' in str(event):
    			if event.from_chat:
    				Send_Message('','photo94890674_457245477')
    		elif 'нюхай' and 'бебру' in str(event):
    			if event.from_chat:
    				Send_Message(account_info[0]['first_name']+', Ты охуел? Сам нюхай!!', 'video258466863_456239268')
    		elif 'отсоси' in str(event) or 'соси' in str(event):
    			Check_Woman_Logic()
    		else:
    			if event.from_chat:
    				Send_Message('Неверная команда, иди нахуй')
    	elif 'Ксюша' in str(event):
    		if event.from_chat:
    			Send_Message('Какая нахуй Ксюша?? Она блять Оксана!!!!')
       	
       			
       	
       			
