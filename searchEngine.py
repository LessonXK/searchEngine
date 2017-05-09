#!/usr/bin/env python
#coding:utf8

#author : xiaokong

import re
import sys
import requests
import logging
import random
import time
from magic_google import MagicGoogle

class searchEngine(object):
    
    def __init__(self):
        pass
        
    def setLogger(self, log):
        self.log = log
    
    def googleSearch(self, searchString):
        
        PROXIES = [{'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080'}]

        mg = MagicGoogle(PROXIES)

        n = 0
        while True:
            result = mg.search_url(query='inurl:gov.cn', num=50, start=n)
            print(result)
            n += 50
            for url in result:
                print((n,url))
        
            time.sleep(random.randint(5, 30))
            
    def binSearch(self):
        pass
        
    def baiduSearch(self):
        pass
        
def logger(v=1):
    
    logging.addLevelName(41, 'MESSAGE')
    logger = logging.getLogger('search')
    
    try:
        from logutils.colorize import ColorizingStreamHandler
        handler = ColorizingStreamHandler(sys.stdout)
        handler.level_map[logging.getLevelName('MESSAGE')] = (None, 'red', True)
        handler.level_map[logging.INFO] = (None, 'white', False)
    except ImportError:
        handler = logging.StreamHandler(sys.stdout)
    
    formatter = logging.Formatter("[%(funcName)s] %(message)s", "%Y-%m-%d %H:%M:%S") 
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(v*10)
    
    return logger
    
if __name__ == '__main__':
    
    searchEngine = searchEngine()
    searchEngine.googleSearch("gov.cn")
