import requests


class ApiChannel(object):
    def api_get_channels(self,url,headers):
        return requests.get(url,headers=headers)