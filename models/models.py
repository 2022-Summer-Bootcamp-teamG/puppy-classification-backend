from app import db


class Puppy(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    kidFriendly = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    highEnergy = db.Column(db.Integer, nullable=False)
    easyToTrain = db.Column(db.Integer, nullable=False)
    lowBarking = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    feature = db.Column(db.Text(), nullable=False)
