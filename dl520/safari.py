# -*-coding: utf-8 -*-
'''
Created by jojo at 2017/8/3
'''
import os
from time import sleep
from selenium import webdriver

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

def initWork():
    driver = webdriver.Safari()  # Get local session of firefoxromedriver
    return driver


# 执行登录
def handleLogin():
    # 定义自己的用户名密码
    username = "17138955984"
    password = "youxia5533"
    # 执行操作的页面地址
    url = 'http://m.weibo.cn/'
    #driver.set_window_size(480, 760)
    driver.get(url)

    # 目前还没学会cookie怎么用先获取到吧肯定用的到
    # 获得cookie信息
    cookie1 = driver.get_cookies()
    # 将获得cookie的信息打印
    print (cookie1)
    # 下面就开始在打开的页面中自动执行操作了
    # 根据xpath获取登录按钮
    elem = driver.find_element_by_xpath("/html/body/div[1]/div/a[2]");
    # 发送确认按钮跳转到登录页面
    print('hheowhn')
    elem.send_keys(Keys.ENTER)


    # 休眠两秒钟后执行填写用户名和密码操作
    sleep(2)
    elem = driver.find_element_by_xpath("//*[@id='loginName']");

    elem.send_keys(username)
    elem = driver.find_element_by_xpath("//*[@id='loginPassword']");
    elem.send_keys(password)
    elem = driver.find_element_by_xpath("//*[@id='loginAction']");
    elem.send_keys(Keys.ENTER)
    cookie2 = driver.get_cookies()
    # 将获得cookie的信息打印
    print (cookie2)

    # 判断是否登录成功
    if cookie1 == cookie2:
        print (u' (￣y▽￣)╭可能登录失败了手动登录一下吧')
        sleep(60)
    else:
        wait = WebDriverWait(driver, 30)
        elems = wait.until(lambda driver: driver.find_elements_by_css_selector('div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option'))

    # 获取信息
    while 1:  # 循环条件为1必定成立
        result = isPresent()
        print (u'判断页面1成功 0失败  结果是=%d' % result)
        if result == 1:
            elems = driver.find_elements_by_css_selector('div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
            return elems
            break
        else:
            print (u'页面还没加载出来呢')
            sleep(20)

# 开始解析页面
def handlePage(elems):
    x = 1
    for page in elems:
        print (u'========第%d页========' % x)
        handleScroll()
        perser()
        x = x + 1
        sleep(20)


def handleNextPage():
    print (u'====================================下一页======================================')
        # 点击下一页
    driver.find_element_by_css_selector('div.line-around.layout-box.mod-pagination > a.btn.box-col.line-left').click()
    sleep(2)

# 判断元素是否存在
def isPresent():
    temp =1
    try:
        elems = driver.find_elements_by_css_selector('div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
    except:
        temp =0
    return temp

# 解析信息并翻页
def perser():
    try:
        perserElements()
        sleep(10)
        handleNextPage()
    except:
        print (u'=!=!=!=!=!=!=!=!=!=!=发生了意外=!=!=!=!=!=!=!=!=!=!=')
    finally:
        pass

# 解析微博
def perserElements():
    elems = driver.find_elements_by_css_selector('div.card9')
    for elem in elems:
        head_img = elem.find_element_by_css_selector('header > a.mod-media.size-xs > div > img').get_attribute('src')
        print (u'头像地址：' + head_img)
        head_name = elem.find_element_by_css_selector('header > div > a > span').text
        head_time_from = elem.find_element_by_css_selector('header > div > div').text
        print (head_name + u'    ' + head_time_from)
        weibo_detail = elem.find_element_by_class_name('weibo-detail').text
        print (weibo_detail)
        print (u'---------------------------------------')

# 执行滚动加载出全部内容
def handleScroll():

    for i in range (1 , 7 , 1):
        Transfer_Clicks(driver)
        print (u'滚动%d次' % i)
        sleep(2)
    sleep(10)

# 定义一个滚动函数
def Transfer_Clicks(browser):
    try:
        browser.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
        # 这个是执行一段Javascript函数，将网页滚到到网页顶部。
        # browser.execute_script("window.scrollBy(0,5)", "")
        # 向下滚动200个像素，鼠标位置也跟着变了
#         ActionChains(browser).move_by_offset(0,-80).perform()
        # 向上移动鼠标80个像素，水平方向不同
#         ActionChains(browser).click().perform()
        # 鼠标左键点击
#         ActionChains(browser).key_down(Keys.TAB).perform()
        # 模拟tab键的输入
#         ActionChains(browser).send_keys(Keys.ENTER).perform()
        # 模拟输入ENTER键
    except:
        pass
    return "Transfer successfully \n"


if __name__ == '__main__':
    driver = initWork()
    try:
        elems = handleLogin()
        cookie3 = driver.get_cookies()
        for cookie in driver.get_cookies():
            print ("driver.add_cookie({\'name\':\'%s\', \'value\':\'%s\'})" % (cookie['name'], cookie['value']))

        # 将获得cookie的信息打印
        print (cookie3)
        handlePage(elems)
    finally:
        if driver._is_remote:
            driver.close()
            driver.quit()
    pass
