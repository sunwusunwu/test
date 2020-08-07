import json


class ReadJson(object):
    def __init__(self,filename):
        self.filepath = "data/" + filename

    def read_json(self):
        with open(self.filepath,'r',encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    # def get_data():
    data = ReadJson('login.json').read_json()
    arrs = []
    arrs.append((
            data.get('url'),
            data.get('data'),
            data.get('expect_result'),
            data.get('status_code')
       ))
    print(arrs)
       # return arrs