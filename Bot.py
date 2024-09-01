import telebot
from texts import *
from button import *
import logging
from dotenv import load_dotenv
import os
load_dotenv()

my_token = os.getenv('TOKEN')
my_id = os.getenv('TO_CHAT_ID')

logging.basicConfig(level=logging.WARNING, filename='my_logging.log',
                    format='%(asctime)s - %(name)s - ''%(levelname)s - %(message)s', datefmt='%d/%m/%y %I:%M:%S',
                    encoding='utf-8')


bot = telebot.TeleBot(my_token)

counter = [0, 0]
name_animal = None




try:
    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('start_test')
        item2 = types.KeyboardButton('friends_club')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, text_Hi.format(message.from_user), reply_markup=markup)

    @bot.message_handler(func=lambda message: message.text == 'start_test' or message.text == 'friends_club'
                         or message.text == "прохождение теста" or message.text == "вернуться" or
                                          message.text == 'попробывать ещё раз' or
                                              message.text == 'связаться с сотрудником' or
                                              message.text == 'попробывать ещё раз' or
                                              message.text == 'поделиться ботом' or message.text == 'перейти на сайт')
    def zoo_test(message):
        global name_animal
        if message.text == 'start_test' or message.text == 'попробывать ещё раз':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('начать тест')
            item_back
            markup.add(item, item_back)
            bot.send_message(message.chat.id, text_start_test.format(message.from_user), reply_markup=markup)
        elif message.text == 'friends_club':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('перейти на сайт')
            item_back
            markup.add(item, item_back)
            bot.send_message(message.chat.id, text_friends_club.format(message.from_user), reply_markup=markup)
        elif message.text == 'вернуться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('start_test')
            item1 = types.KeyboardButton('friends_club')
            markup.add(item, item1)
            bot.send_message(message.chat.id, text_Hi.format(message.from_user), reply_markup=markup)
        elif message.text == 'поделиться ботом':
            bot_username = bot.get_me().username
            chat_link = f"https://t.me/{bot_username}?start={message.from_user.id}"
            bot.send_message(message.chat.id,
                             f"Поделись нашим ботом с друзьями, используя эту ссылку\n{chat_link}")
        elif message.text == 'связаться с сотрудником':
            bot.send_message(message.chat.id, text_connect)
            bot.send_message(970891330, text=name_animal)
        elif message.text == 'перейти на сайт':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_back
            markup.add(item_back)
            bot.send_message(message.chat.id, text_to_site.format(message.from_user), reply_markup=markup)





    @bot.message_handler(content_types=['text'])
    def start_test(message):
        global name_animal
        if message.text == 'начать тест':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('жара')
            item2 = types.KeyboardButton('холод')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Что больше любит твой друг?".format(message.from_user),
                             reply_markup=markup)
        elif message.text == 'жара' or message.text == 'холод':
            if message.text == 'холод':
                counter[0] = 1
            elif message.text == 'жара':
                counter[0] = 2
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('социум')
            item2 = types.KeyboardButton('одиночки')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Он общительный или любит уединение?".format(message.from_user),
                             reply_markup=markup)
        elif message.text == 'социум' or message.text == 'одиночки':
            if message.text == 'социум':
                counter[1] = 3
            elif message.text == 'одиночки':
                counter[1] = 4
            if counter[0] == 1:
                if counter[1] == 3:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton('ластоногий')
                    item2 = types.KeyboardButton('не ластоногий')
                    item_back
                    markup.add(item1, item2, item_back)
                    bot.send_message(message.chat.id, "Как думаешь он ластоногий?".format(message.from_user),
                                     reply_markup=markup)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    item1 = types.KeyboardButton('кошка')
                    item2 = types.KeyboardButton('не кошка')
                    item_back
                    markup.add(item1, item2, item_back)
                    bot.send_message(message.chat.id, "Может быть это большая кошка?".format(message.from_user),
                                     reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('хищник')
                item2 = types.KeyboardButton('травоядный')
                item_back
                markup.add(item1, item2, item_back)
                bot.send_message(message.chat.id, "Твой зверь хищник или травоядный?"
                             .format(message.from_user), reply_markup=markup)
        elif message.text == 'ластоногий':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('суровый')
            item2 = types.KeyboardButton('милый')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Хочешь чтомы он был суровый или милый?".format(message.from_user),
                         reply_markup=markup)
        elif message.text == 'не ластоногий':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('земля')
            item2 = types.KeyboardButton('вода')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Где же он обитает?".format(message.from_user),
                         reply_markup=markup)
        elif message.text == 'кошка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('пятнистый')
            item2 = types.KeyboardButton('однотонный')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Какой цвет шкурки у этой кошки?".format(message.from_user),
                         reply_markup=markup)
        elif message.text == 'не кошка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('наземный')
            item2 = types.KeyboardButton('воздушный')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "наземный или любит полетать?".format(message.from_user),
                         reply_markup=markup)
        elif message.text == 'хищник':
            if counter[1] == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('в воде')
                item2 = types.KeyboardButton('на земле')
                item3 = types.KeyboardButton('в воздухе')
                item_back
                markup.add(item1, item2, item3, item_back)
                bot.send_message(message.chat.id, "где же он охотится?".format(message.from_user),
                             reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('теплокровные')
                item2 = types.KeyboardButton('не теплокровные')
                item_back
                markup.add(item1, item2, item_back)
                bot.send_message(message.chat.id, "Его вид теплокровный?".format(message.from_user),
                                 reply_markup=markup)
        elif message.text == 'травоядный':
            if counter[1] == 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('приручен')
                item2 = types.KeyboardButton('не приручен')
                item_back
                markup.add(item1, item2, item_back)
                bot.send_message(message.chat.id, "Приручил ли его человек?".format(message.from_user),
                                 reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('связаться с сотрудником')
                item2 = types.KeyboardButton('попробывать ещё раз')
                item_back
                item_share
                markup.add(item1, item2, item_back, item_share, item_connect)
                name_animal = 'Дикдик'
                photo = open('изображения\Дикдик.jpeg', 'rb')
                bot.send_photo(message.chat.id, photo, caption=name_animal+text_dicdic, reply_markup=markup)

        elif message.text == 'суровый':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Морж"
            photo = open('изображения\Морж.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_walrus, reply_markup=markup)
        elif message.text == 'милый':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Морской котик"
            photo = open('изображения\Морской котик.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_seal, reply_markup=markup)
        elif message.text == 'земля':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Альпака"
            photo = open('изображения\Альпака.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_alpaca, reply_markup=markup)
        elif message.text == 'вода':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Папуасский пингвин"
            photo = open('изображения\Папуасский пингвин.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_papuan, reply_markup=markup)
        elif message.text == 'пятнистый':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back,item_share)
            name_animal = "Снежный барс"
            photo = open('изображения\Барс.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_snow_leopard, reply_markup=markup)
        elif message.text == 'однотонный':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Пума"
            photo = open('изображения\Пума.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_cougar, reply_markup=markup)
        elif message.text == 'наземный':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Белогрудый ёж"
            photo = open('изображения\Ёж.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_hedgehog, reply_markup=markup)
        elif message.text == 'воздушный':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Мохноногий сыч"
            photo = open('изображения\Мохноногий сыч.png', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_owl, reply_markup=markup)
        elif message.text == 'в воде':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Пингвин гумбольдта"
            photo = open('изображения\Пингвин гумбольдта.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_humboldt, reply_markup=markup)
        elif message.text == 'в воздухе':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Нильский крылан"
            photo = open('изображения\Нильский крылан.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_bat, reply_markup=markup)
        elif message.text == 'на земле':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('собак')
            item2 = types.KeyboardButton('кошек')
            item3 = types.KeyboardButton('других')
            item_back
            markup.add(item1, item2, item3, item_back)
            bot.send_message(message.chat.id, "Кого ты больше любишь?".format(message.from_user),
                         reply_markup=markup)
        elif message.text == 'собак':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Феник"
            photo = open('изображения\Феник.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_fenech, reply_markup=markup)
        elif message.text == 'кошек':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Лев"
            photo = open('изображения\Лев.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_leo, reply_markup=markup)
        elif message.text == 'других':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Сурикат"
            photo = open('изображения\Сурикат.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_meerkat, reply_markup=markup)
        elif message.text == 'теплокровные':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('милашка')
            item2 = types.KeyboardButton('опастный')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Он дружелюбный или опасен?".format(message.from_user),
                             reply_markup=markup)
        elif message.text == 'милашка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Малая панда"
            photo = open('изображения\Малая панда.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_panda, reply_markup=markup)
        elif message.text == 'опастный':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Медоед"
            photo = open('изображения\Медоед.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_badger, reply_markup=markup)
        elif message.text == 'не теплокровные':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('медлинный')
            item2 = types.KeyboardButton('быстрый')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Медлительный или быстрый хищник? /slow /fast".format(message.from_user),
                             reply_markup=markup)
        elif message.text == 'медлинный':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Тигровый питон"
            photo = open('изображения\Питон.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_python, reply_markup=markup)
        elif message.text == 'быстрый':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Веслоног деннеси"
            photo = open('изображения\Веслоног.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_dennessy, reply_markup=markup)
        elif message.text == 'приручен':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('люблю')
            item2 = types.KeyboardButton('не люблю')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Любишь живопись?".format(message.from_user), reply_markup=markup)
        elif message.text == 'не приручен':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('комфортно')
            item2 = types.KeyboardButton('не комфортно')
            item_back
            markup.add(item1, item2, item_back)
            bot.send_message(message.chat.id, "Как чувствуете себя в незнакомой компании?".format(message.from_user),
                             reply_markup=markup)
        elif message.text == 'люблю':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal ="Слон"
            photo = open('изображения\Слон.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_elephant, reply_markup=markup)
        elif message.text == 'не люблю':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Двугорбый верблюд"
            photo = open('изображения\Верблюд.jpeg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_camel, reply_markup=markup)
        elif message.text == 'комфортно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Капибара"
            photo = open('изображения\Капибара.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_capybara, reply_markup=markup)
        elif message.text == 'не комфортно':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('связаться с сотрудником')
            item2 = types.KeyboardButton('попробывать ещё раз')
            item_back
            item_share
            markup.add(item1, item2, item_back, item_share)
            name_animal = "Жираф"
            photo = open('изображения\Жираф.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, caption=name_animal+text_giraffe, reply_markup=markup)


    bot.polling(none_stop=True)

except Exception as e:
    logging.exception(e)