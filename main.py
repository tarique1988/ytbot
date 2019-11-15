"""
Created by: Tarique Ali Mirza <sajmtam@gmail.com>
Date started: November 15, 2019
Version: 0
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options, FirefoxProfile
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import os

def main():
    # The code goes here!
    get_proxies()
    initialize_app()


def initialize_app():
    return None

def get_proxies(request="getproxies", proxytype="http", timeout="10000", country="all", ssl="all", anonymity="all"):
    """
    Method: GET
    Sample: https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
    request - request proxies (default: getproxies)
    proxytype - http, https, socks4, and socks5 (default: http)
    timeout - time in ms (default: 10000)
    country - country code e.g US, IN, RU etc. (default: all)
    ssl - not sure what that means (default: all)
    anonymity - type of anonymity (default: all)
    """
    request = request
    proxytype = proxytype
    timeout = timeout
    country = country
    ssl = ssl
    anonymity = anonymity
    url = "https://api.proxyscrape.com/"+ \
        "?request="+request+ \
        "&proxytype="+proxytype+ \
        "&timeout="+timeout+ \
        "&country="+country+ \
        "&ssl="+ssl+ \
        "&anonymity="+anonymity
    r = requests.get(url)
    proxy_list = r.text
    proxies = proxy_list.split("\r\n")
    proxy_file = open("./proxies.txt", "w+")
    for proxy in proxies:
        if(len(proxy)> 4):
            proxy_file.write(proxy+"\n")
    return None

def create_window():
    return None

if __name__ == '__main__':
    main()