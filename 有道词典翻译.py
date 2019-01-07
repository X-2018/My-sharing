# GITHUB:https://github.com/X-2018
#website:www.test407.cn
import urllib.request
import urllib.parse
import json             #语言编码和解码
import time

while True:
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    fy=input("请输入要翻译的内容（退出请输入q）：")
    print('\n')

    if  fy=='q':
        break
    
    elif fy!='':
        try:
            


            data={}                 #定义一个data字典，用于放head头
            data['i']=fy
            data['from']= 'AUTO'
            data['to']= 'AUTO'
            data['smartresult']= 'dict'
            data['client']='fanyideskweb'
            data['salt'] = '1539837013850'
            data['sign']= '214f22f0ed631470031995ce9efc94b2'
            data['doctype']= 'json'
            data['version']= '2.1'
            data['keyfrom']='fanyi.web'
            data['action']= 'FY_BY_REALTIME'
            data['typoResult']= 'false'
            data = urllib.parse.urlencode(data).encode("UTF-8")   #这个函数主要用于分析URL中query组件的参数，返回一个key-value对应的字典格式

            req = urllib.request.Request(url,data)              #发送Request请求
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')     #变更User-Agent属性

            response = urllib.request.urlopen(req)              
            html=response.read().decode('UTF-8')

            target = json.loads(html)
            target =target['translateResult'][0][0]['tgt']
            print("翻译结果是:  %s \n\n\n========================================="% target)
            print('User-Agent信息：%s\n'% req.headers)
            print('5秒后继续...')
            print('-----------------------------------------')
            time.sleep(5)
        except  Exception as e:
            print("\n出错了！出错信息：",e)
            print("\n")


    else:
        print("您输入为空！！\n")
