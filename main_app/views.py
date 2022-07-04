from urllib import response
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from pkg_resources import require
from .models import MyProject
#from rest_framework import response
#from rest_framework.response import Response
from .forms import PostForm
from telegram import Bot
import random
#import redis
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

#r = redis.StrictRedis()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


class SenderMessages:

    TELEGRAM_TOKEN = TELEGRAM_TOKEN
    CHAT_ID = CHAT_ID
    bot = Bot(token=TELEGRAM_TOKEN)

    def sended_message(message):
        send = SenderMessages
        send.bot.send_message(chat_id=send.CHAT_ID, text=message)

def generator_id():
    data = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    chat_key = ''
    for i in range(100):
        x = int(random.randint(0, 35))
        chat_key += str(data[x])
    print(chat_key)
    return chat_key

def index(request, gera_dev_cook=None):
    SenderMessages.sended_message('кто-то открыл страницу')
    form = PostForm()
    if request.method == "POST":
    #    if 'gera_dev_cook' not in request.session:
    #        request.session['gera_dev_cook'] = generator_id()
    #else:
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            SenderMessages.sended_message(text)
            return render(request, 'index.html', {'ok':ok})

    ok = False
    return render(request, "index.html", {'form': form, 'ok': ok})
