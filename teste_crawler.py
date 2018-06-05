from urllib.request import urlopen,build_opener
from bs4 import BeautifulSoup
import classes
s = []
opener = build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
i = -1

sites = classes.sites()
for url in s:
	i += 1
	print("indo no site :", url)
	try:
		request = opener.open(url, timeout=5)
	except Exception as e:
		print("Time out!")
	else:
		teste = BeautifulSoup(request.read(), "html.parser")
		for x in teste.select(products[i]):
			nome = x.select(nomes[i])[0]
			preco = x.select(precos[i])[0]
			print(nome.text , " = " , preco.text)