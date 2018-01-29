import webbrowser
from spotify.auth.user import authorize_url, User
from urlparse import urlparse, parse_qs


def parse_code(url):
    """
    Parse the code parameter from the a URL

    :param str url: URL to parse
    :return: code query parameter
    :rtype: str
    """
    result = urlparse(url)
    query = parse_qs(result.query)
    return query['code']


def user_token(scopes, client_id=None, client_secret=None, redirect_uri=None):
    """
    Generate a user access token

    :param List[str] scopes: Scopes to get
    :param str client_id: Spotify Client ID
    :param str client_secret: Spotify Client secret
    :param str redirect_uri: Spotify redirect URI
    :return: Generated access token
    :rtype: User
    """
    webbrowser.open_new(authorize_url(client_id=client_id, redirect_uri=redirect_uri, scopes=scopes))
    code = parse_code(raw_input('Enter the URL that you were redirected to: '))
    return User(code, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
