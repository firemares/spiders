from collections import Counter

# 计算数量
def count_num(url_all):
    dict = Counter(url_all)
    num = len(dict)
    return  num