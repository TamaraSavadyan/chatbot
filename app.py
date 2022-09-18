from tokenize import Token
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URl

# global bot, TOKEN

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()

    # for debugging
    print("got text msg: ", text)

    if text == '/start':
        bot_welcome = """
        Welcome to coolAvatar bot, 
        the bot is using the service from http://avatars.adorable.io/ to generate cool 
        looking avatars based on the name you enter 
        so please enter a name and the bot will reply with an avatar for your name.
        """    
        # send welcoming msg
        bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message=msg_id)
   
