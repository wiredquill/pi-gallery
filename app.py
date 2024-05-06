
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/dbase/images.db'
db = SQLAlchemy(app)
class ImageMetadata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer)
    date_taken = db.Column(db.String(255))
@app.route('/')
def index():
    images = ImageMetadata.query.all()
    return render_template('gallery.html', images=images)
if __name__ == '__main__':
    app.run(debug=True)
