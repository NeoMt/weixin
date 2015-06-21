#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Ma Teng(matengneo@gmail.com)
#
# ����ҳץȡ����

import urllib2

def get_web_content(url):
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  return response.read()

if __name__=='__main__':
  get_web_content("https://www.baidu.com/")