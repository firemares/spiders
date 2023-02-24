import pymysql
from collections import Counter
import datetime
import file_write
import sys

print('欢迎使用ip导出功能。'+'\n'
      '查询今日是否存储ip--请输入：0'+'\n'
      '导出今日存储ip--请输入：1'+'\n'
      '退出--请输入：2'+'\n'
      '查询总ip数量--请输入：3'+'\n'
      '导出总存储ip--请输入：4'+'\n'
      )

check = input()
date_time = datetime.date.today()
db = pymysql.connect(host='localhost',user='root',password='root',port=3306,database='spiders', autocommit=True)
cursor = db.cursor()

sql_select = 'select ip from ip_table where date_time = %s'
sql_select_all = 'select ip from ip_table'



if check == '1':
    cursor.execute(sql_select, (date_time))
    infors = cursor.fetchall()
    print('正在打印，请稍后')
    for info in infors:
        str_info=str(info)
        file = open('search_ip.txt','a')
        file.write(str_info+' '+str(date_time)+'\n')
        print(str(info))
    print('打印完成，ip已写入search_ip.txt')

elif check == '2':
    print('已退出，想要获取响应请重新启动请重新启动')
    sys.exit(0)

elif check == '0':
    cursor.execute(sql_select, (date_time))
    infors = cursor.fetchall()
    print('今日采集的ip条数为'+str(cursor.rowcount))

elif check == '3':
    cursor.execute(sql_select_all)
    infors = cursor.fetchall()
    print('总ip数量为：'+str(cursor.rowcount))

elif check == '4':
    cursor.execute(sql_select_all)
    infors = cursor.fetchall()
    print('正在打印，请稍后')
    for info in infors:
        str_info = str(info)
        file = open('search_ip_all.txt', 'a')
        file.write(str_info  + '\n')
        print(info)
    print('打印完成，ip已写入search_ip.txt')

else:
    print('请输入提示的【数字】')

# print('')
