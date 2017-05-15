#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
  'encodedService': 'http%3a%2f%2fi.hdu.edu.cn%2fdcp%2findex.jsp',
  'service': 'http://i.hdu.edu.cn/dcp/index.jsp',
  'serviceName': 'null',
  'loginErrCnt':1,
  'username': '11055221',
  'password': 'cd24b64984fc67ab4a99860753edf4e0',
  'lt': 'LT-63135-jQWT92uX1Ftc59jVume9'
})

# User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36
# 留个坑 估计是headers有什么东西没带上导致

try:
  loginUrl = 'http://cas.hdu.edu.cn/cas/login'
  result = opener.open(loginUrl, postdata)
  cookie.save(ignore_discard=True, ignore_expires=True)
  gradeUrl = 'http://i.hdu.edu.cn/dcp/forward.action?path=/portal/portal&p=wkHomePage'
  r = opener.open(gradeUrl)
  print r.read()
except urllib2.HTTPError, e:
  print e.reason
except urllib2.URLError, e:
  print e.reason