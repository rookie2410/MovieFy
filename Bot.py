import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from OMDB import get_movie_info


def start(bot,update):
    bot.send_message(chat_id = update.message.chat_id , text = "Welcome to MovieFy... \n Enter the movie name to get its rating..!!!! ")


def ratings(bot,update):
    bot.send_chat_action(chat_id = update.message.chat_id, action = 'typing')
    movie_name = update.message.text
    movie_info = get_movie_info(movie_name)
    
    message_text = ""
    
    if movie_info:
        rating_string = f"IMDb Rating: {movie_info['imdb_rating']}\n"
        for rating in movie_info['ratings']:
            rating_string += f"{rating['Source']}: {rating['Value']}\n"
               
        message_text = (f"{movie_info['title']} ({movie_info['year']}):\n\n" + 
            f"Plot:\n{movie_info['plot']}\n\n" +
            f"Starring:\n{movie_info['actors']}\n\n" +
            f"Ratings:\n{rating_string}"
            ) 
        
    else:
        message_text = f"Movie '{movie_name}' not found. Check for typos and try again."
    
    bot.send_message(chat_id = update.message.chat_id, text = message_text)


if __name__ == "__main__":
    #token = os.getenv('TOKEN')
    token = 976482014:AAHu8-lx_d7T8_tb1Z3uGr5JJCwtbJskKkQ
    updater = Updater(token)
    dispatcher = updater.dispatcher
    bot = telegram.Bot(token)

    start_handler = CommandHandler("start", start)
    ratings_handler = MessageHandler(Filters.text, ratings)
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ratings_handler)

    updater.start_polling()
    updater.idle()
