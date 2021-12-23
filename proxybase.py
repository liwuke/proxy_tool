import re
import asyncio
import json
import aiohttp
from socketbase import Sendmethod
from keywords import Get

class Proxy:


    def __init__(self):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        self.url_list=[]
        self.proixes={}
        self.good_proixes={}
        self.target_url='https://miaomiao.scmttec.com/seckill/seckill/now2.do'
        self.header = {
            'host': 'miaomiao.scmttec.com'
            , 'accept': 'application/json, text/plain, */*'
            ,'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
            , 'x-requested-with': 'XMLHttpRequest'
            , 'content-type': 'application/json'
            , 'referer': 'https://servicewechat.com/wxff8cad2e9bf18719/22/page-frame.html'
            , 'accept-encoding': 'gzip, deflate, br'
        }


    def kuaidaili(self):
        url='https://www.kuaidaili.com/free/inha/'
        for i in range(1,3):
            # res=Sendmethod.method('get',url+str(i)+'/')
            # ips=re.findall('<td data-title="IP">(.*?)</td>',res.text)
            # ports=re.findall('<td data-title="PORT">(.*?)</td>',res.text)
            # for ip,port in zip(ips,ports):
            #     self.proixes[ip]=port

            self.url_list.append(('kuaidaili',url+str(i)+'/'))


    def xiaohuan(self):
        url='https://ip.ihuan.me/address/5Lit5Zu9.html?page='
        pages=['b97827cc','4ce63706','5crfe930']
        for page in pages:
            # res = Sendmethod.method('get', url + page)
            # content=re.findall('<img src="/flag/CN.svg">(.*?) href="/address/5Lit5Zu9.html">', res.text)
            # for i in content:
            #     ip = re.findall('(.*?)</a></td><td>', i)
            #     port = re.findall('</a></td><td>(.*?)</td><td><a', i)
            #     self.proixes[ip[0]]=port[0]

            self.url_list.append(('xiaohuan',url + page))


    def ip66(self):
        url = 'http://www.66ip.cn/index.html'
        # res = Sendmethod.method('get', url)
        # ips = re.findall('<tr><td>(.*?)</td><td>', res.text)[1:]
        # ports = re.findall('</td><td>(.*?)</td><td>', res.text)
        # ports=list(filter(lambda x:x.isdigit(),ports))
        # for ip,port in zip(ips,ports):
        #     self.proixes[ip]=port

        self.url_list.append(('ip66',url))


    def dieniao(self):
        url='https://www.dieniao.com/FreeProxy.html'
        # res = Sendmethod.method('get', url)
        # ips = re.findall("<span class='f-address'>(.*?)</span>", res.text)[1:]
        # ports = re.findall("<span class='f-port'>(.*?)</span>", res.text)
        # ports = list(filter(lambda x: x.isdigit(), ports))
        # for ip,port in zip(ips,ports):
        #     self.proixes[ip]= port

        self.url_list.append(('dieniao',url))


    def kaixin(self):
        url='https://proxy11.com/api/demoweb/proxy.json'
        # res = Sendmethod.method('get', url)
        # ips=Get.get_keyword(json.loads(res.text),'ip')
        # ports=Get.get_keyword(json.loads(res.text),'port')
        # for ip,port in zip(ips,ports):
        #     self.proixes[ip] = port

        self.url_list.append(('kaixin',url))


    def yundaili(self):
        url='http://www.ip3366.net/?stype=1&page='
        for i in range(1,4):
            # res = Sendmethod.method('get', url+str(i))
            # content=re.findall("<tr>(.*?)</tr>", res.text,re.S)[1:]
            # for item in content:
            #     ip=re.findall("<td>(.*?)</td>", item)[0]
            #     port=re.findall("<td>(.*?)</td>", item)[1]
            #     self.proixes[ip]=port
            self.url_list.append(('yundaili',url+str(i)))


    async def check_proxy(self,proxy):
        timeout = aiohttp.ClientTimeout(total=10, connect=10, sock_connect=10, sock_read=10)
        async with aiohttp.ClientSession(trust_env=True) as conn:
            async with conn.get(self.target_url,timeout=timeout,proxy=f'http://{proxy[0]}:{proxy[1]}',ssl=False,headers=self.header) as res:
                response = await res.text()
                if response:
                    self.good_proixes[proxy[0]]=proxy[1]


    async def main(self):
        tasks=[asyncio.ensure_future(self.check_proxy(proxy)) for proxy in self.proixes.items()]
        await asyncio.gather(*tasks,return_exceptions=True)


    def entrance(self):
        self.kuaidaili()
        loop=asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        print(self.good_proixes)


if __name__ == '__main__':
    # Proxy().entrance()
    a=Proxy()
    a.kuaidaili()
    a.xiaohuan()
    a.ip66()
    a.dieniao()
    a.kaixin()
    a.kaixin()
    a.yundaili()
    print(a.url_list)