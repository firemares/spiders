
print('欢迎使用风险ip更新系统,请输入对应指令进行操作')
content=input()
if content == 'get_url':
    print('正在获取存在风险IP的url')
elif content == 'get_ip':
    print('正在获取存在风险IP')
elif content == 'check_info':
    print('请输入需要查询的时间')
    c_time = input()
    if c_time == '1':
        print('正在查询')
    else:
        print('该时间段无数据')
else:
    print('请输入正确的参数')