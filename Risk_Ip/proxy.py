import requests
from fake_useragent import UserAgent


ua = UserAgent()
headers = {
    'Host':'httpbin.org',
    'User-Agent': ua.random
}
print('请输入：'+'127.0.0.1:7890'+'格式的内容')
proxy = input()
proxies ={
    'http':'http://'+ proxy,
    'https':'https://'+proxy,
}

try:
    response= requests.get('http://httpbin.org/get',proxies=proxies)
    # response = requests.get('http://httpbin.org/get',headers=headers)
    print(response.text)
except requests.exceptions.ConnectionError as e :
    print('error',e.args)
