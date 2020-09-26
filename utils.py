import logging

import requests
from bs4 import BeautifulSoup


def assert_utils(self,response,status_code,status,desc):
    # 针对收到的响应进行断言
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get('status'))
    self.assertEqual(desc, response.json().get("description"))

def third_request_api(form_data):
    #解析form表单中的内容，并提取参数发送第三方请求
    soup = BeautifulSoup(form_data, 'html.parser')
    third_request_url = soup.form['action']
    data = {}
    for input in soup.find_all('input'):
        data.setdefault(input['name'], input['value'])
    logging.info("third request data = {}".format(data))
    # 调用响应中的url和参数来发送请求，并接收响应
    response = requests.post(third_request_url, data=data)
    logging.info("third response data={}".format(response.text))
    return response
