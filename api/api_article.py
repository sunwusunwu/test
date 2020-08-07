import requests


class ApiAticle(object):
    def api_post__article(self,url,headers,data):
        return requests.post(url,headers=headers,json=data)

    def api_delete_cancel(self,url,headers):
        return requests.delete(url,headers=headers)
