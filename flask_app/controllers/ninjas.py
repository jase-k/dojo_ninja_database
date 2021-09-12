from flask_app.models.dojo import Dojo
from werkzeug.utils import redirect
from flask_app.models.ninja import Ninja
from flask.globals import request
from flask.templating import render_template
from flask_app import app

@app.route('/add_ninja')
def addNinja():
    data =  Dojo.getAllDojos()

    return render_template("new_ninja.html", data = data)

@app.route('/add_ninja/<int:dojo_id>')
def addNinjaWithID(dojo_id):
    data =  {
        "id" : dojo_id
    }

    return render_template("add_ninja_dojo.html", data = data)

@app.route('/add_ninja_submit', methods=["POST"])
def submitNinja():
    
    print("form Stuff: ", request.form)
    
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }

    id = Ninja.addNinja(data)

    return redirect(f'/dojo/{id}')