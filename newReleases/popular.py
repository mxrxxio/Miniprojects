import requests

def getAlbums():
    albums = requests.get("https://rss.applemarketingtools.com/api/v2/us/music/most-played/10/albums.json")
    result = albums.json()["feed"]["results"]
    for album in range(1, len(result)+1):
        print("{count}.- Title: {title} \n \t Artist: {artist} ".format(
            count=album,
            title=result[album-1]["name"],
            artist=result[album-1]["artistName"]
        ))
    
getAlbums()
