import  datetime
# 写文件
time =str(datetime.datetime.now())
def file_write(txt):
    ip_txt=open('ip.txt','a')
    ip_txt.write(txt+' '+time+'\n')