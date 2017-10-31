# This is the class used for setting and getting cloudname and token
# You need both cloudname and token set to upload a file
# with only cloudname set you will be able to get data


class InteliverConfig:
    def __init__(self, cloudname=None, token=None):
        self._cloudname = cloudname
        self._token = token

    def set_cloudname(self, cloudname):
        self._cloudname = cloudname

    def set_token(self, token):
        self._token = token

    def get_cloudname(self):
        return self._cloudname

    def get_token(self):
        return self._token
