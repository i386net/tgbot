"""
Задание

Установите модуль ephem
Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском,
например /ephem Mars
В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
При помощи условного оператора if и ephem.constellation научите бота отвечать,
в каком созвездии сегодня находится планета.
"""

from telegram.ext import Updater, CommandHandler  # импорт классов
import logging
import ephem as e
from bot_key import api_key, PROXY


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def planet_info(bot, update):
    planet = update.message.text.split()[1]
    try:
        planet = getattr(e, planet)()
        planet.compute()
        constellation = e.constellation(planet)
        return update.message.reply_text(' 💫 '.join(constellation))
    except AttributeError:
        message = 'No planet "{}" was found'.format(planet)
        return update.message.reply_text(message)


def main():
    mybot = Updater(api_key, request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', planet_info))
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
