import requests
import concurrent.futures


proxylist = []
with open('proxy.txt', 'r') as f:
    for line in f:
        proxylist = [line.strip() for line in f]

def extract(proxy):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:

        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=1)
        #test proxy print(r.json(), ' | works')
        print(proxy)
    except:
        pass
        #print(proxy, 'faild')
    return proxy

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract, proxylist)
