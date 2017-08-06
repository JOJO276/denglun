# -*-coding: utf-8 -*-
'''
Created by jojo at 2017/8/5
'''
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#
# with open("/Users/jojo/PycharmProjects/denglun/yd/untitled3/sinaAccount.file/inactive.txt", 'a+') as file:
#      file.write('ejwelahulehf\n')
driver = webdriver.Safari()
#geckodriver = "/Applications/Firefox.app/Contents/geckodriver"
#os.environ["webdriver.firefox.bin"] = geckodriver
#brower = webdriver.Firefox(geckodriver)
brower = webdriver.Safari()
url = 'http://m.weibo.cn/'
# url = 'http://weibo.com/u/6283668410/home?topnav=1&wvr=6'
# url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
brower.set_window_size(480, 760)
brower.get(url)
print("dakai")
time.sleep(20)
#brower.close()
print('guanbi')
#brower.quit()
print('ooooooo')