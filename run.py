from pyrogram import Client
from asyncio import sleep
api_id = 6630105; api_hash = "8508c1bcfdb0c54ccc610f29fc041d99"
app = Client('test', api_id, api_hash)

with app:
	while True:
		try:
			e = app.send_message('ava_anime1', '<b>Канал был захвачен.</b>\nhttps://t.me/d3ntly/34')
			app.pin_chat_message('ava_anime1', e.message_id)
		except:
			pass
app.run()
