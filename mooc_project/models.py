import sqlite3
from django.db import models

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()

class User(models.Model):
  username = models.TextField()
  password = models.TextField()

class Comments(models.Model):
  comment = models.TextField()

def user_query(src_str):
  cursor.execute(f'SELECT first_name, last_name, phone_number FROM Users WHERE first_name="{src_str}"')
  resp = cursor.fetchall()
  return resp

user = User(username="mahti", password="mursu")
user.save()

cursor.execute('DROP TABLE IF EXISTS Users')
cursor.execute('CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   ' first_name VARCHAR(20), last_name VARCHAR(20), phone_number TEXT, current_address TEXT)')
cursor.execute(
    'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
    ('Mursu', 'Mahti', '+35864682', 'Finland'))
cursor.execute(
    'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
    ('Antti', 'Laaksonen', '+35858424', 'Yliopisto'))
cursor.execute(
    'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
    ('Matti', 'Luukkainen', '+35862334', 'Koti'))
cursor.execute(
    'INSERT INTO Users ("first_name", "last_name", "phone_number", "current_address") VALUES (?, ?, ?, ?)',
    ('Leo', 'Varis', '+35896393', 'Vantaa'))
conn.commit()