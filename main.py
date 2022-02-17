import json
import requests
import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def hello(ctx):
    author = ctx.message.author

    await ctx.send(f'Hello, {author.mention}!')


@bot.command()
async def yo(ctx):
    author = ctx.message.author

    await ctx.send(f'I`m okay, {author.mention}!, xd')


@bot.command()
async def panda(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')  # запрос url
    json_data = json.loads(response.text)                            # extract json file

    embed = discord.Embed(color = 0xff9900, title='Рандомная Панда') #embed
    embed.set_image(url = json_data['link'])                         #load img
    await ctx.send(embed = embed)                                    #send embed


bot.run(settings['token'])
