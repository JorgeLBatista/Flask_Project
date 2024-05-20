from flask import Flask, request, make_response, redirect

"""
    tengo q ver bien esto

"""
app = Flask(__name__)


@app.route('/index')
def index():
    user_ip_information = request.remote_addr
    reponse = make_response(redirect('/show_information_address'))
    reponse.set_cookie('user_ip_information', user_ip_information)
    return reponse

@app.route('/show_information_address')
def show_information():
    user_ip = request.cookies.get('user_ip_information')
    return f'Hola su ip es: {user_ip}'

app.run(host='0.0.0.0', port=81, debug=True)






