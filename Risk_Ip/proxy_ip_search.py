from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import pymysql

db = pymysql.connect(host='localhost',user='root',password='root',port=3306,database='spiders',autocommit=True)
cursor = db.cursor()


# 定义一个sql插入函数
def insert_proxy(ip,port,address1,address):
    try:
        cursor.execute(sql_select,ip)
        if cursor.fetchone() == None:
            cursor.execute(sql_insert,(ip,port,address1,address))
            db.commit()
        else:
            print(ip+'该ip重复')
    except:
        db.rollback()
    # db.close()


# 定义sql语句
sql_insert = 'insert ignore into proxy_ip(ip ,port ,address1 ,address) values(%s,%s,%s,%s)'
sql_select = 'select * from proxy_ip where ip = %s '

url = 'https://www.89ip.cn/'

ua=UserAgent()
headers = {
    'Cookie':'Cookie: showTips=true; csrfToken=PId6PwRpOaB8Qh676bz-o3Xv; day_first_activity=true; rememberme=ad6e5602a0bc582fea4f75385c53b7c264a8f07e|2ec56589c9914efaa84556599b831697|1670923000734|public|w; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%222ec56589c9914efaa84556599b831697%22%2C%22first_id%22%3A%221820f058798d63-074163195aabca4-26021a51-1327104-1820f058799d0c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.threatbook.cn%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTgyMGYwNTg3OThkNjMtMDc0MTYzMTk1YWFiY2E0LTI2MDIxYTUxLTEzMjcxMDQtMTgyMGYwNTg3OTlkMGMiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIyZWM1NjU4OWM5OTE0ZWZhYTg0NTU2NTk5YjgzMTY5NyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%222ec56589c9914efaa84556599b831697%22%7D%2C%22%24device_id%22%3A%221820f058798d63-074163195aabca4-26021a51-1327104-1820f058799d0c%22%7D',
    'Host':'www.89ip.cn',
    'User-Agent': ua.random
}


response = requests.get(url,headers=headers)

# 选择lxml作为解析器
soup = BeautifulSoup(response.text,'lxml')

# 定义一个列表作为后续数据的容器
dict = []

# print(type(dict))
# print(soup.find_all(name='td'))

# 循环取出ip的信息
for td in soup.select('td'):
    content = td.string.strip()
    dict.append(content)
print(len(dict))

# print(dict)
num = len(dict)
i=0
p=1
a1=2
a=3
for x in range(num):
    if i < num:
        ip = dict[i]
        port = dict[p]
        address1 = dict[a1]
        address = dict[a]
        i = i + 5
        p = p + 5
        a1 = a1 + 5
        a = a + 5
        insert_proxy(ip,port,address1,address)
        print(ip)
        # print(port)
        # print(address1)
        # print(address)
    else:

        print('over')
        exit()

