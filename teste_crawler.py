from urllib.request import urlopen,build_opener
from bs4 import BeautifulSoup
opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
site = ["https://br.gearbest.com/xiaomi-redmi-5-_gear/","https://www.tomtop.com/pt/search/xiaomi-redmi-5.html"]
products = ["li.gbGoodsItem","li.productClass"]

nomes = ["a.gbGoodsItem_title", "a.productTitle"]

precos = ["p.gbGoodsItem_price", "p.productPrice"]
i = -1
for url in site:
	i += 1
	print("indo no site :", url)
	request = opener.open(url, timeout=5)
	teste = BeautifulSoup(request.read(), "html.parser")
	for x in teste.select(products[i]):
		nome = x.select(nomes[i])[0]
		preco = x.select(precos[i])[0]
		print(nome.text , " = " , preco.text)