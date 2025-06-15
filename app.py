from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import db, Staff

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///staff.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    staff_list = Staff.query.all()
    return render_template('index.html', staff=staff_list)

if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('staff.db'):
            db.create_all()
    app.run(debug=True)
