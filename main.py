import random, vk_api, vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='260b77719a995237e89ac3aa7b8bb2b07a19804602dffc7f739f6745eb11dd9986dc5e2139d30853ded8f')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 193323157)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

command_name = 'Оксения' #имя на которое бот будет триггериться 

#Является ли данное сообщение командой?
def Is_Command(message_):
	return command_name in str(message_)

#В параметрах 1) Текст сообещния, 2) Ссылка на прикреплённый объект
def Send_Message(message_, link_attachment = ''):
	vk.messages.send(
                    key = ('497dddd12ab57e45b2078e39124c70ec3a546118'),
                    server = ('https://lp.vk.com/wh193323157'),
                    ts=('11'),
                    random_id = get_random_id(),
              	    message = message_,
              	    peer_id=event.object.peer_id,
              	    attachment = link_attachment,
            	    chat_id = event.chat_id
                    )

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        if Is_Command(event) and ('Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event)):
            if event.from_chat:
                Send_Message('Привет!')

        elif 'Ксюша' in str(event):
        	if event.from_chat:
        		Send_Message('Какая нахуй Ксюша?? Она блять Оксана!!!!')

       	elif Is_Command(event) and ('дз' and 'скинули' in str(event)):
       		if event.from_chat:
       			Send_Message('','photo94890674_457245477')
       			
       	elif Is_Command(event) and ('нюхай' and 'бебру' in str(event)):
       		if event.from_chat:
       			Send_Message('Ты охуел? Сам нюхай!!', 'video258466863_456239268')
       			
