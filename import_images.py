
import os
import psycopg2
from PIL import Image

# Connect to the PostgreSQL database
conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()

# Path to the images directory
image_dir = "/data/images"

# Read each image and insert metadata into the database
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg"):  # Assuming JPEG images
        filepath = os.path.join(image_dir, filename)
        image = Image.open(filepath)
        size = os.path.getsize(filepath)
        date_taken = image._getexif().get(36867)  # EXIF date taken

        # Insert metadata into the database
        cur.execute("INSERT INTO image_metadata (filename, size, date_taken) VALUES (%s, %s, %s)",
                    (filename, size, date_taken))
        conn.commit()

cur.close()
conn.close()
