#Импорты
import disnake
import dotenv
import os
import time
from disnake.ext import commands
from dotenv import load_dotenv


#Бот (настрoйка)
intents = disnake.Intents.default()
intents.members = True
intents.typing = False
client = commands.Bot(command_prefix=None, case_insensitive=True, intents=intents) 

#Остальная настройка






#Комманды





#Токен
load_dotenv()
TOKEN = os.getenv("discord_token")

#Старт
try:
    client.run(TOKEN)
except:
    print("ERROR: Неправильный токен! Возможно с файлом .env что то не так!")
    time.sleep(10)