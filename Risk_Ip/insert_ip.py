import pymysql
import datetime
import cmd_color


def insert_ip(url_address,ip,date_time):
    # 链接数据库
    db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders', autocommit=True)
    cursor = db.cursor()

    sql_creat = 'CREATE TABLE if not exists ip_table (`id`  int NOT NULL AUTO_INCREMENT,`url_address`  varchar(255) not NULL ,`ip`  varchar(255) not NULL ,`date_time`  varchar(255) not NULL ,PRIMARY KEY (`id`));'
    sql_insert = 'insert ignore into ip_table(url_address, ip, date_time) values(%s,%s,%s)'
    sql_sel='select id from ip_table where ip = %s'
    # 创建数据库
    cursor.execute(sql_creat)
    try:
        cursor.execute(sql_sel,(ip))
        if cursor.fetchone()==None:
            try:
                cursor.execute(sql_insert,(url_address,ip,date_time))
                db.commit()
                id = cursor.lastrowid
                print('这是第' + str(id) + '条ip，它的ip地址是' + ip + '。它的入库日期是' + str(date_time))
            except:
                db.rollback()

        else:
            cmd_color.printGreen('warring!!!!')
            print('ip:' + ip + '已存在')

            cmd_color.printGreen('该问题出现的原因：'+'\n'+'1）main.py爬取的url.txt中的文件是重复的--请及时更新'+'\n'+'2）数据库中已存在该ip'
                                '--如果您更新了url.txt，然后爬取了100条以上的url，且每条ip都提示”ip已存在“，说明您更新的url存在大量重复')
    except:
        print('插入失败!请联系创作者HHB')
    # db.close()


# insert_ip(url_address='2',ip='2')
# 执行
# cursor.execute(sql_creat)
# try:
#     cursor.execute(sql_insert,(id,url_address,ip))
#     db.commit()
#     print('插入成功')
# except:
#     db.rollback()
#     print('插入失败')
#     print(cursor.fetchall())
# 打印结果


