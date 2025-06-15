from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    profile_url = db.Column(db.String(300), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Staff {self.name}>'
