from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from requests import get

updater = Updater(token='994234344:AAGhFXvdPEkSGZB0LSSAbDLmaNY8DFiXL3Q', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot for Fedora Project. I count forks. Ask anything and I count it :) ")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def getForks(repoName):
    return get('https://api.github.com/repos/fedora-infra/{}'.format(repoName)).json().get('forks')


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= getForks(update.message.text))


unknown_handler = MessageHandler(Filters.text, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
