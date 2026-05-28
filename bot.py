import os
import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.environ.get('BOT_TOKEN')

JOKES = [
    "Tere jokes sunke Google bhi 'I am feeling lucky' daba deta hai 😂",
    "Tu itna funny hai ki meme bhi tujhe dekh ke haste hain 🤣",
    "Bhai tu comedy ka CEO hai kya? 🔥"
]

def start(update, context):
    update.message.reply_text('Go Funny Bot me swagat hai! Kuch bhi likh 😄')

def reply(update, context):
    update.message.reply_text(random.choice(JOKES))

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
updater.start_polling()
updater.idle()
