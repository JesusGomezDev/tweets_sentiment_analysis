import snscrape.modules.twitter as sntwitter
import json

# Creating list to append tweet data to
salida = open('datos.json', 'a+')
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('suicide').get_items()):
    if i>300000:
        break
    tweetInfo = {
        'Username' : tweet.user.username,
        'Likes' : tweet.likeCount,
        'Contenido' : tweet.content,
    }

    j = json.dumps(tweetInfo)
    salida.write(j + '\n')
