

class Resource(object):

    def __init__(self, version):
        self.version = version


class Instance(Resource):

    def __init__(self, version, properties):
        super(Instance, self).__init__(version)
        self.properties = properties

    def property(self, name, default=None):
        return self.properties.get(name, default)


class UpgradableInstance(Instance):

    def __init__(self, version, properties):
        super(UpgradableInstance, self).__init__(version, properties)

    @property
    def href(self):
        return super(UpgradableInstance, self).property('href')

    def upgrade(self):
        response = self.version.client.request('GET', self.href)
        self.properties = response.json()

    def property(self, name, default=None):
        prop = super(UpgradableInstance, self).property(name)
        if prop:
            return prop

        self.upgrade()
        return super(UpgradableInstance, self).property(name)
