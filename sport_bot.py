from telegram import Update
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler


group_1 = 'Грудь'
group_2 = 'Бицепс'
group_3 = 'Трицепс'
group_4 = 'Спина'
group_5 = 'Плечи'
group_6 = 'Ноги'


def button_help_handler_1(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Жим лежа 10x3\n'
             'Горизонтальная тяга в кроссовере 3x10\n'
             'Жим лежа под углом 3x10\n'
             'Вертикальная тяга 3x10\n'
             'Отжимания на брусьях 3х10\n'
             'Вертикальная тяга сверху вниз 3x10\n',


    )


def button_help_handler_2(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Подъем штанги 3х12\n'
            'Скамья Скотта 3х12\n'
            'Молотки 3х12\n'
            'Подъем гантелей сидя 3х12\n',
    )


def button_help_handler_3(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Брусья 3x10\n'
            'Обратные отжимания3x15\n'
            'ПодЬем гантелей сидя из-за спина3x15\n',
    )


def button_help_handler_4(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Тяга блока к груди 3х12'
            'Гиперэкстензия 3х15\n'
            'Тяга блока к животу 4х15\n'
            'Тренажёр 3х15\n'
            'Подтягивания Макс Макс\n',
    )


def button_help_handler_5(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Жим гантелей на плечи 4х12\n'
            'Обратная бабочка 4х15\n'
            'Подъем гантелей в бок 3х15\n'
            'Армейский жим 3х12\n',
    )


def button_help_handler_6(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Приседания 15х3\n'
            'Жим ногами 15х3\n'
            'Икроножные 15х3\n'
            'Бедро 15х3\n',
    )

def button_help_handler_7(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='ГЭЙ'
    )


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == group_1 or text == 'грудь':
        return button_help_handler_1(update=update, context=context)

    elif text == group_2 or text == 'бицепс':
        return button_help_handler_2(update=update, context=context)

    elif text == group_3 or text == 'трицепс':
        return button_help_handler_3(update=update, context=context)

    elif text == group_4 or text == 'спина':
        return button_help_handler_4(update=update, context=context)

    elif text == group_5 or text == 'плечи':
        return button_help_handler_5(update=update, context=context)

    elif text == group_6 or text == 'ноги':
        return button_help_handler_6(update=update, context=context)

    elif text == 'Данил кто' or text == 'Данил who':
        return button_help_handler_7(update=update, context=context)


def main():
    print('Start')

    updater = Updater(
        token='864511076:AAH2EFAYj8XwhSU3i84GfvPJDyosKzwVfQU',
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()