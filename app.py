from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from routes.auth_route import auth_bp
from routes.usuario_route import usuario_bp
from routes.artista_route import artista_bp
from routes.empresa_route import empresa_bp
from routes.vaga_route import vaga_bp

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "seu-segredo-super-seguro"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(usuario_bp, url_prefix="/usuarios")
app.register_blueprint(artista_bp, url_prefix="/artistas")
app.register_blueprint(empresa_bp, url_prefix="/empresas")
app.register_blueprint(vaga_bp, url_prefix="/vagas")

if __name__ == "__main__":
    app.run(debug=True)
