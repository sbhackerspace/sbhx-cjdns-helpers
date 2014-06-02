import flask
from flask import Flask

app = Flask(__name__)

urls = ('/')

render = flask.render_template('templates')

class Index(object):
	def GET(self):
		return render.peer_form()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s, %s" % (form.IP, form.Pswd, form.PubKey)
		return render.index(greeting = greeting)

if __name__ == '__main__':
	app.run()
