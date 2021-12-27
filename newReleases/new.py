from dotenv import load_dotenv
import os
import pprint
import requests

load_dotenv()

def auth():
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    auth_response_data = auth_response.json() # request to JSON
    return auth_response_data['access_token'] # save the access token


headers = {
    'Authorization': 'Bearer {token}'.format(token=auth())
}


BASE_URL = 'https://api.spotify.com/v1/'
NEW_RELEASES = "https://api.spotify.com/v1/browse/new-releases"

def new_releases():
    r = requests.get(NEW_RELEASES,
                headers=headers)
    return r.json()

data = new_releases()
#print(data['albums']['items'])
def getNew():
    for album in range(1, len(data['albums']['items'])+1):
        print("{count}.- Title: {title} \n \t Artist: {artist}".format(
            count=album,
            title=data['albums']['items'][album-1]['name'],
            artist=data['albums']['items'][album-1]['artists'][0]['name']
    ))
