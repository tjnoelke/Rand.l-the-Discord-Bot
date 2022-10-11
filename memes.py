#Small program to pull a random meme (or specific depending on the choices below) from r/blursedimages
#imports
import json 
import requests
#settings 
subreddit = 'blursedimages'
count = 1
timeframe = 'day' #hour, day, week, month, year, all
listing = 'top' # controversial, best, hot, new, random, rising, top
#pulling the API 
def get_reddit(subreddit,count):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?count={count}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 
top_post = get_reddit(subreddit,count)

#pulling specific data 
if listing != 'random':
    title = top_post['data']['children'][0]['data']['title']
    url = top_post['data']['children'][0]['data']['url']
else:
    title = top_post[0]['data']['children'][0]['data']['title']
    url = top_post[0]['data']['children'][0]['data']['url']
 
#printing the results 
print(f'{title}\n{url}')