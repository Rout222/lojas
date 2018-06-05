import MySQLdb
class sites(object):
	"""docstring for sites"""
	def __init__(self):
		super(sites, self).__init__()
		self.lista = self.pegarTodosOsSites()

	def pegarTodosOsSites(self):
		db=MySQLdb.connect(passwd="",db="lojas", user="root")
		c=db.cursor()
		c.execute("SELECT url, seletorProduto, seletorNome, seletorPreco FROM sites")
		sites = []
		for s in c.fetchall():
			sites.append(site(s[0],s[1],s[2],s[3]))
		return sites
class site(object):
	"""docstring for sites"""
	def __init__(self, url, seletorProduto, seletorNome, seletorPreco):
		super(site, self).__init__()
		self.url 			= url
		self.seletorProduto = seletorProduto
		self.seletorNome 	= seletorNome
		self.seletorPreco 	= seletorPreco
