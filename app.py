
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
    try:
        images = ImageMetadata.query.all()
        return render_template('gallery.html', images=images)
    except Exception as e:
        app.logger.error(f"Failed to fetch images: {str(e)}")
        return "Internal Server Error", 500
if __name__ == '__main__':
    app.run(debug=True)

