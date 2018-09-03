import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Bot is ready and connected to Discord")

@client.event
async def on_message(message):
    if message.content.upper().startswith('PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s>  Pong!" % (userID) )
    if message.content.upper().startswith('SAY'):
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    if message.content.upper().startswith('БОТ СКАЖИ ЧТО НИБУДЬ'):
       msg = 'Виталя ЛОХ {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.upper().startswith('БОТ СКАЖИ ЧТО-НИБУДЬ'):
       msg = 'Виталя ЛОХ {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)  
    if message.content.upper().startswith('ПРИВЕТ'):
       msg = 'Здоровеньки булы {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.upper().startswith('QQ'):
       msg = 'q  {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.upper().startswith('КУ'):
       msg = 'Дарова {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.upper().startswith('ЗДАРОВА МЫШИ'):
       msg = 'Здарова чёрт {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)  





client.run("NDg1NTAzMzQ5NTE3NzEzNDE4.Dm0jJw.RjBFbnkIQEcPE-zpP6EHTyquzoQ")




