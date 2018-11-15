import grequests
from bs4 import BeautifulSoup
import simplejson
import time
import random

def run_test(times):
	links = [
		'https://www.lazada.vn/op-lung-bao-da-dien-thoai/apple/?spm=a2o4n.searchlistbrand.card.4.1e152e4b3OnFT4&item_id=150511785&from=onesearch_brand_69',
		'https://www.lazada.vn/trang-diem/?spm=a2o4n.home.cate_4.1.20566afeMlj0C5',
		'https://www.lazada.vn/co-va-cac-dung-cu-trang-diem/?spm=a2o4n.searchlistcategory.card.2.7c9e3876OMXnQ7&item_id=143041134&from=onesearch_category_4611',
		'https://www.lazada.vn/chau-tam-phu-kien/?spm=a2o4n.home.cate_5_5.4.baef6afe1fHz0q',
		'https://www.lazada.vn/cac-loai-do-uong/?spm=a2o4n.searchlistcategory.cate_6.3.59a94b71Ud3Ynn'
	]

	urls = []

	# Run only one url
	# i = random.randint(0, 14)
	# urls.append("%s/?t=%s" % (links[i],int(time.time())))

	# Run multi urls
	for link in links:
		urls.append("%s/?t=%s" % (link,int(time.time())))

	print(urls)
	print('Get data from Rakuten time %s' % times)

	headers = {'user-agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

	rs = (grequests.get(u, headers=headers) for u in urls)
	responses = grequests.map(rs)

	i = 0
	for response in responses:
		if response.status_code != 200:
			raise Exception("Error Response : %s for url : %s" % (response.status_code,urls[i]))
		else:
			get_data(response.text)
		i = i + 1

def get_data(content):
	soup = BeautifulSoup(content, 'html.parser')
	searchresultitem = soup.find_all("script")
	for item in searchresultitem:
		if str(item).find('window.pageData') > 0:
			content = item.string.replace("window.pageData=", "")
			data = simplejson.loads(content)
			for pro in data['mods']['listItems']:
				print(pro['productUrl'])
			return


total = 100
for times in range(0,total):
	run_test(times+1)
	# time.sleep(3)
	# print('Run again after 3 seconds')