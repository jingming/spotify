from spotify import values
from spotify.object.image import Image
from spotify.page import Page
from spotify.resource import Instance, Resource
from spotify.v1.browse.categories.playlist import PlaylistList


class CategoryInstance(Instance):

    def __init__(self, version, properties):
        super(CategoryInstance, self).__init__(version, properties)
        self._context = CategoryContext(self.version, self.id)

    @property
    def href(self):
        return self.property('href')

    @property
    def icons(self):
        return [Image.from_json(icon) for icon in self.property('icons')]

    @property
    def id(self):
        return self.property('id')

    @property
    def name(self):
        return self.property('name')

    @property
    def playlists(self):
        return self._context.playlists


class CategoryContext(Resource):

    def __init__(self, version, id):
        super(CategoryContext, self).__init__(version)
        self.id = id

        self._playlists = None

    @property
    def playlists(self):
        if not self._playlists:
            self._playlists = PlaylistList(self.version, self.id)

        return self._playlists

    def fetch(self):
        response = self.version.request('GET', '/browse/categories/{}'.format(self.id))
        return CategoryInstance(self.version, response.json())


class CategoryList(Resource):

    def __init__(self, version):
        super(CategoryList, self).__init__(version)

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
