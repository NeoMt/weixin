#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Ma Teng(matengneo@gmail.com)
#
# 从搜狗微信搜索页面抓取每日内容
# 输出内容:
#  抓取时间 文章标题 阅读量 文章URL 公众号名称

from common.web_getter import get_web_content

CHANNEL_TYPE = "pc_2"

FIRST_PAGE_URL = "http://weixin.sogou.com/pcindex/pc/%s/%s.html" % (CHANNEL_TYPE, CHANNEL_TYPE)
LOAD_PAGE_URL = "http://weixin.sogou.com/pcindex/pc/%s/{load_page_num}.html" % CHANNEL_TYPE

if __name__=='__main__':
  print get_web_content(LOAD_PAGE_URL.replace("{load_page_num}", str(1)))