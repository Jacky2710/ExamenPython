from flask import Flask, send_from_directory
from config import db, migrate
from routes.User import user_bp
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
#cargar variables de entorno
load_dotenv()

app=Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY']='wyhgewty3g278te62fec32uhes'
jwt=JWTManager(app)

#configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(user_bp, url_prefix='/users')
@app.route("/swagger.yaml")
def get_swagger_yaml():
    return send_from_directory(os.path.dirname(_file_), "swagger.yaml")

# 📌 Configurar Swagger UI
SWAGGER_URL = "/docs"  # Ruta de Swagger UI
API_URL = "/swagger.yaml"  # URL del archivo YAML
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__=='__main__':
    app.run(debug=True)