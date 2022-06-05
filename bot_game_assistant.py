#@GameAssistant_Bot
import logging
import random
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = ''
# список названий кнопок главного экрана бота
initial_keyboard = [['/dice', '/timer']]
# список названий кнопок выбора кубиков
dice_keyboard = [['1 кубик', '2 кубика'],
                 ['кубик на 20', 'назад']]
# список названий кнопок таймера
time_keyboard = [['30 секунд','1 минута'],
                  ['5 минут', 'назад']]
# название кнопки работы таймера
close_keyboard = [['/close']]
# разметки кнопок
markup_start = ReplyKeyboardMarkup(initial_keyboard, one_time_keyboard=False)
markup_dice = ReplyKeyboardMarkup(dice_keyboard, one_time_keyboard=False)
markup_timer = ReplyKeyboardMarkup(time_keyboard, one_time_keyboard=False)
markup_close = ReplyKeyboardMarkup(close_keyboard, one_time_keyboard=False)

# команда начала работы бота
def start(update, context):
    update.message.reply_text('Сделайте выбор', reply_markup= markup_start)

# команда назад
def back(update, context):
    update.message.reply_text('Сделайте выбор', reply_markup= markup_start)
# команда отображение меню выбора кубиков
def dice(update, context):
    update.message.reply_text('Кинем кости?!', reply_markup=markup_dice)
# команда броска первого кубика
def dice_1(update, context):
    update.message.reply_text(f'Выпало число {random.randint(1,6)}.')
# клманда броска двух кубиков
def dice_2(update,context):
    update.message.reply_text(f'Выпали числа {random.randint(1,6)} и {random.randint(1,6)}.')
# команда броска 20-гранного кубика
def big_dice(update, context):
    update.message.reply_text(f'Выпало число {random.randint(1,20)}.')
# команда меню выбора таймеров
def timer(update, context):
    update.message.reply_text('Сколько засечём?', reply_markup=markup_timer)
# функция мониторинга задач
def monitor(update, context):
    choice = update.message.text  # текст нажатой кнопки, не имеющей команды
    if choice == dice_keyboard[0][0]:  # если выбран бросок 1 кубика
        dice_1 (update, context)
    if choice == dice_keyboard[0][1]:  # если выбран бросок 2 кубиков
        dice_2(update, context)
    if choice == dice_keyboard[1][0]:  # если выбран бросок 20-гранного кубика
        big_dice(update, context)
    if choice == dice_keyboard[1][1]:  # если выбрана команда назад
        back(update, context)
    # если выбрана команда установки таймера
    if choice in [time_keyboard[0][0], time_keyboard[0][1], time_keyboard[1][0]]:
        time = int(choice.split()[0])  # принимаем первое число за время
        if time == 30:  # если время равно 30 секундам
            timer_set(update, context, time)  # то устанавливаем таймер
        else:  # иначе переводим минуты в секунды и
            timer_set(update, context, time * 60)  # запускаем таймер

def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

def close(update, context):
    """Отменяет таймер, если пользователь передумал"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    timer(update,context)

# функция оповещения о завершении работы таймера
def timer_end(update, context, text_time):
    job = context.job
    context.bot.send_message(job.context, text=f'{text_time} истекло')
    timer(update, context)

# функция установки таймера
def timer_set(update, context, time):
    text_time = update.message.text  # текст команды
    chat_id = update.message.chat_id
    #job_removed = remove_job_if_exists(str(chat_id), context)
    # устанавливает задачу работы таймера на время time
    context.job_queue.run_once(lambda x=context:timer_end(update, x, text_time),
                               time, context=chat_id, name=str(chat_id))
    # оповещаем, что таймер запущен
    update.message.reply_text(f'засёк {text_time}', reply_markup=markup_close)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    monitor_handler = MessageHandler(Filters.text & ~Filters.command, monitor,
                                  pass_job_queue=True,
                                  pass_chat_data=True)
    dp.add_handler(monitor_handler)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('dice', dice))
    dp.add_handler(CommandHandler('timer', timer))
    dp.add_handler(CommandHandler('close', close, pass_chat_data=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()