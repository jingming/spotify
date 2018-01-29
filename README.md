# spotify-python

[![PyPI](https://img.shields.io/pypi/v/spotify-python.svg)](https://pypi.python.org/pypi/spotify-python)

A module using the [Spotify Web API](https://developer.spotify.com/web-api/) based off of the [Twilio](https://www.github.com/twilio/twilio-python) library.

## Installation
Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python.

    pip install spotify-python
    
## Getting Started

### Credentials
Using `spotify-python` requires either Client Credentials or User Credentials.

**Client Credentials**

When using Client Credentials, you can pass them directly or use environment variables.
```python
from spotify.auth.client import Client
from spotify import Client as Spotify

SPOTIFY_CLIENT_ID = 'CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'CLIENT_SECRET'
credentials = Client(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
spotify = Spotify(credentials)
```

Alternatively, calling the `Client` constructor without these parameters will look for the
`SPOTIFY_CLIENT_ID` and `SPOTIFY_CLIENT_SECRET` in the current environment. I suggest using 
this method.
```python
from spotify.auth.client import Client
from spotify import Client as Spotify 
spotify = Spotify(Client())
```

**User Credentials**

For more advanced features, User Credentials may be required. You can find a complete description [here](https://developer.spotify.com/web-api/authorization-guide/#authorization_code_flow). To get a user token, you can use the user token utility method. If none are passed into the `user_token` method, `client_id`, `client_secret` and `redirect_uri` will be retrieved using the `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `SPOTIFY_REDIRECT_URI` environment variables.
```python
from spotify.auth.util import user_token
from spotify import Client as Spotify

scopes = ['scope-a', 'scope-b']
token = user_token(scopes)
# Acknowledge browser prompt, and paste in the redirect URI

spotify = Spotify(token)
```

### Search for a song
```python
from spotify import Client as Spotify

token = fetch_user_token()
spotify = Spotify(token)

search_result = spotify.v1.search.get('Never gonna give you up', ['track'])
for track in search_result.tracks:
    print track.name
```

### List my recently played songs
```python
from spotify import Client as Spotify

token = fetch_user_token()
spotify = Spotify(token)

recently_played = spotify.v1.me.player.recently_played.list()
for rp in recently_played:
    print rp.track.name
```