from flask import Flask

#instancia do servidor do flask
app = Flask(__name__)

#rota 1: pagina principal

@app.route('/')
def home():
    return "<H1>Servidor Flask rodando.</h1>" "<h1>Bem vindo ao meu servidor Flask!</h1>"

#rota 2: sobre a aplicação

@app.route('/sobre')
def sobre():
    return "<p>Sobre a aplicação.</h1>" "<h1>Esta é uma simples aplicação flask.</p>"

#Rota 3: Status de aplicação

@app.route('/status')
def status():
    return "<H1>Status da aplicação.</h1>" "<h1>O servidor flask está rodando corretamnete.</h1>"

if __name__ == '__main__':
    app.run(debug = True)