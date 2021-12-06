from flask import render_template, request, redirect, Flask
import todo_app.data.session_items as session_items
import todo_app.data.trello_items as trello_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = trello_items.get_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    trello_items.add_item(request.form.get('title'))
    return redirect('/')

@app.route('/update/<id>')
def mark_completed(id):
    trello_items.complete_item(id)
    return redirect('/')

@app.route('/remove/<id>')
def remove(id):
    trello_items.remove_item(id)
    return redirect('/')