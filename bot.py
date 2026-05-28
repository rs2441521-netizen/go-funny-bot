import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get('BOT_TOKEN')

JOKES = [
    "Tere jokes sunke Google bhi 'I am feeling lucky' bolta hai 😂",
    "Tu itna funny hai ki meme bhi tujhe dekh ke haste hain 🤣",
    "Bhai tu comedy ka CEO hai kya? 🔥"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Go Funny Bot me tera swagat hai! 😂\nKuch bhi message bhej, main roast karunga')

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(JOKES))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_polling()
