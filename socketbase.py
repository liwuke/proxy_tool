# -*- coding:utf-8 -*-
import requests
import json
from requests.packages import urllib3


class Sendmethod:  # 这里传入的data，必须要保证值为str而不是dict，所有要用dumpts转换为str
    @staticmethod
    def method (method,url,data=None,headers=None,cookies=None,proxy=None):
        urllib3.disable_warnings ()
        # new_data = json.dumps (data) if data else None
        session = requests.session ()
        response = session.request (method,url,data = data,headers = headers,verify = False,timeout=10,cookies=cookies,proxies=proxy)
        if method == 'delete':
            return response.status_code
        else:
            return response

    @staticmethod
    def get_json (response):
        return json.dumps (response)

    @staticmethod
    def transformation (response):
        return json.load (response)


if __name__ == '__main__':
    # data={"phone":"15282897777","password":"123456"}
    print (Sendmethod.method ('get','https://www.baidu.com/'))
