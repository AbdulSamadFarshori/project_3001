import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import Main_Data, Reply_Data, Reply_thread, Config, engine, LinkConfig

Session = sessionmaker(bind=engine)


class DataUploader(object):

	def __init__(self):
		self.db = Session()


	def row2dict(self, row):
    	d = {}
    	for column in row.__table__.columns:
        	d[column.name] = str(getattr(row, column.name))

    	return d

    def http_requester(self, method=None, url=None, headers=None, data=None):
    	
    	if method == "post":
    		if json_data:
    			response = requests.post(url=url, data=data)
    			if response.status_code == 200:
    				return {"msg":"successfull!"}
    			return {"msg":"Error"}
    		else:
    			return "only post request send!"

    def send_main_data(self):
    	data = self.db.query(Main_Data).all()
    	for obj in data:
    		if obj:
    			_foo = self.row2dict(obj)
    			res = self.http_requester(method="post", url="https://abdulsamad.pythonanywhere.com/apis/main-data", data=_foo)
    			print("data sending...")
    	return "done"

    def send_reply_data(self):
    	data = self.db.query(Reply_Data).all()
    	for obj in data:
    		if obj:
    			_foo = self.row2dict(obj)
    			res = self.http_requester(method="post", url="https://abdulsamad.pythonanywhere.com/apis/reply-data", data=_foo)
    			print("data sending...")
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
    	self.send_main_data()
    	print()
    	print("sending reply data...")
    	print()
    	self.send_reply_data()
    	print()
    	print("sending reply thread data...")
    	print()
    	self.send_reply_thread()



if __name__ == "__main__":
	run = DataUploader()
	run.start_uploading()
	exit()

