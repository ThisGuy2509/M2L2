import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

organik = ['kulit buah', 'kertas', 'daun - daun']
anorganik = ['plastik', 'sterofoam', 'besi']

@bot.command('trash')
async def trash(ctx):
    await ctx.send('Masukan jenis sampah yang ingin diketahui: ')
    msg = await bot.wait_for("message")
    if msg.content in organik or anorganik:
        pass
    else:
        await ctx.send('Tidak ada jenis sampah yang bernama', {msg})

bot.run("token")
