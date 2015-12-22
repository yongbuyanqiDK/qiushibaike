# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import re

__author__ = 'inso'


def get_page():
    loginUrl = 'http://219.148.85.172:9080/loginAction.do'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    post_data = urllib.urlencode({
        'zjh':'120730132',
        'mm':'120730132'
    })
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    request = urllib2.Request(
        url = loginUrl,
        data = post_data,
        headers = headers
    )
    result = opener.open(request)
    cookie.save(ignore_discard=True, ignore_expires=True)
    grade_url = 'http://219.148.85.172:9080/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=3842'
    result = opener.open(grade_url)
    print result.read().decode('gbk')

get_page()
