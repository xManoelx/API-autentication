from flask import Flask, request, jsonify   # Importa Flask
from models.user import User                # Importa o modelo User
from database import db                     # Importa o objeto do banco de dados
from flask_login import LoginManager        # Importa o gerenciador de login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 

login_manager = LoginManager() 

db.init_app(app)                           # Inicializa o objeto do banco de dados
login_manager.init_app(app)                # Inicializa o gerenciador de login  

# view login


# Session <- conexão ativa com o banco de dados

# Carrega o usuário pelo ID mantendo a segurança devido ao uso da senha criptografada
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:  # Verifica se o usuário existe
            return jsonify({'message': 'Login bem-sucedido'}), 200

    return jsonify({'message': 'Credenciais invalidas'}), 400

# Cria a rotina Hello World
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)