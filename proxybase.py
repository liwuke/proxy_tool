import re
import asyncio
import json
import aiohttp
from keywords import Get
from socketbase import Sendmethod

class Proxy:


    def __init__(self):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        self.url_list=[]
        self.proixes={}
        self.good_proixes={}
        self.index=0
        # self.target_url='https://miaomiao.scmttec.com/seckill/seckill/now2.do'
        self.target_url='https://www.baidu.com'
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


    def freedaili(self):
        for i in range(1,4):
            url=f'https://ip.jiangxianli.com/?page={i}&country=%E4%B8%AD%E5%9B%BD'
            # res=Sendmethod().method('get',url)
            # content=re.findall('<link rel="dns-prefetch" href="//github.com">(.*?)<link rel="dns-prefetch" href="//buy.jiangxianli.com">', res.text,re.S)
            # ips=re.findall('<link rel="dns-prefetch" href="//(.*?):', content[0])
            # ports=re.findall(':(.*?)">', content[0])
            # for ip, port in zip(ips, ports):
            #     self.proixes[ip] = port
            self.url_list.append(('freedaili', url))


    def daili89(self):
        for i in range(1, 7):
            url=f'https://www.89ip.cn/index_{i}.html'
            # res = Sendmethod().method('get', url)
            # content=re.findall('<td>(.*?)</td>', res.text,re.S)
            # ips=[content[index].strip('\n').strip('\t') for index in range(0,len(content),5)]
            # ports=[content[index].strip('\n').strip('\t') for index in range(1,len(content),5)]
            # for ip, port in zip(ips, ports):
            #     self.proixes[ip] = port
            self.url_list.append(('daili89', url))


    def zhandaye(self):
        main_url='https://www.zdaye.com'
        self.header={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
        }
        res = Sendmethod().method('get', main_url+'/dayProxy.html',headers=self.header)
        main_pages = re.findall('<H3 class="thread_title"><a href="(.*?)">', res.text)
        for main_page in main_pages[0:3]:
            url=main_url+main_page
            for x in range(6):
                if x ==0:
                    self.url_list.append(('zhandaye', url))
                else:
                    self.url_list.append(('zhandaye', url[:-5]+'/'+str(x)+'.html'))


    async def crawl_ip(self,item):
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(trust_env=True) as conn:
            async with conn.get(item[1], timeout=timeout, ssl=False) as res:
                response = await res.text()
                if item[0] == 'kuaidaili':
                    ips = re.findall('<td data-title="IP">(.*?)</td>', response)
                    ports = re.findall('<td data-title="PORT">(.*?)</td>', response)
                    for ip, port in zip(ips, ports):
                        self.proixes[ip] = port
                elif item[0] == 'xiaohuan':
                    content = re.findall('<img src="/flag/CN.svg">(.*?) href="/address/5Lit5Zu9.html">', response)
                    for i in content:
                        ip = re.findall('(.*?)</a></td><td>', i)
                        port = re.findall('</a></td><td>(.*?)</td><td><a', i)
                        self.proixes[ip[0]] = port[0]
                elif item[0] == 'ip66':
                    ips = re.findall('<tr><td>(.*?)</td><td>', response)[1:]
                    ports = re.findall('</td><td>(.*?)</td><td>', response)
                    ports = list(filter(lambda x: x.isdigit(), ports))
                    for ip, port in zip(ips, ports):
                        self.proixes[ip] = port
                elif item[0] == 'dieniao':
                    ips = re.findall("<span class='f-address'>(.*?)</span>",response)[1:]
                    ports = re.findall("<span class='f-port'>(.*?)</span>", response)
                    ports = list(filter(lambda x: x.isdigit(), ports))
                    for ip, port in zip(ips, ports):
                        self.proixes[ip] = port
                elif item[0] == 'kaixin':
                    ips = Get.get_keyword(json.loads(response), 'ip')
                    ports = Get.get_keyword(json.loads(response), 'port')
                    for ip, port in zip(ips, ports):
                        self.proixes[ip] = port
                elif item[0] == 'yundaili':
                    content = re.findall("<tr>(.*?)</tr>", response, re.S)[1:]
                    for item in content:
                        ip = re.findall("<td>(.*?)</td>", item)[0]
                        port = re.findall("<td>(.*?)</td>", item)[1]
                        self.proixes[ip] = port
                elif item[0] == 'freedaili':
                    content = re.findall('<link rel="dns-prefetch" href="//github.com">(.*?)<link rel="dns-prefetch" href="//buy.jiangxianli.com">',response, re.S)
                    ips = re.findall('<link rel="dns-prefetch" href="//(.*?):', content[0])
                    ports = re.findall(':(.*?)">', content[0])
                    for ip, port in zip(ips, ports):
                        self.proixes[ip] = port
                elif item[0] == 'daili89':
                    content = re.findall('<td>(.*?)</td>', response, re.S)
                    ips = [content[index].strip('\n').strip('\t') for index in range(0, len(content), 5)]
                    ports = [content[index].strip('\n').strip('\t') for index in range(1, len(content), 5)]
                    for ip, port in zip(ips, ports):
                        self.proixes[ip] = port
                elif item[0] == 'zhandaye':
                    ips = re.findall('<a href="/ip/CheckHttp/(.*?)" title=', response)
                    for i in ips:
                        self.proixes[i.split(':')[0]] = i.split(':')[1]
                self.index+=1
                self.progress_bar('爬取IP进度',len(self.url_list))


    def progress_bar(self,msg,length):
        print('\r',f"{msg}: {int((self.index/length)*100)}%: ", "▋" * int((self.index / length)*100), end="")


    async def check_proxy(self,proxy):
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(trust_env=True) as conn:
            async with conn.get(self.target_url,timeout=timeout,proxy=f'http://{proxy[0]}:{proxy[1]}',ssl=False) as res:
                self.index += 1
                response = await res.text()
                if res.status in (200,201,202,203,204,205,206) and response:
                    self.good_proixes[proxy[0]]=proxy[1]
                    self.progress_bar('成功率', len(self.proixes))


    async def main(self):
        self.kuaidaili()
        self.xiaohuan()
        self.ip66()
        self.dieniao()
        self.kaixin()
        self.yundaili()
        self.freedaili()
        self.daili89()
        self.zhandaye()
        tasks = [asyncio.ensure_future(self.crawl_ip(item)) for item in self.url_list]   #爬取代理ip
        await asyncio.gather(*tasks,return_exceptions=True)
        self.index=0   #重置index
        tasks=[asyncio.ensure_future(self.check_proxy(proxy)) for proxy in self.proixes.items()]   #检查有效代理ip
        await asyncio.gather(*tasks,return_exceptions=True)


    def entrance(self):
        loop=asyncio.get_event_loop()
        loop.run_until_complete(self.main())


if __name__ == '__main__':
    a=Proxy()
    a.entrance()
    print(a.good_proixes)