from flask import Flask, request, jsonify                                            
from models.user import User                                                         
from database import db                                                              
from flask_login import LoginManager,  login_user, current_user, logout_user, login_required         

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 

login_manager = LoginManager() 

db.init_app(app)                           # Inicializa o objeto do banco de dados
login_manager.init_app(app)                # Inicializa o gerenciador de login  


login_manager.login_view = 'login'         # Visualiza a página de login

# Carrega o usuário pelo ID usando o gerenciador de login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rota para login do usuário
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Login
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:  # Verifica se o usuário existe
            login_user(user) # Faz a autenticação do usuário
            print(current_user.is_authenticated)  # Imprime que o usuário está autenticado
            return jsonify({'message': 'Login bem-sucedido'}), 200

    return jsonify({'message': 'Credenciais invalidas'}), 400

# Rota para logout do usuário
@app.route('/logout', methods=['GET'])
@login_required # Garante que o usuário esteja logado para acessar essa rota
def logout():
    logout_user()  # Faz o logout do usuário
    return jsonify({'message': 'Logout bem-sucedido'}), 200    

# Rota para criar um novo usuário
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Cria um novo usuário
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuário criado com sucesso'}), 201

    return jsonify({'message': 'Dados inválidos'}), 400

# Cria a rotina Hello World
@app.route('/hello-world', methods=['GET'])
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)