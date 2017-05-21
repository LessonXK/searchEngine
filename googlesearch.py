#!/usr/bin/env python
#coding:utf8

__author__ = 'xiaokong'

import lxml.html
import os
import sys
import urlparse
from config import set_config, get_config
from search import Search
if sys.version_info[0] > 2:
    from urllib.parse import quote_plus, urlparse, parse_qs
else:
    from urllib import quote_plus
    from urlparse import urlparse, parse_qs

class GoogleSearch(Search):
    """
    Google SEARCH
    """
    def __init__(self):
        pass

    def search(self, query, num, start):
        """
        Google Search
        """
        url = get_config('GOOGLE_SEARCH').format(domain=self.get_random_domain(),
                                                query=query, num=num, 
                                                start=start)
        response = self.query(method='GET', url=url)
        if response is None:
            return False
        
        result = list()
        html = lxml.html.fromstring(response.content)
        links = html.cssselect('h3.r a[href]')

        for link in links:
            link = link.get('href')
            url = self.__filter_link(link)
            if url is not None:
                result.append(url)
                self.log.info(url)

        return result

    def __filter_link(self, link):
        """
        Returns None if the link doesn't yield a valid result.
        Token from https://github.com/MarioVilas/google
        :return: a valid result
        """
        try:
            # Valid results are absolute URLs not pointing to a Google domain
            # like images.google.com or googleusercontent.com
            o = urlparse(link, 'http')
            print o
            if o.netloc:
                return link
            # Decode hidden URLs.
            if link.startswith('/url?'):
                link = parse_qs(o.query)['q'][0]
                # Valid results are absolute URLs not pointing to a Google domain
                # like images.google.com or googleusercontent.com
                o = urlparse(link, 'http')
                if o.netloc:
                    return link
        # Otherwise, or on error, return None.
        except Exception as e:
            self.log.exception(e)
            return None


if __name__ == '__main__':
    google = GoogleSearch()
    google.search('inurl:gov.cn', 10,0)
