import MySQLdb
from urllib.request import urlopen,build_opener
from bs4 import BeautifulSoup
import re

class sites(object):
	"""docstring for sites"""
	def __init__(self):
		super(sites, self).__init__()
		lista = []
		self.pegarTodosOsSites()

	def pegarTodosOsSites(self):
		db=MySQLdb.connect(passwd="",db="lojas", user="root")
		c=db.cursor()
		c.execute("SELECT url, seletorProduto, seletorNome, seletorPreco, consultaInput, consultaTarget, moeda FROM sites")
		sites = []
		for s in c.fetchall():
			sites.append(site(s))
		self.lista = sites

	def fazerPesquisas(self, arg):
		for s in self.lista:
			s.criarPesquisa(arg)
class site(object):
	"""docstring for sites"""
	def __init__(self, s):
		super(site, self).__init__()
		if(len(s) == 7):
			self.url 			= s[0]
			self.seletorProduto = s[1]
			self.seletorNome 	= s[2]
			self.seletorPreco 	= s[3]
			self.consultaInput	= s[4]
			self.consultaTarget	= s[5]
			self.moeda			= s[6]
		else:
			 raise Exception('Argumentos inválidos')


	def fazerUrl(self, arg):
		return self.url.format(arg.translate(arg.maketrans(self.consultaInput, self.consultaTarget)))

	def nomePrintavel(self, nome):
		return nome.strip()	

	def precoPrintavel(self, preco):
		return (self.moeda + re.sub("[^,.0-9]+", "", preco))

	def criarPesquisa(self, arg):
		urlDePesquisa = self.fazerUrl(arg)
		opener = build_opener()
		opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
		try:
			request = opener.open(urlDePesquisa, timeout=5)
		except Exception as e:
			print("Time out!")
		else:
			rHTML = BeautifulSoup(request.read(), "html.parser")
			for x in rHTML.select(self.seletorProduto):
				nome = self.nomePrintavel(x.select(self.seletorNome)[0].text)
				preco = self.precoPrintavel(x.select(self.seletorPreco)[0].text)
				print(nome , " = " , preco)
