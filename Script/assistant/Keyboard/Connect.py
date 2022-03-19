from Script.assistant.TgCalls.Clients import *

with Client("Indian Music Bot", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with abhi as app:
    me_abhi = app.get_me()
