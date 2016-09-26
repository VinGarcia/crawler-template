#!/usr/bin/python
# coding: utf-8

# To use this project execute it with:
# scrapy runspider stack_spider.py

import scrapy
import json
import codecs
import re

from functools import partial

# Some useful functions:
from os.path import isfile, isdir, splitext, dirname, exists, basename
from os import makedirs, listdir, rmdir

# Use this to extract inner html content:
innerHtml = re.compile('\A<[^>]*>(.*)</[^>]*>\Z', re.DOTALL)
def getInner(html):
    return innerHtml.match(html).group(1)

class Crawler(scrapy.Spider):
    name = "crawler"

    # Save your data here:
    my_data = []

    # Put your startin url here:
    start_urls = [
        "http://www.physicsdemos.com/alpha/index.php/search-results/"
      ]

    # If you need to run some code before the crawler starts
    # put it inside this function:
    def __init__(self):
        pass
 
    # This function will parse your `start_urls`
    def parse(self, resp):

        # Use resp.css() or resp.xpath() to extract data from the web page:
        selector_list = resp.css('...');

        # Use extract to extract all the results of the list:
        results = selector_list.extract()

        # Use extract_first to extract a single result:
        single_result = selector_list.extract()

        # Save your data on `self.my_data`
        self.my_data.append(my_data)

        # To parse another url use the yield command like this:
        yield scrapy.Request(
            my_url,
            callback=partial(self.parse_my_url, 'argument1', 'argument2')
          )

        # Please note that parse_my_url function is defined below, you can
        # write your own code there, or even create other `parse` functions.

    def parse_my_url(self, arg1, arg2, resp):
        pass

    # To download data be it a image, video or an
    # html page, just Request it and set download
    # as a callback with:
    #
    # - yield scrapy.Request('url', patial(self.download, "path/to/file")
    #
    def download(self, path, resp): 
        print()
        print("  Downloading %s!" % path)
        print()
        # Make sure path exists: 
        if not isdir(dirname(path)): 
            makedirs(dirname(path))        
        with open(path, 'wb') as file: 
            file.write(resp.body) 

    # Save the data before quit:
    def closed(self, reason):

        # To write utf-8 files do as described bellow:

        # If using Python2
        with codecs.open('data/Posts.xml', 'w', 'utf-8') as file:

        # If using Python3:
        with open('data/Posts.xml', 'wb') as file:
            # Using JSON:
            # text = json.dumps(
            #     self.pages,
            #     indent = 2,
            #     sort_keys=True).decode('raw_unicode_escape')

            # Using lxml:
            xml_text = etree.tostring(
                self.posts, encoding='utf-8', pretty_print=True, xml_declaration=True)
            file.write(xml_text)
