
#!/bin/bash
for file in /data/images/*.jpg; do
    size=$(stat -c %s "$file")
    date_taken="2024-01-01" # Example static date, replace with extraction logic
    sqlite3 /data/dbase/images.db "INSERT INTO image_metadata (filename, size, date_taken) VALUES ('$file', $size, '$date_taken');"
done
