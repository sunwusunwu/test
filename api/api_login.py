import requests


class ApiLogin(object):
    def api_post_login(self,url,headers,data):
        return requests.post(url,headers=headers,json=data)