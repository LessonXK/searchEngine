#!/usr/bin/env python
#coding:utf8

__author__ = 'xiaokong'

import requests
import time
import chardet
import random
import os
from config import set_config, get_config
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from log import logger

class Search(object):

    def __new__(cls, *args, **kwargs):
        self = super(Search, cls).__new__(cls, *args, **kwargs)
        self.log = logger(1, self.__module__)
        return self

    def query(self, method, url, data=None, cookie=None, headers={}, params=None, allow_redirects=False, files=None):
        """
        query url
        """
        headers['User-Agent'] = self.get_random_user_agent()
        proxies = get_config('proxy') if get_config('proxy') else None
        pause = get_config('pause') if get_config('pause') else 0
        if cookie:
            headers['Cookie'] = cookie
        try: 
            self.log.debug(url)
            time.sleep(pause)
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.request(method=method, 
                                        url=url,
                                        headers=headers, 
                                        proxies=proxies,
                                        files=files,
                                        data=data, 
                                        params=params,
                                        timeout=30,
                                        verify=False,
                                        allow_redirects=allow_redirects)
        except Exception as e:
            self.log.error('error: '+str(e))
            return None

        return response

    def get_random_user_agent(self):
        """
        Get a random user agent string.
        :return: Random user agent string.
        """
        return random.choice(self.__get_data('user_agents.txt', 'USER_AGENT'))

    def __get_data(self, filename, default=''):
        """
        Get data from a file
        :param filename: filename
        :param default: default value
        :return: data
        """
        root_folder = os.path.dirname(__file__)
        user_agents_file = os.path.join(
            os.path.join(root_folder, 'data'), filename)
        try:
            with open(user_agents_file) as fp:
                data = [_.strip() for _ in fp.readlines()]
        except:
            data = [default]
        return data

    def get_random_domain(self):
        """
        Get a random user agent string.
        :return: Random user agent string.
        """
        domain = random.choice(self.__get_data('all_domain.txt', get_config('GOOGLE_DOMAIN')))
        if domain in get_config('BLACK_DOMAIN'):
            self.get_random_domain()
        else:
            return domain