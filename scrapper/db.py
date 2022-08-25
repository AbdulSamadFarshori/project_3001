
import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine("sqlite:///D:/work/project_3001/db.sqlite3", echo=True, future=True)

class Main_Data(Base):
	__tablename__ = "main_data"

	id = Column(Integer, primary_key=True,  autoincrement=True)
	title = Column(String)
	subheading = Column(String)
	main_problem = Column(String)
	author_name = Column(String)

	def __repr__(self):
		return f"{self.main_problem}"

class Reply_Data(Base):
	__tablename__ = "reply_data"
	id = Column(Integer, primary_key=True,  autoincrement=True)
	case_id = Column(Integer, ForeignKey("main_data.id"), nullable=False)
	author = Column(String)
	recipient = Column(String)
	reply = Column(String)
	
	
	def __repr__(self):
		return f"Reply {self.case_id}"

class Reply_thread(Base):
	__tablename__ = "reply_thread"
	id = Column(Integer, primary_key=True,  autoincrement=True)
	reply_id = Column(Integer, ForeignKey("reply_data.id"), nullable=False)
	author = Column(String)
	recipient = Column(String)
	reply = Column(String)
	
	def __repr__(self):
		return f"Reply {self.case_id}"

class Config(Base):
	__tablename__ = "config"
	id = Column(Integer, primary_key=True,  autoincrement=True)
	page_no = Column(Integer)

	def __repr__(self):
		return f"config {self.page_no}"


class LinkConfig(Base):
	__tablename__="link_config"

	id = Column(Integer, primary_key=True,  autoincrement=True)
	title = Column(String)
	heading = Column(String)
	link = Column(String)
	status = Column(String)

	def __repr__(self):
		return f"Reply {self.id}"

def create_db():
	Base.metadata.create_all(engine)
	return "db created"

def drop_table():
	Main_Data.__table__.drop(engine)
	Reply_Data.__table__.drop(engine)
	Reply_thread.__table__.drop(engine)
	return "deleted"
 # drops the users table





# class DataBase(object):
	
# 	def connection(self):	
# 		conn = sqlite3.connect('../db.sqlite3')
# 		c = conn.cursor()
# 		print("connected successfully")
# 		return conn, c

# 	def create_tables(self):
# 		try:
# 			conn, c = self.connection()
# 			c.execute('''CREATE TABLE main_data(id INTEGER PRIMARY KEY AUTOINCREMENT,
# 						 heading VARCHAR(255), sub_heading VARCHAR(255),
# 						 main_problem VARCHAR(65535), author_name  VARCHAR(255))''')

# 			c.execute('''CREATE TABLE reply_data(id INTEGER PRIMARY KEY AUTOINCREMENT, case_id INTEGER, reply TEXT, no_of_reply TEXT, 
# 						FOREIGN KEY (case_id) REFERENCES main_data(id))''')

# 			c.execute('''CREATE TABLE config(id INTEGER PRIMARY KEY AUTOINCREMENT, page_no INTEGER)''')
			
# 			conn.commit()
# 			conn.close()
# 		except Exception as e:
# 			print(e)
# 			print("create_tables")

# 		return "created tables"

# 	# Insert Values
# 	def insert_main_data(self, head, sub_head, main_problems, author_names):
# 		try:
# 			conn, c = self.connection()
# 			c.execute(f"INSERT INTO main_data(heading, sub_heading, main_problem, author_name) VALUES({head}, {sub_head}, {main_problems}, {author_names})")
# 			conn.commit()
# 			conn.close()
# 		except Exception as e:
# 			print(e)
# 			print("insert_main_data")

# 	def get_id(self, current_title):
# 		try:
# 			conn, c = self.connection()
# 			number = c.execute('SELECT id FROM main_data WHERE sub_heading = %s' , (current_title)).fetchone()
# 			conn.close()
# 			return number
# 		except Exception as e:
# 			print(e)
# 			print("get_id")
		


# 	def insert_replies(self, case_id, repy, no_of_reply):
# 		try:
# 			conn, c = self.connection()
# 			c.execute("INSERT INTO reply_data( case_id, repy, no_of_reply) VALUES(%s, %s, %s)",( case_id, repy, no_of_reply))
# 			conn.commit()
# 			conn.close()
# 		except Exception as e:
# 			print(e)
# 			print("insert_replies")

# 	def insert_config(self, page_no):
# 		try:
# 			conn, c = self.connection()
# 			c.execute(f"INSERT INTO config (page_no) VALUES({page_no})")
# 			conn.commit()
# 			conn.close()
# 		except Exception as e:
# 			print(e)
# 			print("insert_config")

# 	def update_config(self, value):
# 		try:
# 			conn, c = self.connection()
# 			c.execute(f"UPDATE config SET page_no = {value} WHERE id = 1;")
# 			conn.commit()
# 			conn.close()
# 		except Exception as e:
# 			print(e)
# 			print("update_config")


# 	# Read Values
# 	def get_object(self, table_name):
# 		try:
# 			conn, c = self.connection()
# 			number = [row for row in c.execute('SELECT * FROM %s' , (table_name)).fetchone()]
# 			conn.close()
# 			return number
# 		except Exception as e:
# 			print(e)
# 			print("get_object")
		

# 	def get_page_no(self):
# 		try:
# 			conn, c = self.connection()
# 			number = c.execute('SELECT page_no FROM config WHERE id = 1').fetchone()
# 			conn.close()
# 			return number
# 		except Exception as e:
# 			print(e)
# 			print("get_page_no")
# 		