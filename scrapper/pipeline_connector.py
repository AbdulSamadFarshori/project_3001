import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import Main_Data, Reply_Data, Reply_thread, Config, engine, LinkConfig

Session = sessionmaker(bind=engine)


class DataUploader(object):

	def __init__(self):
		self.db = Session()


	def row2dict(self):
		d = []
		f = set([])
		reply = self.db.query(Reply_Data).all()
		for ids in reply:
			c_d = ids.case_id
			f.add(c_d)
		for i in f:
			case = self.db.query(Main_Data).filter_by(id=i).first()
			d.append(case)
		print(len(d))
		print(d[0].id)
		print(d[0].sub_heading)
		return d

	def http_requester(self, method=None, url=None, headers=None, data=None):
		if method == "post":
			if data:
				response = requests.post(url=url, data=data)
				if response.status_code == 200:
					print(response.json())
					return {"msg":"successfull!"}
			return {"msg":"Error"}
		return "only post request send!"

	def send_main_data(self):
		
				
		res = self.http_requester(method="post", url="https://abdulsamad.pythonanywhere.com/apis/main-data", data=_foo)
		print("data sending...")
		return "done"

	def send_reply_data(self):
		data = self.db.query(Reply_Data).all()
		for obj in data:
			if obj:
				_foo = self.row2dict(obj)
				res = self.http_requester(method="post", url="https://abdulsamad.pythonanywhere.com/apis/reply-data", data=_foo)
				
				print(res)
		return "done"

	def send_reply_thread(self):
		data = self.db.query(Reply_thread).all()
		for obj in data:
			if obj:
				_foo = self.row2dict(obj)
				res = self.http_requester(method="post", url="https://abdulsamad.pythonanywhere.com/apis/reply-thread", data=_foo)
				print("data sending...")
		return "done"

	def start_uploading(self):
		# self.send_main_data()
		print()
		print("sending reply data...")
		print()
		self.send_reply_data()
		print()
		# print("sending reply thread data...")
		# print()
		# self.send_reply_thread()


if __name__ == "__main__":
	run = DataUploader()
	run.row2dict()
	exit()

