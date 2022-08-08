import sqlite3


class DataBase(object):
	
	def connection(self)	
		conn = sqlite3.connect('../db.sqlite3')
		c = conn.cursor()
		print("connected successfully")
		return c

	def create_tables(self)
		c.execute('''CREATE TABLE scrape_data(id INTEGER PRIMARY KEY AUTOINCREMENT,
					 heading TEXT, heading_url TEXT, heading_page_no TEXT, sub_heading TEXT,
					 sub_heading TEXT, main_problem TEXT, )''')
		conn.commit()
		conn.close()

# Insert Values
conn = sqlite3.connect('tablename.db')
c = conn.cursor()
c.execute("INSERT INTO tablename VALUES (?, ?)", (name, number))
conn.commit()
conn.close()

# Read Values
conn = sqlite3.connect('tablename.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM tablename'):
	print(row)

number = [row[2] for row in c.execute('SELECT * FROM tablename')]
conn.close()