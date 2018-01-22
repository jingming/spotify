

class Scope(object):
    """
    User scopes

    For more information see: https://developer.spotify.com/web-api/using-scopes/
    """
    PLAYLIST_READ_PRIVATE = 'playlist-read-private'
    PLAYLIST_READ_COLLABORATIVE = 'playlist-read-collaborative'
    PLAYLIST_MODIFY_PUBLIC = 'playlist-modify-public'
    PLAYLIST_MODIFY_PRIVATE = 'playlist-modify-private'

    STREAMING = 'streaming'

    UGC_IMAGE_UPLOAD = 'ugc-image-upload'

    USER_FOLLOW_MODIFY = 'user-follow-modify'
    USER_FOLLOW_READ = 'user-follow-read'

    USER_LIBRARY_READ = 'user-library-read'
    USER_LIBRARY_MODIFY = 'user-library-modify'

    USER_READ_PRIVATE = 'user-read-private'
    USER_READ_BIRTHDATE = 'user-read-birthdate'
    USER_READ_EMAIL = 'user-read-email'
    USER_READ_PLAYBACK_STATE = 'user-read-playback-state'
    USER_MODIFY_PLAYBACK_STATE = 'user-modify-playback-state'
    USER_READ_CURRENTLY_PLAYING = 'user-read-currently-playing'
    USER_READ_RECENTLY_PLAYED = 'user-read-recently-played'

    USER_TOP_READ = 'user-top-read'
