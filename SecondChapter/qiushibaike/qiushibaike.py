#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1.抓取糗事百科热门段子
# 2.过滤带有图片的段子
# 3.实现每按一次回车显示一个段子的发布时间，发布人，段子内容，点赞数
# 正则不能太长否则太影响性能了

import urllib
import urllib2
import re

# page = 1
# url = 'http://www.qiushibaike.com/8hr/page/' + str(page) + '/?s=4979256'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent': user_agent }
# try:
#     request = urllib2.Request(url, headers=headers)
#     response = urllib2.urlopen(request)
#     content = "".join(response.read().decode('utf-8').split())
#     pattern = re.compile('<h2>(.*?)</h2>.*?content"><span>(.*?)</span>.*?(thumb.*?|.*?)number">(.*?)</i>')
#     items = re.findall(pattern, content)
#     for item in items:
#         haveImg = re.search('img', item[2])
#         if not haveImg:
#             print u'提供人：' + item[0]
#             print u'笑话：' + item[1]
#             print u'点赞数：' + item[3]
#             print '\n\n\n'
# except urllib2.URLError, e:
#     if hasattr(e, 'code'):
#         print 'code:' + e.code
#     if hasattr(e, 'reason'):
#         print 'reason: ' + e.reason


class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent': self.user_agent }
        self.stories = []
        self.enable = False
        self.nthStory = 0

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
        pattern = re.compile('<h2>(.*?)</h2>.*?content"><span>(.*?)</span>.*?(thumb.*?|.*?)number">(.*?)</i>')
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            haveImg = re.search('img', item[2])
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, '\n', item[1])
                # item[0]是一个段子的发布者，item[1]是内容，item[3]是点赞数
                pageStories.append([item[0].strip(), text.strip(), item[3].strip()])

        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    def getNthStory(self):
        self.nthStory += 1
        return self.nthStory

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, pageStories):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable = False
                return
            print u"第%s条, 发布人:%s\t赞:%s\n%s\n\n" %(self.getNthStory(),story[0],story[2],story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                del self.stories[0]
                self.getOneStory(pageStories)

spider = QSBK()
spider.start()
