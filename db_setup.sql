
CREATE TABLE image_metadata (
    id SERIAL PRIMARY KEY,
    filename TEXT NOT NULL,
    size INTEGER,
    date_taken TIMESTAMP
);
