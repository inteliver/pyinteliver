# This class will help to upload a file
import os
from datetime import datetime
import requests
import hmac
import hashlib
from InteliverConfig import InteliverConfig


class Uploader:
    def __init__(self, config=None):
        self.config = None
        if isinstance(config, InteliverConfig):
            self.config = config

    def upload(self, filepath):
        if not self.config:
            return "err/config not set"
        if not self.config.get_cloudname():
            return " err/config cloudname not set"
        if not self.config.get_token():
            return " err/config token not set"

        name, ext = os.path.splitext(filepath)
        with open(filepath, 'rb') as d:
            data = d.read(-1)
        data = {'data': str(data),
                'type': str(ext),
                'cloudname': str(self.config.get_cloudname()),
                'timestamp': str(self.utc_timestamp())}

        data['signature'] = self.signature(data, self.config.get_token())
        resp = requests.post('https://api.inteliver.com/api/v1/upload', data)
        if resp.status_code != 200:
            return "err/{} - {}".format(resp.status_code, resp.content)

        return resp.content

    @staticmethod
    def utc_timestamp():
        return int((datetime.utcnow() - datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())

    @staticmethod
    def signature(data_dict, token):
        message = '&'.join([str(i[0])+'='+str(i[1]) for i in sorted(data_dict.items()) if i[0] != 'signature'])
        return hmac.new(token, message, hashlib.sha1).hexdigest()
