# -*-coding: utf-8 -*-
'''
Created by jojo at 2017/8/3
'''
import os
import random
from time import sleep

import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


# 初始化配置
def initWork():
    # 初始化配置根据自己chromedriver位置做相应的修改
    chromedriver = "/Applications/Google Chrome.app/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    brower = webdriver.Chrome(chromedriver)
    return brower


# 执行登录
def handleLogin(brower, username, password):
    # 执行操作的页面地址
    url = 'http://m.weibo.cn/'
    # url = 'http://weibo.com/u/6283668410/home?topnav=1&wvr=6'
    # url = 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'
    brower.set_window_size(480, 760)
    brower.get(url)

    # 目前还没学会cookie怎么用先获取到吧肯定用的到
    # 获得cookie信息
    cookie1 = brower.get_cookies()
    # 将获得cookie的信息打印
#    print('11111111')
#    print(cookie1)

    # 下面就开始在打开的页面中自动执行操作了
    # 根据xpath获取登录按钮

    elem = brower.find_element_by_xpath("/html/body/div[1]/div/a[2]");
    # 发送确认按钮跳转到登录页面
    elem.send_keys(Keys.ENTER)

    # 休眠两秒钟后执行填写用户名和密码操作
    sleep(2)
    elem = brower.find_element_by_xpath("//*[@id='loginName']");

    elem.send_keys(username)
    elem = brower.find_element_by_xpath("//*[@id='loginPassword']");
    elem.send_keys(password)
    elem = brower.find_element_by_xpath("//*[@id='loginAction']");
    elem.send_keys(Keys.ENTER)

    cookie2 = brower.get_cookies()
    # 将获得cookie的信息打印
#    print('222222222')
#    print(cookie2)

    # 判断是否登录成功
    if cookie1 == cookie2:
        print(u' (￣y▽￣)╭可能登录失败了手动登录一下吧')
        sleep(30)
    else:
        wait = WebDriverWait(brower, 30)
        elems = wait.until(lambda brower: brower.find_elements_by_css_selector(
            'div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option'))

    # 获取信息
    while 1:  # 循环条件为1必定成立
        result = isPresent()
        print(u'判断页面1成功 0失败  结果是=%d' % result)
        if result == 1:
            elems = brower.find_elements_by_css_selector(
                'div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
            print(elems)
            return elems
            break
        else:
            print(u'页面还没加载出来呢')
            sleep(20)


# 开始解析页面
def handlePage(elems):
    x = 1
    for page in elems:
        print(u'========第%d页========' % x)
        handleScroll()
        perser()
        x = x + 1
        sleep(20)


def handleNextPage():
    print(u'====================================下一页======================================')
    # 点击下一页
    driver1.find_element_by_css_selector('div.line-around.layout-box.mod-pagination > a.btn.box-col.line-left').click()
    sleep(2)


# 判断元素是否存在
def isPresent():
    temp = 1
    try:
        elems = driver1.find_elements_by_css_selector(
            'div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
    except:
        temp = 0
    return temp


# 解析信息并翻页
def perser():
    try:
        perserElements()
        sleep(10)
    #        handleNextPage()
    except:
        print(u'=!=!=!=!=!=!=!=!=!=!=发生了意外=!=!=!=!=!=!=!=!=!=!=')
    finally:
        pass


# 解析微博
def perserElements():
    elems = driver1.find_elements_by_css_selector('div.card9')
    i = 0
    for elem in elems:
        i = i + 1
        head_img = elem.find_element_by_css_selector('header > a.mod-media.size-xs > div > img').get_attribute('src')
        print(u'头像地址：' + head_img)
        head_name = elem.find_element_by_css_selector('header > div > a > span').text
        head_time_from = elem.find_element_by_css_selector('header > div > div').text
        print(head_name + u'    ' + head_time_from)
        weibo_detail = elem.find_element_by_class_name('weibo-detail').text
        print(weibo_detail)
        print(u'---------------------------------------')
        print('转发微博')
    #        driver1.find_element_by_css_selector(
    #           'div.line-around.layout-box.mod-pagination > a.btn.box-col.line-left').click()


# 执行滚动加载出全部内容
def handleScroll():
    for i in range(1, 7, 1):
        Transfer_Clicks(driver1)
        print(u'滚动%d次' % i)
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


def repost(browser):
    idSet = ['4136071652551986', '4135937334320864']
    commentSet = ['#邓伦#邓伦最帅，爱你😍@邓伦', '#邓伦#伦哥注意防暑哦😁@邓伦', '#邓伦# ❤❤️❤️❤❤️❤️伦伦伦，永远爱你❤❤️❤️❤❤️❤️@邓伦']
    print(commentSet)
    j = random.randint(0,2)
    print(j)
    i = 0
    while 1:
        for id in idSet:
            i = i + 1
            tweet_url = "https://m.weibo.cn/compose/comment?id=%s" % (id)
            print(id)
            browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
            sleep(5)
            #
            browser.get(tweet_url)
            sleep(5)
            #
            text = browser.find_element_by_tag_name('textarea')
            print(commentSet[j])
            text.send_keys(commentSet[j])
            sleep(5)
            send = browser.find_element_by_class_name('m-send-btn')
            send.click()
            sleep(5)
            browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
            sleep(1)
            print(i)
def comment(browser):
    id_set = ['4136954880155475', '4135937334320864']
    comment_set = [' 邓伦最帅，爱你！', ' 伦哥注意防暑哦！', ' 伦伦伦，永远爱你！', ' 邓伦我爱你!']
    while 1:
        i = 0
        j = 0
        with open("poem2", 'r') as file:
            while i < 30:
                for id in id_set:
                    i = i + 1
                    tweet_url = "https://m.weibo.cn/compose/comment?id=%s" % id
                    print(id)
                    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
                    browser.get(tweet_url)
                    sleep(5)
                    #
                    text = browser.find_element_by_tag_name('textarea')
                    line = file.readline().strip('\n')
                    if not line:
                        break
                    text.send_keys(comment_set[j])
                    text.send_keys("送你二十四首情诗：")
                    text.send_keys(line)
                    print(file.readline())
                    j = j + 1
                    if j == 4:
                        j = 0
                    sleep(2)
                    send = browser.find_element_by_class_name('m-send-btn')
                    send.click()
                    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                    sleep(1)
                    print(i)
        sleep(4*60*60)
if __name__ == '__main__':
    # 定义自己的用户名密码
    usrname = sys.argv[1]
 #   usrname = "13261969620" #'邓伦初恋'
    #username1 = ["14719861661", "14799390896", "14799391989", "1347712144", "17138955984", "14799390896", ]
    pwd = sys.argv[2]
 #   pwd = "DENGLUNSHIWODE" #"abc12345"
    driver1 = initWork()
   # driver2 = initWork()
    try:
        elems1 = handleLogin(driver1, usrname, pwd)
    #    elems2 = handleLogin(driver2, username1[2], password1)
#        cookie3 = driver1.get_cookies()
#        for cookie in driver1.get_cookies():
#            print("driver1.add_cookie({\'name\':\'%s\', \'value\':\'%s\'})" % (cookie['name'], cookie['value']))

        # 将获得cookie的信息打印
#        print('33333333')
#        print(cookie3)
        # handlePage(elems)
        comment(driver1)
#        repost(driver1)
    finally:
        if driver1._is_remote:
            driver1.close()
            driver1.quit()
    pass
