from telethon import TelegramClient, events
import logging
from auth import authorize

import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_name = 'my_session'
TOKEN = os.getenv('BOT_TOKEN')
client = TelegramClient(session_name, api_id, api_hash).start(bot_token=TOKEN)

user_data = {}

@client.on(events.NewMessage(pattern='/login'))
async def cmd_login(event):
    user_id = event.sender_id
    user_data[user_id] = {'step': 'login'}
    await event.respond('Enter login:')

@client.on(events.NewMessage())
async def msg_handler(event):
    user_id = event.sender_id
    text = event.text.strip()
    if user_id not in user_data:
        return
    if text.startswith('/'):
        return

    step = user_data[user_id]['step']
    if step == 'login':
        user_data[user_id] = {'step': 'password', 'login': text}
        await event.respond('Enter password:')
    elif step == 'password':
        login = user_data[user_id]['login']
        password = text
        try:
            await event.respond('Try to authorize')
            success = authorize(login, password)
            if success:
                await event.respond('Authorization success')
            else:
                await event.respond('Authorization failed. Check login or password')
        except Exception as e:
            logging.error('Error authorization')
            await event.respond('Error authorization')

