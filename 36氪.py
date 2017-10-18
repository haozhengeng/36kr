import re
import json
from api import get_page

class Kr36(object):
    def __init__(self):
        self.url = 'http://36kr.com/'
        self.pattern = re.compile('<script>var props=({.*?}}})</script>', re.S)
        '''
        <script>var props={.*?}}}</script>

        '''

    def parse_data(self, str_data):
        '''使用正则匹配数据'''
        str_data = self.pattern.findall(str_data)[0]
        # print(str_data)
        # with open('temp.json', 'w') as f:
        #     f.write(str_data)

        str_data2 = re.sub(',locationnal=.*', '', str_data)
        with open('temp2.json', 'wb') as f:
            f.write(str_data2.encode())

        data_list = json.loads(str_data2)['feedPostsLatest|post']
        return data_list

        # for data in data_list:
        #     print(data)
    def save_data(self,data_list):
        '''保存数据'''
        with open('36kr.json', 'wb') as f:
            for data in data_list:
                # print(data)
                str_data = json.dumps(data, ensure_ascii=False) + ',\n'
                f.write(str_data.encode())


    def run(self):
        str_data = get_page(self.url)
        # print(str_data)
        data_list = self.parse_data(str_data)
        self.save_data(data_list)



if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()