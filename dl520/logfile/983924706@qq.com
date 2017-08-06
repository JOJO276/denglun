[{'httpOnly': True, 'name': '_T_WM', 'expiry': 1504618616.591627, 'secure': False, 'domain': '.weibo.cn', 'path': '/', 'value': '292b7b5b964fb2336d6eeef423b6ec8e'}, {'httpOnly': True, 'name': 'SCF', 'expiry': 1817386621.235859, 'secure': False, 'domain': '.weibo.cn', 'path': '/', 'value': 'AiGEO9ip0pR6MhKHtJAfstk7fBe2PvfLvnw3jjsEEJg3YJCn3lD5PHAvnSVUDo1v9VKQYJ0_m1WRn-ftYAL5QNg.'}, {'httpOnly': False, 'name': 'SSOLoginState', 'secure': False, 'domain': '.weibo.cn', 'path': '/', 'value': '1502026621'}, {'httpOnly': False, 'name': 'M_WEIBOCN_PARAMS', 'expiry': 1502027221.505087, 'secure': False, 'domain': '.weibo.cn', 'path': '/', 'value': 'uicode%3D20000174'}, {'httpOnly': False, 'name': 'SUHB', 'expiry': 1533562621.33, 'secure': False, 'domain': '.weibo.cn', 'path': '/', 'value': '02M_XF6hjJL108'}, {'httpOnly': True, 'name': 'SUB', 'expiry': 1533562586.328916, 'secure': False, 'domain': '.weibo.cn', 'path': '/', 'value': '_2A250g2sKDeThGeVM4lcU8inPzjmIHXVXjHVCrDV6PUJbkdAKLXDtkW1OSCKecis3UbSRUf6sBZPfGtVdMA..'}]
判断页面1成功 0失败  结果是=1
[<selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-1")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-2")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-3")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-4")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-5")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-6")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-7")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-8")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-9")>, <selenium.webdriver.remote.webelement.WebElement (session="6b12e9ee409db1eda3593052d96afb18", element="0.2521370278179087-10")>]
伦哥：好棒！第1次运行了
运行时间：2017-08-06 21:37:02
Traceback (most recent call last):
  File "my_repost.py", line 192, in <module>
    repost(driver1)
  File "my_repost.py", line 161, in repost
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 409, in find_element_by_tag_name
    return self.find_element(by=By.TAG_NAME, value=name)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 791, in find_element
    'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 256, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: chrome not reachable
  (Session info: chrome=60.0.3112.90)
  (Driver info: chromedriver=2.31.488774 (7e15618d1bf16df8bf0ecf2914ed1964a387ba0b),platform=Mac OS X 10.12.6 x86_64)

