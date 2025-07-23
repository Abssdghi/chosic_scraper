from chosic_scraper import *

song = search(keyword="taste")['data']['tracks']['items'][0]
name = song['name']
artist = song['artist']
id = song['id']

print(f"\nSongs similar to {name} by {artist}:\n")

tracks = get_similar_songs(id=id, limit=10)['data']['tracks']
    
for i in tracks:
    print(i['artists'][0]['name'] + " - " + i['name'])