from flask import Flask
from models.user import User
from database import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' # Chave secreta para sessões
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Configuração do banco de dados SQLite

db.init_app(app) # Inicializa o objeto do banco de dados com a aplicação Flask

# Session <- conecxão ativa com o banco de dados

# Cria a rotina Hello World
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)