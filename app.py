from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta
from routes.auth_route import auth_bp, blacklist
from routes.usuario_route import usuario_bp
from routes.artista_route import artista_bp
from routes.empresa_route import empresa_bp
from routes.vaga_route import vaga_bp
from database.init_db import criar_tabelas

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "seu-segredo-super-seguro"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in blacklist

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(usuario_bp, url_prefix="/usuarios")
app.register_blueprint(artista_bp, url_prefix="/artistas")
app.register_blueprint(empresa_bp, url_prefix="/empresas")
app.register_blueprint(vaga_bp, url_prefix="/vagas")

if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)
