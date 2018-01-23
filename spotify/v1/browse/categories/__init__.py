from spotify import values
from spotify.object.image import Image
from spotify.page import Page
from spotify.v1.browse.categories.playlist import PlaylistList


class CategoryInstance(object):

    def __init__(self, version, properties):
        self.version = version
        self._properties = properties
        self._context = CategoryContext(self.version)

    @property
    def href(self):
        return self._properties['href']

    @property
    def icons(self):
        return [Image.from_json(icon) for icon in self._properties['icons']]

    @property
    def id(self):
        return self._properties['id']

    @property
    def name(self):
        return self._properties['name']

    @property
    def playlists(self):
        return self._context.playlists


class CategoryContext(object):

    def __init__(self, version, id):
        self.version = version
        self.id = id

        self._playlists = None

    @property
    def playlists(self):
        if not self._playlists:
            self._playlists = PlaylistList(self.version)

        return self._playlists

    def fetch(self):
        response = self.version.request('GET', '/browse/categories/{}'.format(self.id))
        return CategoryInstance(self.version, response.json())


class CategoryList(object):

    def __init__(self, version):
        self.version = version

    def list(self, country=values.UNSET, locale=values.UNSET, limit=values.UNSET, offset=values.UNSET):
        params = values.of({
            'country': country,
            'locale': locale,
            'limit': limit,
            'offset': offset
        })
        response = self.version.request('GET', '/browse/categories', params=params)
        return CategoryPage(self.version, response.json()['categories'], 'items')


class CategoryPage(Page):

    @property
    def instance_class(self):
        return CategoryInstance
