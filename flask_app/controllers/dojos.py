from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def showMain():
    data = Dojo.getAllDojos()
    return render_template('index.html', dojos = data)

@app.route('/dojo/<int:id>')
def showOneDojo(id):
    dojo = Dojo.getDojoById(id)
    print("Returned Dojd: ", dojo.ninjas)
    return render_template("dojos_ninjas.html", dojo = dojo)

@app.route('/new_dojo', methods=["POST"])
def addDojo():
    print(f"Form Results! : {request.form}")
    data = {
        "name" : request.form["name"]
    }

    id = Dojo.addDojo(data)

    return redirect(f'/dojo/{id}')