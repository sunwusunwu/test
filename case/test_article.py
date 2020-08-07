import unittest
from api.api_article import ApiAticle
from tools.read_json import ReadJson
from parameterized import parameterized

def get_data_add():
    data = ReadJson("article_add.json").read_json()
    arrs = []
    arrs.append((
        data.get('url'),
        data.get('headers'),
        data.get('data'),
        data.get('expect_result'),
        data.get('status_code')
    ))
    return arrs

def get_data_cancel():
    data = ReadJson("article_cancel.json").read_json()
    arrs = []
    arrs.append((
        data.get('url'),
        data.get('headers'),
        data.get('status_code')
    ))
    return arrs


class TestArticle(unittest.TestCase):
    @parameterized.expand(get_data_add())
    def test_article(self,url,headers,data,expect_result,status_code):
        res = ApiAticle().api_post__article(url,headers,data)
        self.assertEqual(expect_result,res.json()['message'])
        self.assertEqual(status_code,res.status_code)

    @parameterized.expand(get_data_cancel())
    def test_cancel(self,url,headers,status_code):
        res = ApiAticle().api_delete_cancel(url,headers)
        self.assertEqual(status_code,res.status_code)


if __name__ == '__main__':
    unittest.main()