import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import aiohttp
import time
import json
import requests
from discord import Game
BOT_PREFIX = ("?", "!")
TOKEN = "NDg1NTAzMzQ5NTE3NzEzNDE4.DnAX2A.yTZDg_4mhX31DAJthk_Mt0YHCu4"

Client = discord.Client()
client = commands.Bot(command_prefix = "!")



@client.event
async def on_ready():
    print("Bot is ready and connected to Discord")
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="очке Антона"))
    print("Logged in as " + client.user.name)    

@client.event
async def on_message(message):
    if message.content.upper().startswith('PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s>  Pong!" % (userID) )
    if message.content.upper().startswith('SAY'):
        args = message.content.split(" ")
        #args[0] = SAY
        #args[1] = Hey
        #args[2] = There
        #args[1] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        await client.delete_message(message)

    if  message.content.upper().startswith('БОТ СКАЖИ ЧТО НИБУДЬ'):
        await client.send_message(message.channel, "Виталя ЛОХ")
    if  message.content.upper().startswith('БОТ СКАЖИ ЧТО-НИБУДЬ'):
        await client.send_message(message.channel, "Виталя ЛОХ" )    
    if message.content.upper().startswith('ПРИВЕТ'):
        await client.send_message(message.channel, "Здоровеньки булы")
    if message.content.upper().startswith('QQ'):
        await client.send_message(message.channel, "q")
    if message.content.upper().startswith('КУ'):
        await client.send_message(message.channel, "Дарова")
    if message.content.upper().startswith('ЗДАРОВА МЫШИ'):
        await client.send_message(message.channel, "Здарова чёрт")
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
     
    
    
        
            




client.run("NDg1NTAzMzQ5NTE3NzEzNDE4.Dm0jJw.RjBFbnkIQEcPE-zpP6EHTyquzoQ")
