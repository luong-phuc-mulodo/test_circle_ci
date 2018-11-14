import grequests
from bs4 import BeautifulSoup

def run_test(time):
	urls = [
		'https://search.rakuten.co.jp/search/mall/%E3%82%BF%E3%83%B3%E3%83%96%E3%83%A9%E3%83%BC%20%E5%90%8D%E5%85%A5%E3%82%8C',
		'https://search.rakuten.co.jp/search/mall/iphone8plus%20%E5%90%8D%E5%85%A5%E3%82%8C',
		'https://search.rakuten.co.jp/search/mall/galaxy%20s8%20%E3%82%B1%E3%83%BC%E3%82%B9',
		'https://search.rakuten.co.jp/search/mall/galaxy%20s9%20%E3%82%B1%E3%83%BC%E3%82%B9',
		'https://search.rakuten.co.jp/search/mall/galaxy%20s9%2B%20%E3%82%B1%E3%83%BC%E3%82%B9',
		'https://search.rakuten.co.jp/search/mall/huawei%20mate%2010%20pro',
		'https://search.rakuten.co.jp/search/mall/IC%E3%82%AB%E3%83%BC%E3%83%89',
		'https://search.rakuten.co.jp/search/mall/iface%20iphone7',
		'https://search.rakuten.co.jp/search/mall/iface%20iphone8',
		'https://search.rakuten.co.jp/search/mall/iface%20iphonex',
		# 'https://search.rakuten.co.jp/search/mall/iphone8+%E3%82%B1%E3%83%BC%E3%82%B9/?p=1&t=62327836128',
		# 'https://search.rakuten.co.jp/search/mall/iphone7',
		# 'https://search.rakuten.co.jp/search/mall/iphone6',
		# 'https://search.rakuten.co.jp/search/mall/iphone',
		# 'https://search.rakuten.co.jp/search/mall/iphones'
	]

	print('Get data from Rakuten time %s' % time)

	headers = {'user-agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

	rs = (grequests.get(u, headers=headers) for u in urls)
	responses = grequests.map(rs)

	for response in responses:
		if response.status_code != 200:
			raise Exception("Error Response : %s" % response.status_code)
		else:
			get_data(response.text)

def get_data(content):
	soup = BeautifulSoup(content, 'html.parser')
	searchresultitem = soup.select(".searchresultitem .image a[href]")
	if not searchresultitem:
		raise Exception("Not found Data Response")
		return
	for link in searchresultitem:
		print(link.get('href'))


total = 2
for time in range(0,total):
	run_test(time+1)