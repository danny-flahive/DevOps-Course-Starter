from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from todo_app.data.session_items import *

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    add_item(request.form.get('title'))
    return redirect('/')
