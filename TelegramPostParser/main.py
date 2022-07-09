# Функции

# Основной код. Получает новые посты из канала "Красивые места России", находит в них текст и фото и посылает их в базу данных на mySQL  
from Funcs import *
from telethon.sync import TelegramClient, events

dIdHash= open('IdHash.txt', 'r')
api_id = dIdHash.readline().splitlines()[0]
api_hash = dIdHash.readline().splitlines()[0]
session_name = dIdHash.readline().splitlines()[0]
dIdHash.close()

#Отлаживаем вход в телеграмм
#print("api_id=", api_id, "api_hash=",api_hash, "session_name=", session_name, sep='')
# 'session_id' can be 'your_name'. It'll be saved as your_name.session
client = TelegramClient(session_name, api_id, api_hash)
print("Connecting to telegram...")
client.connect()
print("Connection established successfully")
if not client.is_user_authorized():
	client.send_code_request('+79805365457')
	client.sign_in('+79805365457', input('Enter code: '))

# ###################################
# Now you can use the connected client as you wish
INPUT_CHANNEL = 'PrInput' #PrInput viewrussia
OUTPUT_CHANNEL = 'PrOutput'
#TAGS = ['#TAG1', '#TAG2']

print("Waiting for new posts on", INPUT_CHANNEL, "channel...")
@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):
#    for tag in TAGS:

#        if tag in str(event.message):

	await client.send_message(OUTPUT_CHANNEL, event.message)

	#Получаем только текст из сообщения
	Path=MessageToBase(event.message)
	await client.download_media(event.message.media, Path)
	print("Waiting for new posts on", INPUT_CHANNEL, "channel...")

client.start()
client.run_until_disconnected()

entities = client.get_dialogs(1)
print('\n'.join('{}. {}'.format(i, str(e)) for i, e in enumerate(entities)))






