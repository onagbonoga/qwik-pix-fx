from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)
#configure app to work with lib sass
app.wsgi_app = SassMiddleware(app.wsgi_app,{'qpfApp':("static/styles", "static/styles", "/static/styles")})
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

from qpfApp.core.views import core_app

#register blue print
app.register_blueprint(core_app)