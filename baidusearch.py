#!/usr/bin/env python
#coding:utf8

__author__ = 'xiaokong'

import lxml.html

from config import set_config, get_config
from search import Search

class BaiduSearch(Search):
    """
    BAIDU SEARCH
    """
    def __init__(self):
        pass

    def search(self, query, num):
        """
        Baidu Search
        """
        url = get_config('BAIDU_SEARCH').format(query=query, number=num)
        response = self.query(method='GET', url=url)
        if response is None:
            return False

        result = list()
        html = lxml.html.fromstring(response.content)
        urls = html.cssselect('h3 a[href]')
        for url in urls:
            url = url.get('href')
            response = self.query(method='HEAD', url=url)
            if response is None:
                continue
            if response.status_code == 302:
                result.append(response.headers['location'])
                self.log.info(response.headers['location'])

        return result
