# -*-coding:utf-8-*-
import random
import re
from urllib.parse import urlparse
from urllib.request import urlopen

import datetime
from bs4 import BeautifulSoup
from urllib import request

random.seed(datetime.datetime.now())
deep = 1000

def getExternalLink(bsObj, excludeUrl):
    externalLink = []
    for link in bsObj.findAll('a',href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLink:
                externalLink.append(link.attrs['href'])
    return externalLink


def getInternalLink(bsObj, includeUrl):
    internalLink = []
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    for link in bsObj.findAll('a', href=re.compile("^(/|.*" + includeUrl + ")")):
        if link is not None:
            if link.attrs['href'] not in internalLink:
                if link.attrs['href'].startswith("/"):
                    internalLink.append(includeUrl + link.attrs['href'])
                else:
                    internalLink.append(link.attrs['href'])
    return internalLink


def getRandomExternalLink(startingPage):
    proxy = request.ProxyHandler({"http": "http://lingjiefan:Zurich@1234@10.242.192.32:8080"})
    opener = request.build_opener(proxy)
    request.install_opener(opener)
    res = urlopen(startingPage)
    bsObj = BeautifulSoup(res,'lxml')
    externalLinks = getExternalLink(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks == 0):
        print("no external link, look around a new beging site")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLink(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def splitaddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

allExternalLinks=set()
allInternalLinks=set()

def getAllExternalLink(siteUrl,deep):
    proxy = request.ProxyHandler({"http": "http://lingjiefan:Zurich@1234@10.242.192.32:8080"})
    opener = request.build_opener(proxy)
    request.install_opener(opener)
    res = urlopen(siteUrl)
    bsObj=BeautifulSoup(res,'lxml')
    internalLink = getInternalLink(bsObj,splitaddress(siteUrl)[0])
    externalLink = getExternalLink(bsObj,splitaddress(siteUrl)[0])
    for link in internalLink:
        if link not in allInternalLinks:
            allInternalLinks.add(link)
            # print(link)
    for link in externalLink:
        if link not in allExternalLinks:
            allExternalLinks.add(link)
            print(link)
    deep = deep +1

str = "http://www.163.com"
getAllExternalLink(str)


