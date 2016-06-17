
import os
from flask import *

import sqlite3
import sqlite3 as sql


from app import app


#app = Flask(__name__)

conn = sqlite3.connect('/home/jonaranola/mysite/pylist/app/magedb.db')

@app.route('/')
def todolist():
	con = sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db')
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("SELECT * FROM tasks ORDER BY id")

	rows = cur.fetchall();
	return render_template('todolist.html', rows=rows)

@app.route('/add', methods=['POST', 'GET'])
def add():
	if request.method == 'POST':
		try:
			con = sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db')
			con.row_factory = sql.Row

			cur = con.cursor()
			cur.execute("SELECT * FROM tasks ORDER BY id")

			rows = cur.fetchall();

			task =  request.form['todo'];
			print task #check if user input reaches python

			try:
				with sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db') as con:
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
			con = sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db')
			con.row_factory = sql.Row

			cur = con.cursor()
			cur.execute("SELECT * FROM tasks ORDER BY id")

			rows = cur.fetchall();

			editID = request.form['editID'];
			print editID
			replaceItem = request.form['editTask'];
			print replaceItem

			if replaceItem != "":

				try:
					with sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db') as con:
						cur = con.cursor()
						cur.execute("UPDATE tasks SET task = (?) WHERE id = (?)", (replaceItem, editID,))
						con.commit()
						msg = "Record successfully updated"

				except:
					con.rollback()
		        	msg = "error in update operation"

		finally:
			return redirect("/")

@app.route('/delete/<postID>', methods=['POST', 'GET'])
def delete(postID):
	if request.method == 'POST':
		try:
			con = sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db')
			con.row_factory = sql.Row

			cur = con.cursor()
			cur.execute("SELECT * FROM tasks ORDER BY id")

			rows = cur.fetchall();

			try:
				with sql.connect('/home/jonaranola/mysite/pylist/app/magedb.db') as con:
					cur = con.cursor()
					cur.execute("DELETE FROM tasks WHERE id = (?)", [postID])
					con.commit()
					msg = "Record successfully deleted"

			except:
				con.rollback()
	        	msg = "error in delete operation"

		finally:
			return redirect("/")

@app.route('/readme')
def readme():
	return render_template("readme.html")

# if __name__ == "__main__":
#     app.run()