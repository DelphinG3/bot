import random
import asyncio
import requests
from discord import Game
from discord.ext.commands import Bot
import aiohttp
BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

Client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready and connected to Discord")



@client.command(pass_context=True)
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.send_message(ctx.message.channel, "Bitcoin price is: $" + value)
@client.command()
async def eth():
    url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("Ethereum price is: $" + value)
    await client.say("Ethereums rank is: " + rank)
    await client.say("Ethereums total supply is: " + supply)
    await client.say("Ethereums percent change in the past hour is: " +change1)
    await client.say("Ethereums percent change in the past 24 hours is:" + change24)
    await client.say("Ethereums percent change in the past 7 days is: " + change72)
    await client.say("Ethereums 24 hour volume is: " + vol24)
    await client.say("Ethereums symbol is: " + sym)
@client.command()
async def ripple():
    url = 'https://api.coinmarketcap.com/v1/ticker/ripple/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    rank = response.json()[0]["rank"]
    supply = response.json()[0]["total_supply"]
    change1 = response.json()[0]["percent_change_1h"]
    change24 = response.json()[0]["percent_change_24h"]
    change72 = response.json()[0]["percent_change_7d"]
    vol24 = response.json()[0]["24h_volume_usd"]
    sym = response.json()[0]["symbol"]
    await client.say("Ripples price is: $" + value)
    await client.say("Ripples rank is: " + rank)
    await client.say("Ripples total supply is: " + supply)
    await client.say("Ripples percent change in the past hour is: " +change1)
    await client.say("Ripples percent change in the past 24 hours is:" + change24)
    await client.say("Ripples percent change in the past 7 days is:" + change72)
    await client.say("Ripples 24 hour volume is:" + vol24)
    await client.say("Ripples symbol is: " + sym)
@client.command()
async def litecoin():
    url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("Litecoin price is: $" + value)
@client.command()
async def neo():
    url = 'https://api.coinmarketcap.com/v1/ticker/neo/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("NEO price is: $" + value)
@client.command()
async def eos():
    url = 'https://api.coinmarketcap.com/v1/ticker/eos/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("EOS price is: $" + value)
@client.command()
async def dash():
    url = 'https://api.coinmarketcap.com/v1/ticker/dash/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("DASH price is: $" + value)
@client.command()
async def zcash():
    url = 'https://api.coinmarketcap.com/v1/ticker/zcash/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("Zcash price is: $" + value)
@client.command()
async def metal():
    url = 'https://api.coinmarketcap.com/v1/ticker/metal/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("METAL coin price is: $" + value)
@client.command()
async def trump():
    url = 'https://api.coinmarketcap.com/v1/ticker/trumpcoin/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("Trump Coin price is: $" + value)
@client.command()
async def gas():
    url = 'https://api.coinmarketcap.com/v1/ticker/gas/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("GAS coin price is: $" + value)
@client.command()
async def gts():
    url = 'https://api.coinmarketcap.com/v1/ticker/game/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("GTS coin price is: $" + value)
@client.command()
async def salus():
    url = 'https://api.coinmarketcap.com/v1/ticker/salus/'
    response = requests.get(url)
    value = response.json()[0]["price_usd"]
    await client.say("Salus coin price is: $" + value)


















client.run("NDg1NTAzMzQ5NTE3NzEzNDE4.DnBBLg.u2VaOUPZEqJ3Hb11-Ske6UDqYvo")
