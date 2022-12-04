import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater=Updater(token='5907418022:AAHjBYxmkuG97wKp1zdWsUdaJ7ytKcskAaw',use_context=True)
dispatcher=updater.dispatcher
def Hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Hello Hello')
hello_handler=CommandHandler('Hello',Hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()
def Summary(update,context):
    response=requests.get('https://api.covid19api.com/summary')
    if response.status_code==200:
        data=response.json()
        date=data['Date'][:10]
        answer=f"covid19summary(as of {date}):\n"
        for attribute,value in data['Global'].items():
            if attribute not in['NewConfirmed','NewDeaths','NewRecovered']:
                answer+='total'+attribute[5::].lower()+":"+str(value)+"\n"   
        context.bot.send_message(chat_id=update.effective_chat.id,text=answer)
    else:
              
        context.bot.send_message(chat_id=update.effective_chat.id,text='Sorry something went wrong')
summary_handler=CommandHandler('summary',Summary)
dispatcher.add_handler(summary_handler)