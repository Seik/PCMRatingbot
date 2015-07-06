#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lxml.html
import re

def wordcount(text):
    # Find all non-whitespace patterns.
    list = re.findall('(\S+)', text)
    # Return length of resulting list.
    return len(list)
	
text = raw_input('¿Que juego quieres buscar?')
count = wordcount(text)
if count == 0:
    base_url = 'http://www.pcmrating.com/games?utf8=%E2%9C%93&q%5Btitle_cont%5D=' + text + '&commit=Search'
elif count >= 1:
    textx = text.replace(':', '%3A')  #If there is any : it'll be changed
    textt = textx.replace(' ', '+') #Replace spaces
    base_url = 'http://www.pcmrating.com/games?utf8=%E2%9C%93&q%5Btitle_cont%5D=' + textt + '&commit=Search'
content = lxml.html.parse(base_url)
links = content.xpath('//div[@class="row game even"][1]/div[@class="col-xs-2 game-name"][1]/a/@href[1]')[1] #Get the first href query
nurl = 'http://www.pcmrating.com/' + links
print nurl