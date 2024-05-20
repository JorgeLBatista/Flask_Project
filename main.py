from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

"""
    tengo q ver bien esto

"""
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'CLAVE SEGURA'

items = ["Lechuga", "Platano", "Mango", "Uva"]


@app.errorhandler(404)
def not_found_endpoint(error):
    context = {
        "error": error
    }
    return render_template('error.html', **context)


@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    reponse = make_response(redirect('/show_information_address'))
    session["user_ip_information"] = user_ip_information

    return reponse


@app.route('/show_information_address')
def show_information():
    user_ip = session.get('user_ip_information')
    context = {
        "user_ip": user_ip,
        "items": items
    }
    return render_template('ip_information.html', **context)


@app.route('/index2')
def index2():
    return render_template('hola_mundo.html')


app.run(host='0.0.0.0', port=8080, debug=True)
