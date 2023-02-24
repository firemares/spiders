import time

import requests
import urllib
import re
from urllib import parse
import pymysql
from fake_useragent import UserAgent

url='https://x.threatbook.com/v5/article?threatInfoID='
url_text='https://x.threatbook.com/v5/article?threatInfoID=40553'
db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
ua=UserAgent()
headers = {
    'Cookie':'Cookie: showTips=true; csrfToken=PId6PwRpOaB8Qh676bz-o3Xv; day_first_activity=true; rememberme=ad6e5602a0bc582fea4f75385c53b7c264a8f07e|2ec56589c9914efaa84556599b831697|1670923000734|public|w; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222ec56589c9914efaa84556599b831697%22%2C%22first_id%22%3A%221820f058798d63-074163195aabca4-26021a51-1327104-1820f058799d0c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.threatbook.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyMGYwNTg3OThkNjMtMDc0MTYzMTk1YWFiY2E0LTI2MDIxYTUxLTEzMjcxMDQtMTgyMGYwNTg3OTlkMGMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyZWM1NjU4OWM5OTE0ZWZhYTg0NTU2NTk5YjgzMTY5NyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222ec56589c9914efaa84556599b831697%22%7D%2C%22%24device_id%22%3A%221820f058798d63-074163195aabca4-26021a51-1327104-1820f058799d0c%22%7D',
    'Host':'x.threatbook.com',
    'User-Agent': ua.random
}
# 定义光标
cursor=db.cursor()

# 准备sql
sql_insert='insert ignore into get_url(url) values(%s)'
sql_search='select * from get_url where url = %s'

print('欢迎使用风险url采集爬虫')
print('请输入需要采集网页的起始id--推荐输入id>30000')
start_id=int(input())
print('请输入需要采集网页的结束id--推荐输入id<50000')
end_id=int(input())


uid = 0
# 配置采集的网页的范围
for i in range(start_id,end_id):
    id=i
    url_all=url+str(id)
    response = requests.get(url_all,headers=headers)
    ip_translate=re.compile('(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})',re.S)
    ip_check=re.search(ip_translate,response.text)
    if ip_check!=None:
        cursor.execute(sql_search,(url_all))
        url_check = cursor.fetchone()
        if url_check == None:
            try:
                uid=uid+1
                cursor.execute(sql_insert,(url_all))
                db.commit()
                url_txt = open('new_url.txt', 'a')
                url_txt.write(url_all + '\n')
                print('已成功采集到'+url_all)
            except:
                db.rollback()
                print('error')
        else:
            print(url_all+'该url已存在')
        # db.close()
    else:
        print(ip_check)
    time.sleep(120)

# re_request = re.compile('(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})', re.S)
# re_result = re.findall(re_request, response.text)
# for x in range(10000):
#         # print(re_result[x][0])
#     x = re_result[x][0]
#     if x!='':
#         print(x)
#         ip = open('ip.txt', 'a', encoding='utf8')
#         ip.write(x + '\n')
#     else:
#         print('1')

# response=requests.get(url)
# print(response.text)

# re_request=re.compile('(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})',re.S)
# re_result=re.findall(re_request,response.text)
# for x in range(100):
#     # print(re_result[x][0])
#     x=re_result[x][0]
#     print(x)
#     ip = open('ip.txt', 'a', encoding='utf8')
#     ip.write(x+'\n')