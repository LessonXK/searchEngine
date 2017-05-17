#!/usr/bin/env python
#coding:utf8

__author__ = 'xiaokong'

import requests
import chardet
import logging
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class BaiduSearch():
    """
    BAIDU SEARCH
    """
    def __init__(self):
        pass

    def __search_page(self, query, num, pause=2):
        """
        Baidu Search by Page Number
        """
        time.sleep(pause)
        headers = {'user-agent': self.get_random_user_agent()}
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url=url,
                                    headers=headers,
                                    timeout=30,
                                    verify=False
                                    allow_redirects=False)
            charset = chardet.detect(r.content)
            content = r.content.decode(charset['encoding'])
            return content
        except Exception as e:
            logging.exception(e)
            return None

    def search(self, query, num):
        """
        Baidu Search
        """
        content = self.__search_page(query, num)