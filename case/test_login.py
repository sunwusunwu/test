import unittest
from api.api_login import ApiLogin
from tools.read_json import ReadJson
from parameterized import parameterized

def get_data():
    data = ReadJson('login.json').read_json()
    arrs = []
    arrs.append((
        data.get('url'),
        data.get('headers'),
        data.get('data'),
        data.get('expect_result'),
        data.get('status_code')
    ))
    return arrs


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self,url,headers,data,expect_result,status_code):
        res = ApiLogin().api_post_login(url,headers,data)
        self.assertEqual(expect_result,res.json()['message'])
        self.assertEqual(status_code,res.status_code)


if __name__ == '__main__':
    unittest.main()