from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from routes import routes
from models import Puppy

db = SQLAlchemy()

# POST /puppy
# test 끝내고 삭제 예정
@routes.route('/puppy', methods=['POST'])
def create_puppy():
    req = request.get_json()
    print(req)
    p = Puppy(name=req['name'], size=req['size'], kidFriendly=req['kidFriendly'], intelligence=req['intelligence'], highEnergy=req['highEnergy'],
              easyToTrain=req['easyToTrain'], lowBarking=req['lowBarking'], img_url=req['img_url'], feature=req['feature'])
    db.session.add(p)
    db.session.commit()
    return jsonify(req), 201


# GET /puppy/id
@routes.route('/api/puppy/<int:puppy_id>', methods=['GET'])
def get_puppy_by_id(puppy_id):
    p = Puppy.query.filter_by(id=puppy_id).first()
    puppy = {}
    puppy['id'] = p.id
    puppy['name'] = p.name
    puppy['size'] = p.size
    puppy['kidFriendly'] = p.kidFriendly
    puppy['intelligence'] = p.intelligence
    puppy['highEnergy'] = p.highEnergy
    puppy['easyToTrain'] = p.easyToTrain
    puppy['lowBarking'] = p.lowBarking
    puppy['img_url'] = p.img_url
    puppy['feature'] = p.feature

    return puppy