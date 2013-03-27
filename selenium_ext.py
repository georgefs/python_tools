from urlparse import urlparse
import urllib2
import zlib


def urlopen_by_selenium(url, driver, data=""):
    #use selenium webdriver cookie open url
    domain = urlparse(url).hostname

    cookies = driver.get_cookies()
    cookie = "".join(["{0}={1}; ".format(cookie.get('name'),cookie.get('value')) for cookie in cookies])
    
    headers = {
    'Connection':'keep-alive',
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4',
    'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':' deflate,sdch',
    'Accept-Language':' zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
    'Accept-Charset':' Big5,utf-8;q=0.7,*;q=0.3',
    }

    headers['Host'], headers['Origin'], headers['Referer'] = domain, domain, domain
    headers['Cookie'] = cookie


    req=urllib2.Request(url, data, headers )
    return urllib2.urlopen(req)



def extension_cookie_time(driver, cookie, total_seconds):
    try:
        cookie['expiry'] = cookie.get('expiry') + total_seconds
        driver.add_cookie(cookie)
    except TypeError, e:
        pass

def extension_driver_cookies_time(driver, total_seconds):
    cookies = driver.get_cookies()

    for cookie in cookies:
        extension_cookie_time(driver, cookie, total_seconds)


import time
def wait_alert(driver, timeout=10, poll_frequency=0.5):
    count = int(timeout / poll_frequency) + 1
    alert = driver.switch_to_alert()

    for i in xrange(count):
        try:
            alert.text
            return alert
        except Exception, e:
            pass
        finally:
            time.sleep(poll_frequency)

    raise Exception('timeout')




def is_on_load( driver ):
    try:
        text = driver.find_element_by_css_selector('html').text
        return True
    except Exception,e:
        return False


