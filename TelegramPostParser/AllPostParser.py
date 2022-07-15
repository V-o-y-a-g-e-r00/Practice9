from Funcs import *

from telethon.sync import TelegramClient
from telethon import functions, types
import datetime

dIdHash= open('IdHash.txt', 'r')
api_id = dIdHash.readline().splitlines()[0]
api_hash = dIdHash.readline().splitlines()[0]
session_name = dIdHash.readline().splitlines()[0]
dIdHash.close()

INPUT_CHANNEL = 'viewrussia' #PrInput viewrussia

with TelegramClient('TregLeg2', api_id, api_hash) as client: #для исключений
	limit = 100
	cur_id = 0
	while True:
		result = client(functions.messages.GetHistoryRequest(
			peer=INPUT_CHANNEL, offset_id=cur_id, offset_date=0, #viewrussia
			add_offset=0, limit=limit, max_id=0, min_id=0, hash=0,
		))
		result1=result.messages
		for i in range(len(result1)):
			nic=result1[i]
			
			Path=MessageToBase(nic, 'MsgOutAllPosts.txt')
			client.download_media(nic.media, Path)
			print('--------------start-------------------------')
			print(nic)
			print('------------------end---------------------\n\n')
			
		if len(result1) < limit: #Если постов нашлось меньше, чем мы пытались получить.
			break
		cur_id = result1[-1].id


