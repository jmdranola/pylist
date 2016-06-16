import os
from flask import *
import sqlite3
import sqlite3 as sql

app = Flask(__name__)
if __name__ == '__main__':
	app.run()


from app import views