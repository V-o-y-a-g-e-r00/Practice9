from telethon.sync import TelegramClient, events

# 'session_id' can be 'your_name'. It'll be saved as your_name.session
client = TelegramClient(session_name, api_id, api_hash)



client.connect()
if not client.is_user_authorized():
	client.send_code_request('+79805365457')
	client.sign_in('+79805365457', input('Enter code: '))

# ###################################
# Now you can use the connected client as you wish
INPUT_CHANNEL = 'viewrussia'
OUTPUT_CHANNEL = 'PrOutput'
#TAGS = ['#TAG1', '#TAG2']


@client.on(events.NewMessage(chats=(INPUT_CHANNEL)))
async def normal_handler(event):
#    for tag in TAGS:

#        if tag in str(event.message):

            await client.send_message(OUTPUT_CHANNEL, event.message)

client.start()
client.run_until_disconnected()

entities = client.get_dialogs(1)
print('\n'.join('{}. {}'.format(i, str(e)) for i, e in enumerate(entities)))