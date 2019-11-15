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
    get_proxies(proxytype="http", ssl="yes", anonymity="elite")
    initialize_app()


def initialize_app():
    return None

def get_proxies(request="getproxies", proxytype="http", timeout="10000", country="all", ssl="all", anonymity="all"):
    """
    Method: GET
    Sample: https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all
    request - request proxies (default: getproxies)
    proxytype - http, socks4, and socks5 (default: http)
    timeout - time in ms (default: 10000)
    country - all, US, CA, AU, DE, FR, GB, GE, IN, IT, JP, MX, PH, PK, US, RU, SG  (default: all)
    ssl - all, yes, and no (default: all)
    anonymity - elite, anonymous, and transparent (default: all)
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