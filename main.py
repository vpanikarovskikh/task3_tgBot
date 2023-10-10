import telebot
from telebot import types
import psycopg2
from config import host, user, password, db_name

bot = telebot.TeleBot('6567034735:AAE6SgDa6E9l64w1O7WjtausXERIbOYqK9g')


def select_info(connection, id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT document_link, description FROM documents WHERE document_id = {id}")

        connection.commit()
        return cursor.fetchone()

try:
    #подключение к бд
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        bot.send_message(message.chat.id, 'Привет! Я помогу тебе найти необходимые документы и информацию! \nДля этого просто введи тему, а я отправлю тебе все, что нужно', reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def memorize(message):
        if message.text.lower() == 'программа 1':
            doc_link = select_info(connection, 1)
            bot.send_message(message.chat.id, f'Вот ссылка на нужный вам документ: {doc_link[0]}\n\nОписание:\n{doc_link[1]}')
        elif message.text.lower() == 'программа 2':
            doc_link = select_info(connection, 2)
            bot.send_message(message.chat.id, f'Вот ссылка на нужный вам документ: {doc_link[0]}\n\nОписание:\n{doc_link[1]}')
        elif message.text.lower() == 'программа 3':
            doc_link = select_info(connection, 3)
            bot.send_message(message.chat.id, f'Вот ссылка на нужный вам документ: {doc_link[0]}\n\nОписание:\n{doc_link[1]}')
        else:
            bot.send_message(message.chat.id, 'Еще не имею информации по этой теме :(\nПопробуй другую :]')

    bot.polling(none_stop=True)


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")




    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE documents2 (
    #             document_id smallint NOT NULL,
    #             document_link text NOT NULL,
    #             description text NOT NULL
    #         );
    #
    #         INSERT INTO documents2 VALUES (1, 'https://www.utmn.ru/upload/medialibrary/ce2/Polozhenie-ob-OP-VO-v-TyumGU-2022.pdf', 'Положение об образовательной программе высшего образования в ТюмГУ (от 26.09.2022)');
    #         INSERT INTO documents2 VALUES (1, 'https://www.utmn.ru/upload/medialibrary/302/419_1_1-Prikaz-Ob-utverzhdenii-maketov-strukturnykh-komponentov-OP-VO.PDF', 'Макеты структурных компонентов образовательных программ высшего образования ');
    #         INSERT INTO documents2 VALUES (1, 'https://www.utmn.ru/upload/medialibrary/a0e/Prikaz-ob-utverzhdenii-maketov-strukturnykh-komponentov-OP-VO-ot-27.09.2021-_-616_1.PDF', 'Макеты структурных компонентов образовательных программ высшего образования');
    #         INSERT INTO documents2 VALUES (1, 'https://www.utmn.ru/upload/medialibrary/56c/Poryadok-organizatsii-i-osushchestvleniya-OD-po-OP-SPO-N-762.pdf', 'Приказ Минпросвещения России от 24.08.2022 № 762');
    #         INSERT INTO documents2 VALUES (1, 'https://www.utmn.ru/upload/medialibrary/0e3/O-prakticheskoy-podgotovke-obuchayushchikhsya.pdf', 'Приказ Минобрнауки России от 05.08.2020 № 885');
    #         """
    #     )
    #     connection.commit()
    #     print("Таблица создана: ")