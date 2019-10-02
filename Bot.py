import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from OMDB import getRating


def start(bot,update):
    bot.send_message(chat_id = update.message.chat_id , text = "Welcome to MovieFy... \n Enter the movie name to get its rating..!!!! ")


def ratings(bot,update):
    bot.send_chat_action(chat_id = update.message.chat_id, action = 'typing')
    movie_name = update.message.text
    movie_rating = getRating(movie_name)
    
    message_text = ""
    if movie_rating:
        message_text = f"Rating for {movie_name} is {movie_rating}"
    else:
        message_text = f"Movie '{movie_name}' not found. Check for typos and try again."
    
    bot.send_message(chat_id = update.message.chat_id, text = message_text)


if __name__ == "__main__":
    token = os.getenv('TOKEN')
    updater = Updater(token)
    dispatcher = updater.dispatcher
    bot = telegram.Bot(token)

    start_handler = CommandHandler("start", start)
    ratings_handler = MessageHandler(Filters.text, ratings)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ratings_handler)

    updater.start_polling()
    updater.idle()
