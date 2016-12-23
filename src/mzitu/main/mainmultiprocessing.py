#_*_coding:utf-8_*_
'''
Created on 2016年11月13日

@author: ZWJ
'''
from requesttool import download,mkdir
from bs4 import BeautifulSoup
import os,time,random,sys

from multiprocessing import Pool

SaveDir = r'C:\Users\ZWJ\Desktop\Pyspider\mzitu'
MainPageUrl= 'http://www.mzitu.com/'
BaseUrl = 'http://www.mzitu.com/page/1'

#创建文件夹
mkdir(SaveDir)
#创建类
downtool = download()

def saveImages(url,savepath):
    html = downtool.get(url, 3, False).text
    soup = BeautifulSoup(html,'lxml')
    
    try:
        img_num = int(soup.find('div',class_='pagenavi').find_all('span')[6].get_text())
        img_url_l = list(url+'/'+str(i) for i in range(1,img_num+1))
        #开始存储照片
        img_index = 1
        for img_url in img_url_l:
            #拿到照片的详细地址
            imghtml = downtool.get(img_url,3).text
            imgsoup = BeautifulSoup(imghtml,'lxml')
            
            imgsource = imgsoup.find('div',class_='main-image').p.img['src']
            img_name = str(img_index)+'.jpg'
            img_path = os.path.join(savepath,img_name)
            #判断是否存在文件图片
            if os.path.exists(img_path):print u'已经有喽。。。。';continue

            #开始存储
            try:
                data = downtool.get(imgsource,3).content

                with open(img_path,'wb') as f:
                    #print os.path.join(savepath,'%s.jpg'%img_index)
                    print u'正在保存第%s张mm照片'%str(img_index)
                    f.write(data)
                img_index += 1
            except Exception as e:
                print '111',e
                return
    except Exception as e:
        print u'跳过',e
        return
    
def get_girls_imgs(url,pagedir):
    html = downtool.get(url,3,False).text
    soup = BeautifulSoup(html,"lxml")
    li_list = soup.find('ul',id="pins").find_all('li')
    girl_imgurl_l,girl_img_title_l= [],[]
    for li in li_list:
        #拿到图集连接
        girl_imgurl_l.append(li.a.attrs['href'])
        #拿到图集主题
        girl_img_title_l.append(li.span.get_text())
    
    summary_l = zip(girl_img_title_l,girl_imgurl_l)
    
    #处理summary_l [('性感尤物九儿火爆身材姿态撩人 傲人巨乳呼之欲出','http://www.mzitu.com/79442'),()...]
    title_index = 1
    for sub in summary_l:
        #创建文件夹
        imgstitle = str(title_index)+'-'+sub[0].split()[0]
        if '/' in imgstitle:imgstitle = imgstitle.replace('/','-')
        if '?' in imgstitle:imgstitle = imgstitle.replace('?','')
        imgsavepath=os.path.join(pagedir,imgstitle)
        mkdir(imgsavepath)
        title_index += 1
        #抓取图集并存入文件夹
        print u'正在爬取%s专辑'%(imgstitle)
        saveImages(sub[1],imgsavepath)


       
def main():
    #获取总的页数
    mainhtml = downtool.get(MainPageUrl, 3).text
    if 'you are not allowed to access this website' in mainhtml:sys.exit('forbidden!')
    mainsoup = BeautifulSoup(mainhtml,'lxml')
    total_page_num = int(mainsoup.find('div',class_='nav-links').find_all('a')[3].get_text())
    
    
    for i in range(125,total_page_num+1):
        pagedir = os.path.join(SaveDir,str(i))
        mkdir(pagedir)
        print u'正在爬取第%s页的mm照片...'%str(i)
        get_girls_imgs(MainPageUrl+'page/'+str(i),pagedir)
if __name__ == '__main__':
    main()

        
    
    
    
