import requests
import threading
import re


enableips=[]

class IsEnable(threading.Thread):
    def __init__(self,ip):
        super(IsEnable,self).__init__()
        self.ip=ip
        self.proxies={
        'http':'http://%s'%ip
        }
    def run(self):
        global enableips
        try:
            html=requests.get('http://httpbin.org/ip',proxies=self.proxies,timeout=5).text
            result=eval(html)['origin']
            if result in self.ip:
                enableips.append(self.ip)
        except:
            return False

def get_enableips():
    global enableips
    html=requests.get('http://proxy.ipcn.org/proxya.html').text
    ips=re.findall('\d+\.\d+\.\d+\.\d+:\d+',html)
    html=requests.get('http://proxy.ipcn.org/proxya2.html').text
    ips+=re.findall('\d+\.\d+\.\d+\.\d+:\d+',html)
    threadings=[]
    for ip in ips:
        work=IsEnable(ip)
        threadings.append(work)
    for work in threadings:
        work.start()
    for work in threadings:
        work.join()
    return enableips
