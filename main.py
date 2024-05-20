from flask import Flask, request, make_response, redirect, render_template

"""
    tengo q ver bien esto

"""
app = Flask(__name__)

items = ["Lechuga", "Platano", "Mango", "Uva"]


@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    reponse = make_response(redirect('/show_information_address'))
    reponse.set_cookie('user_ip_information', user_ip_information)

    return reponse


@app.route('/show_information_address')
def show_information():
    user_ip = request.cookies.get('user_ip_information')
    context = {
        "user_ip": user_ip,
        "items": items
    }
    return render_template('ip_information.html', **context)


@app.route('/index2')
def index2():
    return render_template('hola_mundo.html')


app.run(host='0.0.0.0', port=8080, debug=True)
