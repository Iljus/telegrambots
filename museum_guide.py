# @museum_guide_bot
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# за основу взяты залы Эрмитажа
TOKEN = ""

def start(update, context):
    markup_key = ReplyKeyboardMarkup([['/vhod']], one_time_keyboard=False)
    update.message.reply_text('Виртуальный музей!', reply_markup=markup_key)

def vhod(update, context):
    markup_key = ReplyKeyboardMarkup([['/zal_1']], one_time_keyboard=False)
    update.message.reply_text('Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!',
                              reply_markup=markup_key)

def zal_1(update, context):
    markup_key = ReplyKeyboardMarkup([['/zal_2', '/vihod']], one_time_keyboard=False)
    update.message.reply_text('Павильонный зал\nВ этом помещении вы не найдете'
                              ' точеных статуй и полотен, однако его интерьер '
                              'впечатляет своей роскошью и изяществом. '
                              'Создал такую красоту архитектор Андрей Штакеншнейдер '
                              'в 19 веке. В оформлении пространства сочетаются античная, '
                              'мавританская и ренессансная стилистики. Белоснежные колонны, '
                              'ажурные позолоченные решетки, арки, огромные хрустальные '
                              'люстры создают здесь атмосферу восточного дворца.',
                              reply_markup=markup_key)


def zal_2(update, context):
    markup_key = ReplyKeyboardMarkup([['/zal_3']], one_time_keyboard=False)
    update.message.reply_text('Малахитовая гостиная\nЕще одно творение Александра Брюллова, '
                              'созданное в 1837 году на месте Яшмовой гостиной. Благодаря '
                              'оформлению из драгоценных камней это небольшое помещение признано '
                              'самым ценным в корпусе. Основные акценты в оформлении принадлежат малахитовым'
                              ' колоннам, пилястрам и двум каминам. Из камня также выполнены многие '
                              'другие экспонаты: столешницы, тумбочки, вазы. Стены отделаны мрамором, потолок'
                              ' украшен позолоченным узором, который копирует рисунок на полу. Контраста'
                              ' и торжественности залу придают малиновые шторы, а также ткань на стульях.'
                              ' Среди экспонатов самыми старинными считаются высокий вазон из малахита и мебель'
                              ', сохранившаяся после пожара.',
                              reply_markup=markup_key)

def zal_3(update, context):
    markup_key = ReplyKeyboardMarkup([['/zal_1','/zal_4']], one_time_keyboard=False)
    update.message.reply_text('Концертный зал\nЗа историю существования он был трижды '
                              'изменен и свой окончательный вид приобрел в 1837 году. '
                              'В богатстве скульптурной отделки этому залу нет равных. '
                              'Вторые ярусы его стен украшены статуями богинь и античных '
                              'муз. Скульптурные композиции плавно соединяются с потолком,'
                              ' что придает пространству дополнительного объема. Кроме '
                              'роскошного оформления здесь можно увидеть богатую коллекцию '
                              'русского серебра 17 – 20 века. Самым ценным экспонатом считается '
                              'серебряная рака Александра Невского, изготовленная из 1,5 '
                              'тонн благородного металла.',
                              reply_markup=markup_key)

def zal_4(update, context):
    markup_key = ReplyKeyboardMarkup([['/zal_1']], one_time_keyboard=False)
    update.message.reply_text('Белый зал\nРасполагается в юго-западной части Зимнего дворца. '
                              'Холл был создан из трех гостиных и должен был стать местом '
                              'празднования свадьбы Александра Второго. Своим оформлением '
                              'зал ничуть не расходится с названием. Его белые стены задекорированы '
                              'колоннами, которые венчают скульптуры женских фигур. Они символизируют'
                              ' различные виды искусства. Ампирную стилистику зала подчеркивают барельефные'
                              ' фигуры, изображающие богов Олимпа, а также изящные арочные проемы.'
                              'Сегодня в Белом зале выставлена экспозиция французской живописи 18 века, коллекция '
                              'фарфора и предметы мебели в стиле классицизма.',
                              reply_markup=markup_key)

def vihod(update, context):
    markup_key = ReplyKeyboardMarkup([['/vhod']], one_time_keyboard=False)
    update.message.reply_text('Не забудьте забрать свою одежду. Будем рады вас видеть снова!',
                              reply_markup= ReplyKeyboardRemove())#markup_key)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('vhod', vhod))
    dp.add_handler(CommandHandler('zal_1', zal_1))
    dp.add_handler(CommandHandler('zal_2', zal_2))
    dp.add_handler(CommandHandler('zal_3', zal_3))
    dp.add_handler(CommandHandler('zal_4', zal_4))
    dp.add_handler(CommandHandler('vihod', vihod))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()