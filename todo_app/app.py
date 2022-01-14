from flask import render_template, request, redirect, Flask
from todo_app.ViewModel import ViewModel
import todo_app.data.trello_items as trello_items

from todo_app.flask_config import Config

def create_app():
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
    def move_item(id: str):
        if request.form["update"] == "Mark Completed":
            trello_items.change_status(id, "Done")
        elif request.form["update"] == "Set Doing":
            trello_items.change_status(id, "Doing")
        elif request.form["update"] == "Set To Do":
            trello_items.change_status(id, "To Do")
        return redirect('/')

    @app.route('/remove/<id>', methods=["POST"])
    def remove(id: str):
        trello_items.remove_item(id)
        return redirect('/')
    
    return app