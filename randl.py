import discord
import os
import json 
import requests

intents = discord.Intents.default()
intents.message_content = True
clientR = discord.Client(intents=intents)

subreddit = 'blursedimages' #or any subreddit of your choosing
count = 1 
timeframe = 'all' #Options: hour, day, week, month, year, all
listing = 'random' #Options: controversial, best, hot, new, random, rising, top

@clientR.event
async def on_ready():
    print('We have logged in as {0.user}'.format(clientR))

@clientR.event
async def on_message(message):
    if message.author == clientR.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('Hello, my name is Rand.l!\nYou can enter on of the following commands: \n$sup - say hi!\n$meme - pull a random meme from reddit\n$cardsearch - search card names or text\n$cardinfo - get the weblisting for a card or cards')

    if message.content.startswith('$sup'):
        await message.channel.send('Sup, meatbag!')

    if message.content.startswith('$meme'):
        top_post = get_reddit(subreddit,count)
        if listing != 'random':
            title = top_post['data']['children'][0]['data']['title']
            url = top_post['data']['children'][0]['data']['url']
        else:
            title = top_post[0]['data']['children'][0]['data']['title']
            url = top_post[0]['data']['children'][0]['data']['url']
        
        await message.channel.send(f'{title}\n{url}')

    if message.content.startswith('$cardsearch'):
        await message.channel.send(f"Enter a name to search below!")    

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        msg = await clientR.wait_for("message", check=check)
        cardResult = search_cardName(msg.content.lower())

        total = int(cardResult['total_cards'])
        
        for x in range(total):
            name = cardResult['data'][x]['name']
            x += 1
            await message.channel.send(f'{name}')

    if message.content.startswith('$cardinfo'):
        await message.channel.send(f"Enter a name to search below!")    

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        msg = await clientR.wait_for("message", check=check)
        cardResult = search_cardName(msg.content.lower())

        total = int(cardResult['total_cards'])
        
        for x in range(total):
            uri = cardResult['data'][x]['scryfall_uri']
            x += 1
            await message.channel.send(f'{uri}')

def get_reddit(subreddit,count):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()

def search_cardName(cardText):
    try:
        base_url = f'https://api.scryfall.com/cards/search?q={cardText}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()

clientR.run(#insert bot token here)