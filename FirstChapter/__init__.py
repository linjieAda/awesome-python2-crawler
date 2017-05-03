#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

# post
v = {"username":"shumeilinjie@163.com","password":"jie355116lin>" }
data = urllib.urlencode(v)
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = urllib2.Request(url, data)
try:
    r = urllib2.urlopen(request)
    print r.read() + '' + r.geturl()
except urllib2.HTTPError, e:
    print e.reason
except urllib2.URLError, e:
    print e.reason




