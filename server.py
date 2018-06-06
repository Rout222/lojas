from flask import Flask, render_template, request,jsonify, Markup
import MySQLdb
import classes
import sys
s = classes.sites()

app = Flask(__name__)
@app.route("/", methods = ['GET', 'POST'])
def hello():
	lista = []
	if (len(request.form) > 0) and (len(request.form['input']) > 0):
		lista = s.fazerPesquisas(request.form['input'])
	return render_template('index.html', lista=lista)

def pr(valor):
	print(valor, file=sys.stderr)

if __name__ == "__main__":
	app.run()