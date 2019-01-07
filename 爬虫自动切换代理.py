# GITHUB:https://github.com/X-2018
# Website:www.test407.cn
import urllib.request
import random
#------------------------------------------
import time


def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,20);
i=1
while 1==1:
#-------------创建定时器------------------
    try:

        
        print("执行第%d次。。"% i)
        url = 'http://www.ipshi.com/'
        iplist=['115.213.200.41:3128','61.135.217.7:80','118.190.95.35:9001','210.73.202.121:53281','101.251.255.50:38187']
        #此处IP需自己去找，本来我想做个自动收集IP的，可是没时间
        
        daili = urllib.request.ProxyHandler({'http':random.choice(iplist)})

        opener = urllib.request.build_opener(daili)
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')]
        urllib.request.install_opener(opener)

        st = urllib.request.urlopen(url)
        html=st.read()
        html = html.decode("utf-8")

        print(html)
        i+=1
        time.sleep(second);
    except (ConnectionRefusedError,TimeoutError,urllib.error.URLError):
         print("链接超时或被拒绝链接！！")
         i+=1
