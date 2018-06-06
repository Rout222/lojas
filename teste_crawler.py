import classes
from operator import attrgetter
s = classes.sites()
consulta = "Xiaomi redmi 5"
lista = s.fazerPesquisas(consulta)
lista = sorted(lista, key=attrgetter('Likes', 'Preco'), reverse=True)
print(lista)