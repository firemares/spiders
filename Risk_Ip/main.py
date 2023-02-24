import requests
import re
import time
import pymysql
import urllib
import count_num
import file_write
import get_url
import open_file
import insert_ip
import datetime
from fake_useragent import UserAgent

ua=UserAgent()
headers = {
    'Cookie':'Cookie: showTips=true; csrfToken=PId6PwRpOaB8Qh676bz-o3Xv; day_first_activity=true; rememberme=ad6e5602a0bc582fea4f75385c53b7c264a8f07e|2ec56589c9914efaa84556599b831697|1670923000734|public|w; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222ec56589c9914efaa84556599b831697%22%2C%22first_id%22%3A%221820f058798d63-074163195aabca4-26021a51-1327104-1820f058799d0c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.threatbook.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyMGYwNTg3OThkNjMtMDc0MTYzMTk1YWFiY2E0LTI2MDIxYTUxLTEzMjcxMDQtMTgyMGYwNTg3OTlkMGMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyZWM1NjU4OWM5OTE0ZWZhYTg0NTU2NTk5YjgzMTY5NyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222ec56589c9914efaa84556599b831697%22%7D%2C%22%24device_id%22%3A%221820f058798d63-074163195aabca4-26021a51-1327104-1820f058799d0c%22%7D',
    'Host':'x.threatbook.com',
    'User-Agent': ua.random
}

date_time = datetime.date.today()
#循环拿出一条地址里面的所有ip，放入txt文件中
def get_ip(parse):
    url = parse
    # response = requests.get(url)
    response = requests.get(url,headers=headers)
    # print(response.text)
    ip_translate = re.compile('(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})',re.S)
    ip_check = re.findall(ip_translate,response.text)
    ip_num = len(ip_check)
    for ip_id in range(ip_num):
        ip = ip_check[ip_id][0]
        if ip_check!=None:
            # 写入txt中
            file_write.file_write(ip)
            # 写入mysql数据库中
            insert_ip.insert_ip(url,ip,date_time)
            # print(ip + '成功传入数据库')

        else:
            print('爬取失败，请检查问题！！')
    # time.sleep(5)
    # print(ip_check)




filename='url.txt'

# 拿到所有存在风险ip的列表
url_list = open_file.open_file(filename)

# 计算所有风险url的数量
count = count_num.count_num(url_list)



# print(url_list)
for i in range(0,count):
# 循环从列表取出每一条url地址
    url_parse= get_url.get_url(i)
    # print(url_parse)
    # print(type(url_parse))

# 循环从地址取出所有ip，放入txt文件中
    get_ip(url_parse)
    print(url_parse+'       爬取完毕')
    time.sleep(30)

# print(count)
