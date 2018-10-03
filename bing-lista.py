#!/usr/bin/env python
import requests
import urlparse
import argparse
import re
import os
import os
import time
import subprocess 



os.system('clear')


bing_url = 'http://www.bing.com/search?q=ip%3a'
urls_array = []
count = 0
req2 = ''

ip = raw_input('Introduce el archivo con la lista de ips: ')
archivo=open(ip, "r")

lista_objetivos=[]
linea=archivo.readline()
while linea != '':
	lista_objetivos.append(linea[:-1])
	linea=archivo.readline()

	       
while  count < 10 :
	for objetivo in lista_objetivos:
		url = bing_url+objetivo+'&first='+str(count)
		req = requests.get(url, timeout = 3, stream = True)
		req2 += str(req.content)
		count = count+1

        
		hrefs = re.findall('href=[\'"]?([^\'" >]+)', req2)
		for href in hrefs:
			if 'http' in href:
				if 'microsoft' not in href:
					parse = urlparse.urlparse(href)
					urls_array.append(parse.netloc)
				


lista_nueva = []
for url in urls_array:
	print 'url: '+url
	if url not in lista_nueva:
		lista_nueva.append(url)
		file=open("listahost.txt","a")
		file.write(url+"\n")
		file.close
	
