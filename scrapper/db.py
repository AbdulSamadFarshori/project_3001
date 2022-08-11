<<<<<<< HEAD
import sqlite3


class DataBase(object):
	
	def connection(self):	
		conn = sqlite3.connect('../db.sqlite3')
		c = conn.cursor()
		print("connected successfully")
		return conn, c

	def create_tables(self):
		conn, c = self.connection()
		c.execute('''CREATE TABLE main_data(id INTEGER PRIMARY KEY AUTOINCREMENT,
					 heading TEXT, heading_url TEXT, heading_page_no TEXT, sub_heading TEXT,
					 sub_heading_url TEXT, main_problem TEXT, author_name  TEXT)''')

		c.execute('''CREATE TABLE reply_data(id INTEGER PRIMARY KEY AUTOINCREMENT, case_id INTEGER, reply TEXT, no_of_reply TEXT, 
					FOREIGN KEY (case_id) REFERENCES main_data(id))''')

		c.execute('''CREATE TABLE config(id INTEGER PRIMARY KEY AUTOINCREMENT, page_no INTEGER)''')
		
		conn.commit()
		conn.close()

		return "created tables"

	# Insert Values
	def insert_main_data(self, heading, heading_url, heading_page_no, sub_heading, sub_heading_url, main_problem, author_name):
		conn, c = self.connection()
		c.execute("INSERT INTO main_data VALUES(%s, %s, %s, %s, %s, %s, %s)",\
						 (heading, heading_url, heading_page_no, sub_heading, sub_heading_url, main_problem, author_name))
		conn.commit()
		conn.close()

	def get_id(self, current_title):
		conn, c = self.connection()
		number = c.execute('SELECT id FROM main_data WHERE sub_heading = %s' , (current_title))
		conn.close()
		return number


	def insert_replies(self, case_id, repy, no_of_reply):
		conn, c = self.connection()
		c.execute("INSERT INTO reply_data VALUES(%s, %s, %s)",( case_id, repy, no_of_reply))
		conn.commit()
		conn.close()

	def insert_config(self, page_no):
		conn, c = self.connection()
		c.execute(f"INSERT INTO config VALUES({page_no})")
		conn.commit()
		conn.close()

	def update_config(self, value):
		conn, c = self.connection()
		c.execute("UPDATE config SET page_no = %s WHERE id = 1;",(value))
		conn.commit()
		conn.close()


	# Read Values
	def get_object(self, table_name):
		conn, c = self.connection()
		number = [row for row in c.execute('SELECT * FROM %s' , (table_name))]
		conn.close()
		return number

	def get_page_no(self):
		conn, c = self.connection()
		number = c.execute('SELECT page_no FROM config WHERE id = 1')
		conn.close()
=======
import sqlite3


class DataBase(object):
	
	def connection(self):	
		conn = sqlite3.connect('../db.sqlite3')
		c = conn.cursor()
		print("connected successfully")
		return conn, c

	def create_tables(self):
		conn, c = self.connection()
		c.execute('''CREATE TABLE main_data(id INTEGER PRIMARY KEY AUTOINCREMENT,
					 heading TEXT, heading_url TEXT, heading_page_no TEXT, sub_heading TEXT,
					 sub_heading_url TEXT, main_problem TEXT, author_name  TEXT)''')

		c.execute('''CREATE TABLE reply_data(id INTEGER PRIMARY KEY AUTOINCREMENT, case_id INTEGER, reply TEXT, no_of_reply TEXT, 
					FOREIGN KEY (case_id) REFERENCES main_data(id))''')

		c.execute('''CREATE TABLE config(id INTEGER PRIMARY KEY AUTOINCREMENT, page_no INTEGER)''')
		
		conn.commit()
		conn.close()

		return "created tables"

	# Insert Values
	def insert_main_data(self, heading, heading_url, heading_page_no, sub_heading, sub_heading_url, main_problem, author_name):
		conn, c = self.connection()
		c.execute("INSERT INTO main_data VALUES(%s, %s, %s, %s, %s, %s, %s)",\
						 (heading, heading_url, heading_page_no, sub_heading, sub_heading_url, main_problem, author_name))
		conn.commit()
		conn.close()

	def get_id(self, current_title):
		conn, c = self.connection()
		number = c.execute('SELECT id FROM main_data WHERE sub_heading = %s' , (current_title))
		conn.close()
		return number


	def insert_replies(self, case_id, repy, no_of_reply):
		conn, c = self.connection()
		c.execute("INSERT INTO reply_data VALUES(%s, %s, %s)",( case_id, repy, no_of_reply))
		conn.commit()
		conn.close()

	def insert_config(self, page_no):
		conn, c = self.connection()
		c.execute(f"INSERT INTO config VALUES({page_no})")
		conn.commit()
		conn.close()

	def update_config(self, value):
		conn, c = self.connection()
		c.execute("UPDATE config SET page_no = %s WHERE id = 1;",(value))
		conn.commit()
		conn.close()


	# Read Values
	def get_object(self, table_name):
		conn, c = self.connection()
		number = [row for row in c.execute('SELECT * FROM %s' , (table_name))]
		conn.close()
		return number

	def get_page_no(self):
		conn, c = self.connection()
		number = c.execute('SELECT page_no FROM config WHERE id = 1')
		conn.close()
>>>>>>> d7fcdbf4d7cf542bbcf458b18f3540904a40e123
		return number