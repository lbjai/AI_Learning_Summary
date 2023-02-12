import requests
import threading

def get_stock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    r = requests.get(url)
    expr = (r.text)[4:]
    exec(expr)  # 以下用到动态语言的动态机制
    name = 'hq_str_' + code
    info = eval(name)
    info = info.split(',')
    with open(info[0] + '.txt', 'a+') as f:
        ts = info[-3] + ' ' + info[-2]
        price = info[3]
        f.write(ts + ': ' + price + '\n')

codes = ['sz000878', 'sh600993', 'sz000002', 'sh600153', 'sz002230', 'sh600658']
threads = [threading.Thread(target = get_stock, args = (code, )) for code in codes]
for t in threads:
    t.start()
for t in threads:
    t.join()
