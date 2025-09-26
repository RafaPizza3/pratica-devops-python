from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return (
        '<h1>Olá, Mundo! Imagem Docker publicada com sucesso via GitHub Actions!</h1>'
        '<p>Minha primeira aplicação Flask em um container Docker.</p>'
        '<h2>Versão: 0.0.3<h2>'
        )

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=3333)