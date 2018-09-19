"""

"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler  # импорт классов
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
from bot_key import api_key, PROXY

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='I\'m bot')


def echo(bot, update):
    chat = update.message.chat_id
    bot.send_message(chat_id=chat, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    results.append(
        InlineQueryResultArticle(
            id=query.title(),
            title='Title',
            input_message_content=InputTextMessageContent(query.title())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)



def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    mybot = Updater(api_key, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    #dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler('caps', caps, pass_args=True))
    dp.add_handler(InlineQueryHandler(inline_caps))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
