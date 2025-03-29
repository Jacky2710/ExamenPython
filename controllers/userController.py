from models.user import User
from config import db
from flask import jsonify
from flask_jwt_extended import create_access_token

def users():
    try:
        return [user.to_dict() for user in User.query.all()]
    except Exception as e:
        return jsonify(e)

def crear(name, email, password):
    try:
        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"{e}"})



def login(email, password):
    user=User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        access_token=create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user':{
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        })
    return jsonify({"msg": "Credenciales invalidad"}), 401