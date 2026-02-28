from flask import Flask, render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = ['Gabriel', 'Ricardo', 'Cynthia', 'Ana Luiza']

app.config['SECRET_KEY'] = '23416eb77c1417fefa75088240681a3c'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)    

if __name__ == '__main__':
    app.run(debug=True)
