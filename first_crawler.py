#!/usr/bin/env python
# -*- coding: utf-8
# 第一个爬虫

import urllib2
res = urllib2.urlopen("http://www.baidu.com")
ret = res.read()
print(ret)