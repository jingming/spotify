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

### Resource Tree
* `Client` - Spotify Web API
    * `v1` - Version 1 of the Spotify Web API
        * `albums` - **/albums** endpoint
            * `list()` - List albums by ID, returns `Page[AlbumInstance]`
            * `get()` - Get the context of a single album, returns `AlbumContext`
                * `fetch()` - Get details of the album, returns `AlbumInstance`
                * `tracks` - **/albums/{album_id}/tracks** endpoint
                    * `list()` - List the tracks on the album, returns `Page[TrackInstance]` 
        * `artists` - **/artists** endpoint
            * `list()` - List artists by ID, returns `Page[ArtistInstance]`
            * `get()` - Get the context of a single artist, returns `ArtistContext`
                * `fetch()` - Get the details of the artist, returns `ArtistInstance`
                * `albums` - **/artists/{artist_id}/albums** endpoint
                    * `list()` - List albums by the artist, returns `Page[AlbumInstance]`
                * `top_tracks` - **/artists/{artist_id}/top-tracks** endpoint
                    * `list()` - List top tracks by the artist, returns `Page[TrackInstance]`
                * `related_artists` - **/artists/{artist_id}/related-artists** endpoint
                    * `list()` - List related artists, returns `Page[ArtistInstance]`
        * `audio_analysis` - **/audio-analysis** endpoint
            * `get()` - Get the context of the audio analysis for a track, returns `AudioAnalysisContext`
                * `fetch()` - Get the audio analysis details, returns `AudioAnalysisInstance`
        * `audio_features` - **/audio-features** endpoint
            * `list()` - List audio features by track ID, returns `Page[AudioFeaturesInstance]`
            * `get()` - Get the audio features context of a track, returns `AudioFeaturesContext`
                * `fetch()` - Get the audio features details of a track, returns `AudioFeaturesInstance`
        * `browse` - **/browse** endpoint
            * `featured_playlists` - **/browse/featured-playlists** endpoint
                * `fetch()` - Get the latest featured playlists, returns `FeaturedPlaylistInstance`
            * `new_releases` - **/browse/new-releases** endpoint
                * `list()` - List the new release, returns `Page[AlbumInstance]`
            * `categories` - **/browse/categories** endpoint
                * `list()` - List the categories, returns `Page[CategoryInstance]`
                * `get()` - Get the context of a category, returns `CategoryContext`
                    * `fetch()` - Get the details of a category, returns `CategoryInstance`
                    * `playlists` - **/browse/categories/{category_id}/playlists** endpoint
                        * `list()` - List the playlists that are in this category, returns `Page[PlaylistInstance]
        * `me` - **/me** endpoint
            * `fetch()` - Fetch the details of the authenticated user, returns `MeInstance`
            * `albums` - **/me/albums** endpoint
                * `list()` - List the user's saved albums, returns `Page[SavedAlbum]`
                * `save()` - Save an album, returns `bool`
                * `remove()` - Remove a soved album, returns `bool`
                * `contains()` - Checks to see if the user has saved the albums, returns `List[bool]`
            * `following` - **/me/following** endpoint
                * `list()` - List the artists followed by the user, returns `Page[ArtistInstance]`
                * `add()` - Add a follower, returns `bool`
                * `remove()` - Remove a follower, returns `bool`
                * `contains()` - Checks if the user has followed the artists, returns `List[bool]`
            * `player` - **/me/player** endpoint
                * `fetch()` - Get the player details, returns `PlayerInstance`
                * `transfer()` - Transfer playing to another device, returns `bool`
                * `play()` - Set what is being played, returns `bool`
                * `pause()` - Pause playback, returns `bool`
                * `next_()` - Skip the current track, returns `bool`
                * `previous()` - Go back a track, returns `bool`
                * `seek()` - Go to a point in the current track, returns `bool`
                * `repeat()` - Set repeat status, returns `bool`
                * `volume()` - Set the volume, returns `bool`
                * `shuffle()` - Set the shuffle status, returns `bool`
                * `currently_playing` - **/me/player/currently-playing** endpoint
                    * `fetch()` - Get the currently playing item, returns `CurrentlyPlayingInstance`
                * `devices` - **/me/player/devices** endpoint
                    * `list()` - List the devices that the user owns, returns `Page[DeviceInstance]`
                * `recently_played` - **/me/player/recently-played** endpoint
                    * `list()` - List the recently played items, returns `Page[RecentlyPlayedInstance]`
            * `playlists` - **/me/playlists** endpoint
                * `list()` - List the user created playlists, returns `Page[PlaylistInstance]`
            * `top` - **/me/top** endpoint
                * `artists` - **/me/top/artists** endpoint
                    * `list()` - List the user's top artists, returns `Page[ArtistInstance]`
                * `tracks` - **/me/top/tracks** endpoint
                    * `list()` - List the user's top tracks, returns `Page[TrackInstance]`
            * `tracks` - **/me/tracks** endpoint
                * `list()` - List the user's saved tracks, returns `Page[SavedTrack]`
                * `save()` - Save a track, returns `bool`
                * `remove()` - Remove a saved track, returns `bool`
                * `contains()` - Check to see if the user has saved tracks, returns `List[bool]`
        * `recommendations` - **/recommendations** endpoint
            * `fetch()` - Fetch recommendations, returns `RecommendationsInstance`
            * `available_genre_seeds` - **/recommendations/available-genre-seeds** endpoint
                * `fetch()` - Fetch available genre seeds, returns `List[str]`
        * `search` - **/search** endpoint
            * `get()` - Execute a serach, returns `SearchInstance`
        * `tracks` - **/tracks** endpoint
            * `list()` - List tracks by ID, returns `Page[TrackInstance]`
            * `get()` - Get a context of a track, returns `TrackContext`
                * `fetch()` - Get the details of a track, returns `TrackInstance`
        * `users` - **/users** endpoint
            * `get()` - Get a context of a user, returns `UserContext`
                * `fetch()` - Get the details of a user, returns `UserInstance`
                * `playlists` - **/users/{user_id}/playlists** endpoint
                    * `list()` - List the user's playlists, returns `Page[PlaylistInstance]`
                    * `create()` - Create a playlist, returns `PlaylistIntance`
                    * `get()` - Get a context of a playlist, returns `PlaylistContext`
                        * `fetch()` - Get the details of the playlist, returns `PlaylistInstance`
                        * `update()` - Update playlist details, returns `bool`
                        * `follow()` - Follow the playlist, returns `bool`
                        * `unfollow()` - Unfollow the playlist, returns `bool`
                        * `followers` - **/users/{user_id}/playlists/{playlist_id}/followers** endpoint
                            * `contains()` - Check if users follow this playlist, returns `List[bool]`
                        * `images` - **/users/{user_id}/playlists/{playlist_id}/images** endpoint
                            * `replace()` - Replace the playlist cover image, returns `bool`
                        * `tracks` - **/users/{user_id}/playlists/{playlist_id}/tracks** endpoint
                            * `list()` - List the tracks in the playlist, returns `Page[PlaylistTrackInstance]`
                            * `add()` - Add a track to the playlist, returns `Snapshot`
                            * `remove()` - Remove a track from the playlist, returns `Snapshot`
                            * `reorder()` - Reorder playlist tracks, returns `Snapshot`
                            * `replace()` - Replace all tracks in the playlist, returns `bool`
