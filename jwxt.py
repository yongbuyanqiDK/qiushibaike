# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import re

__author__ = 'inso'

class HEBEU:

    def __init__(self):
        self.loginUrl = 'http://219.148.85.172:9080/loginAction.do'
        self.cookies = cookielib.CookieJar()
        self.post_data = urllib.urlencode({
            'zjh':'120730132',
            'mm':'120730132'
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def get_page(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.post_data
        )
        result = self.opener.open(request)
        print result.read().decode('gbk')

hebeu = HEBEU()
hebeu.get_page()
