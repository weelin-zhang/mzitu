# mzitu
爬取mzitu.com所有妹子写真


from requesttool import download,mkdir

from bs4 import BeautifulSoup

import os,time,random,sys

一些说明:


mzitu/src/mzitu/main/main.py(本爬虫主程序)

mzitu/src/mzitu/main/requesttool.py(为本爬虫定义了一个下载工具)

mzitu/src/mzitu/main/mainmultiprocessing.py(本爬虫程序的多进程尝试)

mzitu/src/mzitu/main/selenium_baiduyun.py(与本爬虫无关，记录了selenium的简单使用)

