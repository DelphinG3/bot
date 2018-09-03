import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import json
from discord import Game

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
        
@client.event
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
    raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
    await client.say("Цена биткоина: $" + response['bpi']['USD']['rate'])    




client.run("NDg1NTAzMzQ5NTE3NzEzNDE4.Dm0jJw.RjBFbnkIQEcPE-zpP6EHTyquzoQ")
