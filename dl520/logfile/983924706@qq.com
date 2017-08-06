判断页面1成功 0失败  结果是=1
[<selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-1")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-2")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-3")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-4")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-5")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-6")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-7")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-8")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-9")>, <selenium.webdriver.remote.webelement.WebElement (session="6f1945f5154dcf2f2cfa111900e895ef", element="0.927858774365939-10")>]
伦哥：好棒！第1次运行了
运行时间：2017-08-06 00:57:22
Traceback (most recent call last):
  File "test_repost_new.py", line 245, in <module>
    cookie3 = driver1.get_cookies()
  File "test_repost_new.py", line 204, in repost
    for id in idSet:
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 409, in find_element_by_tag_name
    return self.find_element(by=By.TAG_NAME, value=name)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 791, in find_element
    'value': value})['value']
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 256, in execute
    self.error_handler.check_response(response)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"tag name","selector":"textarea"}
  (Session info: chrome=60.0.3112.90)
  (Driver info: chromedriver=2.31.488774 (7e15618d1bf16df8bf0ecf2914ed1964a387ba0b),platform=Mac OS X 10.12.6 x86_64)

