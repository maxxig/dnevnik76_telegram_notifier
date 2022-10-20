import telegram
#from telegram.ext import Updater
#from telegram.ext import CommandHandler
#from telegram.ext import MessageHandler, Filters
#TOKEN = ''
#updater = Updater(token=TOKEN)
#dispatcher = updater.dispatcher

def send(msg, chat_id, token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)

# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id,text="привет я бот")

# def echo (update, context):
#     logger.info('chat_id=' + str(update.effective_chat.id) +
#                 ', from_user_id='+ str(update.message.from_user.id) + ', first_name=' + update.message.from_user.first_name
#                 + ', full_name=' + update.message.from_user.full_name + ', name=' + update.message.from_user.name
#                 + ', message: ' + update.message.text
#                 )
#     # update.message.from_user.id first_name full_name name
#     # if(update.message.from_user.id !=434381141):
#     #     text =''
#     #     if(len(update.message.text)<5 or len(update.message.text)>25):
#     #         text = 'Не понятнааа'
#     #     else: text = 'Ты говоришь: '+update.message.text + '. Да я говорю: '+update.message.text +'. Дак рассказать тебе сказку про белого бычка?'
#     #     context.bot.send_message(chat_id=update.effective_chat.id,text=text)
#start_handler = CommandHandler('start2',start)
#echo_handker = MessageHandler(Filters.text & (~Filters.command), echo)

#dispatcher.add_handler(start_handler)
#dispatcher.add_handler(echo_handker)
#updater.start_polling()