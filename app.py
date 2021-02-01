from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)
app.wsgi_app = SassMiddleware(app.wsgi_app,{'prolificApp':("static/styles", "static/styles", "/static/styles")})
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def home():
	return render_template("index.html")