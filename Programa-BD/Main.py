from flask import Flask
from flask import render_template, request, redirect, url_for
from Registro import Registro
from Registro import login

app = Flask(__name__)
app.secret_key = 'tu_clave_es_tuya'
@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/Registro/", methods=["GET", "POST"])   
def Registro1():
    form = Registro()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        print(email)
        print(name)
        print(password)
        if next:
         return redirect(next)
        return redirect (url_for('Registro'))                     
    return render_template("Registro.html",form=form)


@app.route("/login/", methods=["GET", "POST"])
def login1():
   form = login()
   if form.validate_on_submit():
      name = form.name.data
      email = form.name.data
      password = form.password.data
      next= request.args.get('next', None)
      print(email)
      print(name)
      print(password)
      if next:
         return redirect(next)
      return redirect (url_for('hello'))
   return render_template("login.html", form=form)
