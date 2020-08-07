import unittest
from api.api_channels import ApiChannel
from tools.read_json import ReadJson
from parameterized import parameterized

def get_data():
    data = ReadJson('channels.json').read_json()
    arrs = []
    arrs.append((
        data.get('url'),
        data.get('headers'),
        data.get('expect_result'),
        data.get('status_code')
    ))
    return arrs

class TestChannels(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_channels(self,url,headers,expect_result,status_code):
        res = ApiChannel().api_get_channels(url,headers)
        self.assertEqual(expect_result,res.json()['message'])
        self.assertEqual(status_code,res.status_code)


if __name__ == '__main__':
    unittest.main()