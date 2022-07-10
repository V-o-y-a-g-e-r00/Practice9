from telethon.sync import TelegramClient
from telethon import functions, types
import datetime

dIdHash= open('IdHash.txt', 'r')
api_id = dIdHash.readline().splitlines()[0]
api_hash = dIdHash.readline().splitlines()[0]
session_name = dIdHash.readline().splitlines()[0]
dIdHash.close()

with TelegramClient('TregLeg2', api_id, api_hash) as client: #для исключений
	limit = 100
	cur_id = 0
	while True:
		result = client(functions.messages.GetHistoryRequest(
			peer='viewrussia', offset_id=cur_id, offset_date=0,
			add_offset=0, limit=limit, max_id=0, min_id=0, hash=0,
		))
		result=result.messages
		if len(result) < limit:
			break
		for i in range(len(result)):
			if result[i].message!='':
				nic=result[i].message
				
				print('--------------start-------------------------\n\n')
				print(nic)
				print('------------------end---------------------\n\n')
				
				with open('result.txt', 'ab') as f:
					f.write(nic.encode('utf-8'))
					f.write('\n\n\n'.encode('utf-8'))
		cur_id = result[-1].id