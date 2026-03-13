CREATE TABLE post (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(200),
    body TEXT,
    image_url VARCHAR(500)
);