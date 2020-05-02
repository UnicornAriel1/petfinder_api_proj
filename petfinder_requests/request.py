from requests_oauthlib import OAuth2Session
from secrets import CLIENT_ID,CLIENT_SECRET
from oauthlib.oauth2 import BackendApplicationClient

def get_animals():
    token_url = 'https://api.petfinder.com/v2/oauth2/token'
    client_id=CLIENT_ID
    client_secret=CLIENT_SECRET
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id,
            client_secret=client_secret)
    animals=oauth.get('https://api.petfinder.com/v2/animals')
    return animals.content

print(get_animals())