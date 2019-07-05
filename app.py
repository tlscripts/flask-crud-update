from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(200))
    last = db.Column(db.String(200))
    one = db.Column(db.String(200))
    two = db.Column(db.String(200))

class EditUser:
    def first(idno, newname):
        q = User.query.filter_by(id=idno).first()
        q.first = newname
        db.session.add(q)
        db.session.commit()

    def last(idno, newname):
        q = User.query.filter_by(id=idno).first()
        q.last = newname
        db.session.add(q)
        db.session.commit()

    def one(idno, newname):
        q = User.query.filter_by(id=idno).first()
        q.one = newname
        db.session.add(q)
        db.session.commit()

    def two(idno, newname):
        q = User.query.filter_by(id=idno).first()
        q.two = newname
        db.session.add(q)
        db.session.commit()

def generate():
    db.create_all()

    for x in range(20):
        one = User(first='', last='', one='', two='')
        db.session.add(one)
        db.session.commit()

# generate()

# EditUser.first(5, 'Michael')
# EditUser.last(5, 'Jordan')