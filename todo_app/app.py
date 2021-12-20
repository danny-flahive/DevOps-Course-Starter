from flask import render_template, request, redirect, Flask
from todo_app.ViewModel import ViewModel
import todo_app.data.trello_items as trello_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    view_model = ViewModel(trello_items.get_items())
    return render_template('index.html', view_model=view_model)

@app.route('/add', methods=['POST'])
def add():
    trello_items.add_item(request.form.get('title'), request.form.get("description"))
    return redirect('/')

@app.route('/update/<id>', methods=["POST"])
def mark_completed(id: str):
    trello_items.change_status(id, "Done")
    return redirect('/')

@app.route('/remove/<id>', methods=["POST"])
def remove(id: str):
    trello_items.remove_item(id)
    return redirect('/')