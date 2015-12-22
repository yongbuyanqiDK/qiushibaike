# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import re

__author__ = 'inso'

class HEBEU:

    def __init__(self):
        self.loginUrl = 'http://219.148.85.172:9080/loginAction.do'
        self.gradeUrl = 'http://219.148.85.172:9080/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=3842'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': user_agent}
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'zjh':'120730132',
            'mm':'120730132'
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    def get_page(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata,
            headers = self.headers
        )
        result = self.opener.open(request)
        result = self.opener.open(self.gradeUrl)
        return result.read().decode('gbk')

    def get_grades(self):
        page = self.get_page()
        myItems = re.findall('<tr>.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<td.*?<p.*?>(.*?)</p>.*?</tr>',page,re.S)
        for item in myItems:
            print item.encode('gbk')

hebeu = HEBEU()
hebeu.get_grades()












