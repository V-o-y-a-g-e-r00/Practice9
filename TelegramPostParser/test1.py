from Funcs import *

from telethon.sync import TelegramClient
from telethon import functions, types
import datetime

dIdHash= open('IdHash.txt', 'r')
api_id = dIdHash.readline().splitlines()[0]
api_hash = dIdHash.readline().splitlines()[0]
session_name = dIdHash.readline().splitlines()[0]
dIdHash.close()

INPUT_CHANNEL = 'PrInput' #PrInput viewrussia

with TelegramClient('TregLeg2', api_id, api_hash) as client: #для исключений
	limit = 10
	cur_id = 0
	while True:
		result = client(functions.messages.GetHistoryRequest(
			peer=INPUT_CHANNEL, offset_id=cur_id, offset_date=0, #viewrussia
			add_offset=0, limit=limit, max_id=0, min_id=0, hash=0,
		))
		result=result.messages
		for i in range(len(result)):
			nic=result[i]
			
			print('--------------start-------------------------')
			print(nic)
			print('------------------end---------------------\n\n')
			
			
		if len(result) < limit: #Если постов нашлось меньше, чем мы пытались получить.
			break
		cur_id = result[-1].id


