import open_file

filename='url.txt'
# 输出数据
def get_url(uid):
    url = open_file.open_file(filename)
    over = url[uid]
    return over