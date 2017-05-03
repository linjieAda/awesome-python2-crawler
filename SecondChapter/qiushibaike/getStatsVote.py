#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 看完数据才知道是降序的的所以需求没用

import urllib
import urllib2
import re
import threading

class QSBKAnalysisVote:

    def __init__(self):
        self.pageCount = 10
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/8hr/page/' + str(pageIndex) + '/?s=4979256'
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = "".join(response.read().decode('utf-8').split())
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u"连接糗事百科失败,错误原因" + e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '页面加载失败...'
            return None
        pattern = re.compile('stats-vote.*?number">(.*?)</i>')
        items = re.findall(pattern, pageCode)
        return items

    def getAllPageItems(self):
        allVotes = []
        for pageIndex in range(1, self.pageCount + 1):
            onePageVotes = self.getPageItems(pageIndex)
            allVotes += (onePageVotes)
            threading._sleep(0.1)
        return allVotes

    def start(self):
        print u"输入要获得的点赞数的页数"
        self.pageCount = int(raw_input())
        allVotes = self.getAllPageItems()
        print allVotes

spider = QSBKAnalysisVote()
spider.start()


