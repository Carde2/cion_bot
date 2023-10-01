import disnake
from disnake.ext import commands, tasks
from disnake.ext.commands import Bot
from disnake.voice_client import VoiceClient
from disnake import FFmpegPCMAudio
from disnake.utils import get
from disnake.ext import commands
import colorama
from colorama import init
import termcolor
from termcolor import colored
import time
import random
import youtube_dl
import dotenv
import nacl
import sys
import os
import asyncio
import ffmpeg

from colorama import Fore, Back, Style
from dotenv import load_dotenv


#Цвета (в консоли)
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
w = Fore.WHITE
gl = Fore.YELLOW
q = Fore.LIGHTBLUE_EX 

#Параметры для discord.py (не трогац)
intents = disnake.Intents.default()
intents.members = True
intents.typing = False

load_dotenv()

# получение токена из env файла
DISCORD_TOKEN = os.getenv("token")

youtube_dl.utils.bug_reports_message = lambda: ''


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ydl_opts)
class YTDLSource(disnake.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename



client = commands.Bot(command_prefix = "t.", case_insensitive=True, intents=intents) 


#Начало кода
os.system('cls')
os.system('title Carbon! бот от #Березы!')
client.remove_command('help')
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

@client.event 
async def on_ready():  
    print('\n\n')
    print(q+"""                          
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ᴛᴀᴜᴍᴇʟ#1663(aka @tvomel)━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        |                                   Бот запущен!...  И даже работает)                                  |
        |━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
        |         Основная инфа          ||                                  ||                                |
        |━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
        | Префикс - /, но так же можно   ||                                  ||                                |
        | Включить и второй t.           ||                                  ||                                |
        |━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
        | Цвета эмбедов только готовые!  ||                                  ||                                |
        | Красный, Зеленый, Желтый,      ||                                  ||                                |
        | Оранжевый, Пурпурный, Розовый, ||                                  ||                                |
        | Синий.                         ||                                  ||                                |
        |                                ||                                  ||                                |
        |                                ||                                  ||                                |
        |                                ||                                  ||                                |
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


#комманды с рандомом (2 штуки)
@client.slash_command(name='шар', help='задайте ему вопрос и получите ответ 0_0')
async def шар(interaction: disnake.AppCmdInter, *, ask):
    global rand
    rand = random.randint(1,4)
    if rand == 1:
      await interaction.send(':crystal_ball:: Да')
    if rand == 2:
      await interaction.send(':crystal_ball:: Нет')
    if rand == 3:
      await interaction.send(':crystal_ball:: Скорее всего да')
    if rand == 4:
      await interaction.send(':crystal_ball:: Скорее всего нет')
@шар.error
async def шар_error(interaction: disnake.AppCmdInter, error):
	if isinstance(error, commands.MissingRequiredArgument):
		msg = await interaction.reply('**Error**:Используйте: .шар "вопрос" Для того чтобы задать вопрос!')
		await interaction.message.delete()
		await asyncio.sleep(3)
		await msg.delete()

@client.slash_command()
async def поиск(interaction: disnake.AppCmdInter, member: disnake.Member = None):
    if not member:
     await interaction.send('Пожалуйста укажите участника!')
    if member.id == 890139054228783124:
      await interaction.send(f'<@!{member.id}> Красавчик')
    else:
        global rand
        rand = random.randint(1,1)
        if rand == 1:
            await interaction.send(f'**Выполняю поиск по запросу "Porn with <@!{member.id}>"...**')
            await interaction.send(f'**Найденные результаты:** *<@!{member.id}> дрочит негру, <@!{member.id}> кончили на ебало, <@!{member.id}> берет в себя несколько хуев.*')
        if rand == 2:
            await interaction.send(f'<@!{member.id}> текст')
        if rand == 3:
            await interaction.send(f'<@!{member.id}> текст')
        if rand == 4:
            await interaction.send(f'<@!{member.id}> текст')
        if rand == 5:
            await interaction.send(f'<@!{member.id}> текст')
        if rand == 6:
            await interaction.send(f'<@!{member.id}> текст')
        if rand == 7:
            await interaction.send(f'<@!{member.id}> текст')
        if rand == 8:
            await interaction.send(f'<@!{member.id}> текст')

@поиск.error
async def info_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await print("")

@client.slash_command(name='попыт', help='    выводит попыт')
async def попыт(interaction: disnake.AppCmdInter):
	await interaction.send("""||:red_square:||||:red_square:||||:red_square:||||:red_square:||||:red_square:||\n||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||\n||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||\n||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||\n||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||""")



#работает
@client.slash_command(name='стоп', help='останавливает музыку')
async def стоп(interaction: disnake.AppCmdInter):
    voice_client = interaction.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await interaction.send("Список проигрывания пуст")



#@client.slash_command(name='играть')
#async def играть(ctx,url):
#    try:
#        server = ctx.message.guild
#        voice_channel = server.voice_client
#
#        async with ctx.typing():
#            filename = await YTDLSource.from_url(url, loop=client.loop)
#            voice_channel.play(discord.FFmpegPCMAudio(executable='C:/Users/User/Desktop/самописка/бот дс/ffmpeg/bin/ffmpeg.exe', source=filename))
#        await ctx.send('**ИГРАЕТ**: {}'.format(filename))
#    except:
#        await ctx.send("Ошибка.")

# @client.slash_command(name='играть')
# async def играть(interaction: disnake.AppCmdInter,url):
#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        ydl.download({url})  
#    try:
#        server = interaction.guild
#        voice_channel = server.voice_client
#        async with interaction():
#            filename = await YTDLSource.from_url(url, loop=client.loop)
#            voice_channel.play(disnake.FFmpegPCMAudio(executable='C:/Users/User/Desktop/самописка/бот дс/ffmpeg/bin/ffmpeg.exe', source=filename))
#        await interaction.send('**ИГРАЕТ**: {}'.format(filename))
#    except:
#        await interaction.send("Ошибка, скорее всего из-за того, что нет плейлистов (уже играет музыка, но вы ищите ещё)....")

@client.slash_command(name='играть')
async def играть(interaction: disnake.ApplicationCommandInteraction, url):
        server = interaction.guild
        voice_channel = server.voice_client
        await interaction.response.defer()
        filename = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(disnake.FFmpegPCMAudio(executable='C:/Users/User/Desktop/самописка/бот дс/ffmpeg/bin/ffmpeg.exe', source=filename))
        await interaction.edit_original_message(content='ИГРАЕТ: {}'.format(filename))

@client.slash_command(name='играть1')
async def играть(interaction: disnake.AppCmdInter):
        server = interaction.guild
        voice_channel = server.voice_client
        await interaction.response.defer()
        voice_channel.play(disnake.FFmpegPCMAudio(executable='C:/Users/User/Desktop/самописка/бот дс/ffmpeg/bin/ffmpeg.exe', source='♪B-Complex-BeautifulLies.mp3'))






@client.slash_command(name='зайти', help='бот заходит в войс (пока бесполезно)')
async def зайти(interaction: disnake.AppCmdInter):
    if not interaction.author.voice:
        await interaction.send("{} бот не подключен".format(interaction.author.name))
        return
    else:
        channel = interaction.author.voice.channel
    await channel.connect()
    await interaction.send("бот зашел.")

#работает
@client.slash_command(name='выйти', help='бот покидает войс')
async def выйти(interaction: disnake.AppCmdInter):
    voice_client = interaction.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await interaction.send("Готово.")
    else:
        await interaction.send("бот вышел.")

#от ембеды
@client.slash_command(name='ембед', help='вызывает красивый текст')
async def ембед(interaction: disnake.AppCmdInter, color, title, name, *, value):
    if color == 'Оранжевый':
        embed = disnake.Embed(color = 0xff9900, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)
    if color == 'Красный':
        embed = disnake.Embed(color = 0x992d22, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)
    if color == 'Зеленый':
        embed = disnake.Embed(color = 0x2ecc71, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)
    if color == 'Желтый':
        embed = disnake.Embed(color = 0xf1c40f, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)
    if color == 'Пурпурный':
        embed = disnake.Embed(color = 0x9b59b6, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)
    if color == 'Розовый':
        embed = disnake.Embed(color = 0xe91e63, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)
    if color == 'Синий':
        embed = disnake.Embed(color = 0x3498db, title= f'{title}')
        embed.add_field(name=f"{name}", value=f"{value}", inline=False)
        await interaction.send(embed=embed)

#ЭТО ВСЕГДА ВНИЗУ!!!!
@client.slash_command(name='помощь', help='help')
async def помощь(interaction: disnake.AppCmdInter):
    embed = disnake.Embed(color = 0x00fdff, title= 'Помощь')
    embed.add_field(name="Из-за почти полной переделки бота могут быть ошибки", value="Бот от клана Береза!\nСоздан благодоря Psychoblad3s\n\nКомманды:\n*/помощь - этот текст. (есть вариация /хелп {название комманды})\n/попыт - выводит попыт 0_0\n/шар <сообщение> - отвечает на вопросы (да, нет, скорее всего да, скорее всего нет)\n/ping - хы\n/тест - временная комманда (позже удалю)\n/стоп - останавливает музыку -_-\n/играть - играет музыку :3\n/выйти - выходит из войса\n/зайти - заходит в войс в котором вы\n/ембед (цвет англ) (заголовок) (название) (текст)\n/поиск - троллоло комманда! работает правильно только при пинге участника!!!!*\n\nОфф сервер бота: https://discord.gg/WkwVN6mRtw", inline=False)
    await interaction.send(embed=embed)

#Запуск бота, проверка правильно ли введен токен
try:
    client.run(DISCORD_TOKEN)
except:
    print('')
    print(r+'ERROR: Неправильный токен! Возможно с файлом .env что то не так!')
    time.sleep(10)
