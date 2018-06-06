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
		c.execute("SELECT url, seletorProduto, seletorNome, seletorPreco, consultaInput, consultaTarget, moeda, seletorLike FROM sites")
		sites = []
		for s in c.fetchall():
			sites.append(site(s))
		self.lista = sites

	def fazerPesquisas(self, arg):
		listaDeProdutos = []
		for s in self.lista:
			listaDeProdutos.append(s.criarPesquisa(arg))
		return listaDeProdutos
class site(object):
	"""docstring for sites"""
	def __init__(self, s):
		super(site, self).__init__()
		if(len(s) == 8):
			self.url 			= s[0]
			self.seletorProduto = s[1]
			self.seletorNome 	= s[2]
			self.seletorPreco 	= s[3]
			self.consultaInput	= s[4]
			self.consultaTarget	= s[5]
			self.moeda			= s[6]
			self.seletorLike	= s[7]
		else:
			 raise Exception('Argumentos inválidos')


	def fazerUrl(self, arg):
		return self.url.format(arg.translate(arg.maketrans(self.consultaInput, self.consultaTarget)))

	def nomePrintavel(self, nome):
		try:
			nome = nome[0].text.strip()
		except Exception as e:
			pass
		else:
			nome = "Erro capturando o nome do " + self.url +". Contate o administrador."
		return nome	

	def precoPrintavel(self, preco):
		try:
			preco = preco[0].text
		except Exception as e:
			pass
		else:
			preco = "Erro capturando o preço do " + self.url +". Contate o administrador."
		return (re.sub("[^,.0-9]+", "", preco))

	def likePrintavel(self, like):
		try:
			like = like[0].text
		except Exception as e:
			pass
		else:
			like = "Erro capturando o likes do " + self.url +". Contate o administrador."
		return (re.sub("[^0-9]+", "", like))

	def criarPesquisa(self, arg):
		urlDePesquisa = self.fazerUrl(arg)
		print(urlDePesquisa)
		opener = build_opener()
		opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
		try:
			request = opener.open(urlDePesquisa, timeout=10)
		except Exception as e:
			print(self.url + "Time out!")
		else:
			reqHTML = BeautifulSoup(request.read(), "html.parser")
			produto = []
			for x in reqHTML.select(self.seletorProduto):
				nome  = self.nomePrintavel  ( x.select(self.seletorNome))
				preco = self.precoPrintavel ( x.select(self.seletorPreco))
				likes = self.likePrintavel  ( x.select(self.seletorLike))
				produto.append({"Nome" : nome, "Preco" : preco,  "Moeda" : self.moeda, "Likes" : likes})
			return produto
