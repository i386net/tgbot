from telegram.ext import Updater, CommandHandler, MessageHandler, Filters# импорт классов
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
import logging
from bot_key import api_key, PROXY
# import re
# from uuid import uuid4
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def kb_on(bot, update):
    chat_id = update.message.chat.id
    calc_kb = [['1', '2', '3', '+'],
          ['4', '5', '6', '-'],
          ['7', '8', '9', '*'],
          ['.', '0', '=', ':']]
    kb = ReplyKeyboardMarkup(keyboard=calc_kb)
    bot.send_message(chat_id=chat_id, text='Lets start!', reply_markup=kb)


def kb_kill(bot, update):
    chat_id = update.message.chat.id
    reply_markup = ReplyKeyboardRemove()
    bot.send_message(chat_id=chat_id, text="BB!", reply_markup=reply_markup)


def get_user_expression(bot, update, user_data):

    key = 'user_expression'
    res_key = 'result'
    operators = '-+:*'

    value = update.message.text
    #user_data.setdefault(key, []).append(value)
    #value = user_data.get(key, '') + update.message.text
    #user_data[key] = value
    #if value.endswith('='):
    #    value = user_data[key][:-1]
    #    result = user_data.get(res_key, user_data)
    #    print(value)
    user_expression = user_data.setdefault(key, [])
    user_expression.append(value)
    if value.endswith('='):
        tmp_list = []
        n = ''
        for v in user_data[key]:
            if v not in operators:

                n += v
                print(n)
                tmp_list.append(v)

                continue

            if v in operators:
                n = ''
                op = v
                tmp_list.append(op)

        print(tmp_list)
    #print(user_data.values())





def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    bot = Updater(api_key, request_kwargs=PROXY)
    dp = bot.dispatcher

    dp.add_handler(MessageHandler(Filters.text, get_user_expression, pass_user_data=True))

    dp.add_handler(CommandHandler('kbon', kb_on))
    dp.add_handler(CommandHandler('kboff', kb_kill))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    bot.start_polling()
    bot.idle()


if __name__ == '__main__':
    main()
