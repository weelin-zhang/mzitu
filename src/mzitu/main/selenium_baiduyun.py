#_*_coding:utf-8_*_


from selenium import webdriver
import time,Image,requests,os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
ChromeDriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'

#phantomjspath = r'C:\phantomjs-2.1.1\bin\phantomjs'

#打开phantomjs
#driver = webdriver.PhantomJS(executable_path=phantomjspath)

driver = webdriver.Chrome(ChromeDriver)

#登录
driver.get('http://pan.baidu.com/')
#设置自动登录为否
driver.find_element_by_name('memberPass').click()
#输入用户名
driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys(u'w张卫健')
#输入密码
driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('213369w')
time.sleep(3)
#拿到验证码图片
validate_img = driver.find_element_by_id('TANGRAM__PSP_4__verifyCodeImg').get_attribute("src")
#吊起验证码图片
#1.存到本地
try:
	with open(r'C:\Users\ZWJ\Desktop\pic\validate.jpg','wb') as f:
		data=requests.get(validate_img).content
		f.write(data)
except Exception as e:
	print e

print validate_img
#2.打开validate.png

vali_im=Image.open(r'C:\Users\ZWJ\Desktop\pic\validate.jpg')
vali_im.show()
#3.输入验证码

validate_str = raw_input('input validate code you see:')

os.remove(r'C:\Users\ZWJ\Desktop\pic\validate.jpg')
driver.find_element_by_id('TANGRAM__PSP_4__verifyCode').send_keys(validate_str.decode('gbk'))

driver.find_element_by_id('TANGRAM__PSP_4__submit').click()

time.sleep(5)#等待弹出框框
try:
	driver.find_element_by_xpath('/html/body/div[4]/div[2]').click()
	print '0'
except:
	pass

#点击上传按钮
#driver.find_element_by_id('h5Input0').click()

time.sleep(2)
#点击视频
try:
	driver.find_element_by_xpath('//*[@id="layoutAside"]/div/ul[1]/li[4]/a/span/span').click()
	print '1'
except:
	print 'error1'
time.sleep(2)
#检查是否点击了视频(找一部视频)
try:
	videoele = driver.find_element_by_xpath('//*[@id="layoutMain"]/div[3]/div[3]/div/div[1]/dd[1]/div[2]/div[1]/a')
	print videoele.text
except:
	print 'error2'
	pass


driver.get('http://www.baidu.com')

time.sleep(2)


driver.back()

time.sleep(2)

driver.forward()
driver.close()
#print driver.get_cookies()


#/html/body/div[4]/div[2]

#//*[@id="layoutAside"]/div/ul[1]/li[4]/a/span/span