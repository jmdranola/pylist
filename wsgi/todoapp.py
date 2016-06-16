#!flask/Scripts/python

import os
from flask import *

import sqlite3
import sqlite3 as sql

app = Flask(__name__)

conn = sqlite3.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db'))

@app.route('/')
def todolist():
	con = sql.connect("magedb.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("SELECT * FROM tasks ORDER BY id")

	rows = cur.fetchall();
	return render_template('todolist.html', rows=rows)

#Insert user input into database
@app.route('/add', methods=['POST', 'GET'])
def add():
	if request.method == 'POST':
		try:
			con = sql.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db'))
			con.row_factory = sql.Row

			cur = con.cursor()
			cur.execute("SELECT * FROM tasks ORDER BY id")

			rows = cur.fetchall();

			task =  request.form['todo'];
			print task #check if user input reaches python

			try:
				with sql.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db')) as con:
					cur = con.cursor()
					cur.execute("INSERT INTO tasks (task) VALUES (?)",(task,))
					con.commit()
					msg = "Record successfully added"

			except:
				con.rollback()
	        	msg = "error in insert operation"
         		
		finally:
			return render_template("todolist.html", msg = msg, rows=rows)
         	con.close()

@app.route('/edit', methods=['POST'])
def edit():
	if request.method == 'POST':
		try:
			con = sql.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db'))
			con.row_factory = sql.Row

			cur = con.cursor()
			cur.execute("SELECT * FROM tasks ORDER BY id")

			rows = cur.fetchall();

			replaceItem = request.form['todo'];

			try:
				with sql.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db')) as con:
					cur = con.cursor()
					cur.execute("UPDATE tasks SET  task = ? WHERE id = ?", (replaceItem))
					con.commit()
					msg = "Record successfully updated"

			except:
				con.rollback()
	        	msg = "error in update operation"
         		
		finally:
			return render_template("todolist.html", msg = msg, rows=rows)
         	con.close()

@app.route('/delete', methods=['POST', 'GET'])
def delete():
	if request.method == 'POST':
		try:
			con = sql.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db'))
			con.row_factory = sql.Row

			cur = con.cursor()
			cur.execute("SELECT * FROM tasks ORDER BY id")

			rows = cur.fetchall();

			id = request.form['id']

			try:
				with sql.connect(os.path.join(os.environ.get('OPENSHIFT_DATA_DIR'), 'magedb.db')) as con:
					cur = con.cursor()
					cur.execute("DELETE FROM tasks  WHERE id = (?)", (id,))
					con.commit()
					msg = "Record successfully deleted"

			except:
				con.rollback()
	        	msg = "error in delete operation"
         		
		finally:
			return render_template("todolist.html", rows = rows)
         	con.close()

@app.route('/readme')
def readme():
	return render_template("readme.html")

if __name__ == "__main__":
    app.run()