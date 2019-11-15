import requests
from datetime import datetime

def get_proxies(request="getproxies", proxytype="http", timeout="10000", country="all", ssl="all", anonymity="all"):
    """
    returns a list of proxies as strings ['host1:port1', 'host2:port2'] or None if proxies aren't found.
    proxytype - http, socks4, and socks5
    timeout - time in ms
    country - all, US, CA, AU, DE, FR, GB, GE, IN, IT, JP, MX, PH, PK, US, RU, SG, and more
    ssl - all, yes, and no
    anonymity - all, elite, anonymous, and transparent
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
    if(len(proxy_list) > 0):
        return proxy_list
    else:
        return None

def import_proxies(request="getproxies", proxytype="http", timeout="10000", country="all", ssl="all", anonymity="all"):
    """
    Imports all proxies into a text file - 'proxies/proxies.txt'
    Returns True on completion and None if proxies aren't found.
    """
    proxies = get_proxies(request=request, proxytype=proxytype, timeout=timeout, country=country, ssl=ssl, anonymity=anonymity)
    proxy_file = open("./proxies/proxies.txt", "w+")
    if(len(proxies) < 1):
        return None
    for proxy in proxies:
        if(len(proxy)> 4):
            proxy_file.write(proxy+"\n")
    return True