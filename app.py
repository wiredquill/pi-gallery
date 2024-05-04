
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect("dbname=postgres user=postgres host=db")  # 'db' is the service name in docker-compose

@app.route('/')
def gallery():
    cur = conn.cursor()
    cur.execute("SELECT filename FROM image_metadata")
    images = cur.fetchall()
    cur.close()
    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
