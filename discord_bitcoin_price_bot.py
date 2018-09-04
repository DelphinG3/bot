
import requests


discord_webhook_url = 'https://discordapp.com/api/webhooks/486535419463467029/vCdWuRC-u03ujGyj4VmWfP0gfNPE1zr6v10wOSjnlHA5V6N5rZriQj_BU4TE4deepIxj'


bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
data = requests.get(bitcoin_price_url).json()
price_in_usd = data['bpi']['USD']['rate']


data = {
    "content": "Bitcoin price is currently at $" + price_in_usd + " USD"
}
requests.post(discord_webhook_url, data=data)
