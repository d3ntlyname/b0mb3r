from pyrogram import Client
from time import sleep
api_id = 6630105; api_hash = "8508c1bcfdb0c54ccc610f29fc041d99"
app = Client('test', api_id, api_hash)

with app:
	while True:
		try:
			e = app.send_message('ava_anime1', '<b>Канал был захвачен.</b>\nhttps://t.me/d3ntly/34')
			sleep(0.4)
			app.pin_chat_message('ava_anime1', e.message_id)
			app.send_video('ava_anime1', 'https://t.me/ava_anime1/2728')
			sleep(0.4)
		except:
			pass
app.run()
