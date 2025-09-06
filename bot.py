from pyrogram import Client, filters

api_id = 29038990
api_hash = "056a7ce4487ce7f5f2ab274703ca8bb8"
bot_token = "7747501076:AAE2lQhL1ZvvpWJiPyOmDXfTc7N1JMmTm6c"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! I am your Auto Filter Bot.")

@app.on_message(filters.text)
async def auto_filter(client, message):
    if "hello" in message.text.lower():
        await message.reply_text("Hi! How can I help you?")

app.run()
