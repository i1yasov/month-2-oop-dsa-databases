import sqlite3
connect = sqlite3.connect('netflix.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL
        )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(30) NOT NULL,
        genre VARCHAR(30) NOT NULL
        )
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        movie_id INTEGER,
        rating INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(movie_id) REFERENCES movies(id)
        )
''')
cursor.executemany(
    "INSERT INTO users (name) VALUES (?)",
    [
        ("Beksultan",),
        ("Aibek",),
        ("Nursultan",),
        ("Aliya",),
        ("Amina",)
    ]
)
cursor.executemany(
    "INSERT INTO movies (title, genre) VALUES (?, ?)",
    [
        ('Бейиш','ДРАМА'),
        ('Салам, New York','КОМЕДИЯ'),
        ('В Поисках Мамы','ДРАМА'),
        ('Палчан','Комедия'),
        ('Мастера меча онлайн','Фэнтази')
    ]
)
cursor.executemany(
    "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
    [
        (1, 1, 10),
        (1, 2, 8),
        (2, 1, 9),
        (2, 3, 7),
        (3, 4, 10),
        (3, 5, 6),
        (4, 2, 9),
        (4, 3, 8),
        (5, 1, 10),
        (5, 4, 9),
        (2, 5, 7),
        (1, 3, 8)
    ]
)
connect.commit()
cursor.execute('''
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
''')
print(cursor.fetchall())
cursor.execute('''
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
''')
print(cursor.fetchall())
cursor.execute('''
SELECT AVG(rating)
FROM reviews
''')
print(cursor.fetchone()[0])

cursor.execute('''
SELECT MAX(rating)
FROM reviews
''')
print(cursor.fetchone()[0])

cursor.execute('''
SELECT MIN(rating)
FROM reviews
''')
print(cursor.fetchone()[0])
