# -*-coding: utf-8 -*-
'''
Created by jojo at 2017/8/3
'''
import os
import sys
import time
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    sleep(2)
    elem = brower.find_element_by_xpath("//*[@id='loginAction']");
    elem.send_keys(Keys.ENTER)

    cookie2 = brower.get_cookies()
    # 将获得cookie的信息打印
    #    print('222222222')
    print(cookie2)

    # 判断是否登录成功
    if cookie1 == cookie2:
        print(' (￣y▽￣)╭可能登录失败了手动登录一下吧')
        sleep(30)
    else:
        wait = WebDriverWait(brower, 30)
        elems = wait.until(lambda brower: brower.find_elements_by_css_selector(
            'div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option'))
    cookie4 = brower.get_cookies()
    # getDomain()
    # https://m.weibo.cn/security?#sms
    # 获取信息
    while 1:  # 循环条件为1必定成立
        result = isPresent()
        print('判断页面1成功 0失败  结果是=%d' % result)
        if result == 1:
            elems = brower.find_elements_by_css_selector(
                'div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
            if elems:
                print(elems)
                return elems
            else:
                with open('/Users/jojo/PycharmProjects/denglun/dl520'
                          '/sinaAccount.file/inactive.txt', 'a+') as account:
                    account.write(username + '----' + password + '\n')
                print('伦哥：呜呜呜，%s----%s 这个号不能用啦 ' % (username, password))
                sleep(20)
                brower.close()
                brower.quit()  # 说明登陆失败，号需要激活，退出浏览器
            break
        else:
            print('页面还没加载出来呢')
            sleep(20)

# 判断元素是否存在
def isPresent():
    temp = 1
    try:
        elems = driver1.find_elements_by_css_selector(
            'div.line-around.layout-box.mod-pagination > a:nth-child(2) > div > select > option')
    except:
        temp = 0
    return temp
#'4136242172004022',1
#'4136242033629515',2
def repost(browser):
#    idSet = ['4136242172004022', '4136242033629515', '4137563058884003']
    idSet = ['4137856689393664', '4137856425867331', '4137856291796034']
    result = EC.alert_is_present()(browser)

    flag = 1
    count = 0
    total_num = 0
    while 1:
        if result:
            if flag:
                print('伦哥：号被锁啦，别灰心，继续努力')
                sleep(4 * 60 * 60)
            else:
                print('伦哥：解封失败了，别灰心，继续努力')
                sleep(4 * 60 * 60)
        else:
            count = count + 1
            sum_num = 0
            print('伦哥：好棒！第%d次运行了' % count)
            i = 0
            print(time.strftime('运行时间：%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            with open("poem2", 'r') as file:
                while i < 80:
                    if result:
                        break
                    for id in idSet:
                        if result:
                            break
                        i = i + 1
                        tweet_url = "https://m.weibo.cn/compose/repost?id=%s" % id
                        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
                        browser.get(tweet_url)
                        sleep(10)
                        text = browser.find_element_by_tag_name('textarea')
                        line = file.readline().strip('\n')
                        if not line:
                            break
                        text.send_keys(line)
                        text.send_keys('[心][心][心]邓伦我爱你[爱你][爱你][爱你]')
                        sleep(10)
                        send = browser.find_element_by_class_name('m-send-btn')
                        send.click()
                        sleep(10)
                        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                        sleep(1)
                        print(i)
                        result = EC.alert_is_present()(browser)
                        print(result)
                        if result:
                            break
                print('冻结条数：%d' % i)
                sum_num = sum_num + i
        total_num = total_num + sum_num
        print('伦哥说君宝这次伦了%d条博，一共伦了%d条博了，还要加油哟' % (sum_num, total_num))
        print(time.strftime('冻结时间：%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        sleep(4 * 60 * 60)
        print(time.strftime('解封时间：%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    # 定义自己的用户名密码
    usrname = sys.argv[1]
    # usrname = 17152569488
    # pwd = 'youxia5533'
    # usrname = "iacen@icloud.com"
    pwd = sys.argv[2]
    # pwd = "abc12123"
    driver1 = initWork()
    sleep(3)
    #    driver2 = initWork()
    try:
        elems1 = handleLogin(driver1, usrname, pwd)
        #        elems2 = handleLogin(driver2, username1[1], password1)
        cookie3 = driver1.get_cookies()
        repost(driver1)
    finally:
        if driver1._is_remote:
            driver1.close()
            driver1.quit()
    pass
