
filename='../url.txt'

# 打开文件
def open_file(filename):
    arr=[]
    file=open(filename,'r')
    read=file.readlines()

    for row in read:
        # 将换行替换为空
        tt = row.replace('\n','')
        arr.append(tt)

    return arr
    # print(arr)
