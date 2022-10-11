#Small program to search a name or text in Scryfall's database
#imports
import json 
import requests
#text to search
cardText = input('Please enter name or text to search: ')
#searching Scryfall
def search_cardName(cardText):
    try:
        base_url = f'https://api.scryfall.com/cards/search?q={cardText}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()

cardResult = search_cardName(cardText)
#Getting the card or list of cards w/ info
total = int(cardResult['total_cards'])
print('Total results found: ', total)
for x in range(total):
    name = cardResult['data'][x]['name']
    print(name)
    uri = cardResult['data'][x]['scryfall_uri']
    print(uri)
    x += 1