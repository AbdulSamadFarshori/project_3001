import requests
from config import baseurl
from bs4 import BeautifulSoup
import time
import datetime
from tqdm import tqdm
import logging
import csv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import Main_Data, Reply_Data, Reply_thread, Config, engine, LinkConfig
from connector import data

Session = sessionmaker(bind=engine)


# class bitio():
# 	def __init__(self):
# 		self.lists = []

# 	def get_list(self):
# 		list_data = data
# 		for heads in list_data:
# 			self.lists.append(heads['sub_heading'])
# 		return self.lists

# bit = bitio() 
# titel_list_data = bit.get_list()
# print(len(titel_list_data))

class FetchHtml():

	headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

	def __init__(self, url=None):
		
		self.url = url

	def fetcher(self):
		response = requests.get(self.url, headers= self.headers)
		html = BeautifulSoup(response.text, "html.parser")
		return html

class FindAllTags():

	def __init__(self, html=None, tag=None, class_name=None):
		
		self.tag = tag
		self.class_name = class_name
		self.html = html

	def get_all_tags(self):
		if self.html:
			result = self.html.find_all(self.tag, class_ = self.class_name)
			return result

	def get_without_class(self):
		if self.html:
			result = self.html.find_all(self.tag)
			return result

class FindSingleTag():
	
	def __init__(self, html=None, tag=None, class_name=None):
		self.tag = tag
		self.class_name = class_name
		self.html = html

	def get_single_tags(self):
		if self.html: 
			result = self.html.find(self.tag, class_ = self.class_name)
			return result

	def get_without_class(self):
		if self.html:
			result = self.html.find(self.tag)
			return result

class FetchMainPage():

	def __init__(self):
		self.starting_url = "https://patient.info/forums/categories/mental-health-25"
		self.main_capturing_list = ["Anxiety Disorders","Depression"]

									# "Alzheimer's Disease", 
									# "Alcohol Consumption", 
									# "Sleep Problems",
									# "PTSD - Post Traumatic Stress Disorder",
									# "Mental Health",
									# "Eating Disorders",
									# "Depression",
									# "Dementia",
									# "Bipolar Affective Disorder",
									# "Autistic Spectrum Disorders",
									# "Substance Misuse"

	def get_all_links_list(self):
		html_obj = FetchHtml(url = self.starting_url)
		html = html_obj.fetcher()
		all_tags = FindAllTags(html=html, tag="h3", class_name="title").get_all_tags()
		return all_tags

	def linklist(self):
		output = {}
		for _temp in self.get_all_links_list():
			title = FindSingleTag(html=_temp, tag="a").get_without_class().text
			if title in self.main_capturing_list:
				anchor_tag = FindSingleTag(html=_temp, tag="a").get_without_class()  
				output[title] = baseurl + anchor_tag["href"]
		return output

class FetchCasesLinks():

	def __init__(self):
		self.var = 0
		self.main_page = FetchMainPage().linklist()
		self.db = Session()

	def get_last_page(self, url=None):
		_html = FetchHtml(url=url).fetcher()
		_tag = FindSingleTag(html=_html, tag="select", class_name="submit reply__control reply-pagination").get_single_tags()
		if _tag:
			options = FindAllTags(html=_tag, tag="option").get_without_class()
			last_page = options[-1]["value"]
			page = int(last_page)
			return page
		return 0

	def get_title_links_urls(self):
		url_list = {}
		title_tag = ""
		for title, url in self.main_page.items():
			last_page = self.get_last_page(url=url)
			urls = [url + f"?page={page}" for page in range(last_page+1)]
			url_list[title] = urls
		return url_list

	def get_links(self, html_obj):
		html = html_obj
		fetcher = FindAllTags(html=html, tag="h3", class_name="post__title")
		all_tags = fetcher.get_all_tags()
		return all_tags

	def linklist(self, html_obj):
		output = {}
		for _temp in self.get_links(html_obj):
			self.var += 1
			title = FindSingleTag(html=_temp, tag="a").get_without_class().text
			anchor_tag = FindSingleTag(html=_temp, tag="a").get_without_class()
			t = anchor_tag["href"] 
			print(f"{self.var} --> {baseurl + t}") 
			output[f"{title}-{self.var}"] = baseurl + anchor_tag["href"]
			link_obj = LinkConfig(title=title, link=baseurl + anchor_tag["href"], status="No")
			self.db.add(link_obj)
			self.db.commit()
		return output 

	def fetch_cases_html(self):
		_foo = []
		url_list = self.get_title_links_urls()
		for title, pos in url_list.items():
			for _temp in pos:
				_html = FetchHtml(url=_temp).fetcher()
				_tags = self.linklist(_html)
				_foo.append(_tags)
		first = len(_foo)
		print(f"============={first}=====================")
		return _foo


class GetProblem():
	
	def __init__(self):	
		self.db = Session()

	def get_tags(self, current_title, current_url):
		current_title = str(current_title)
		current_page_html = FetchHtml(url=current_url).fetcher()
		return current_page_html

	def get_author(self, current_page_html):
		author_name = '' 
		author = FindSingleTag(html=current_page_html, tag="a", class_name="author__name").get_single_tags()
		if author:
			author_name = author.text
		return author_name

	def get_main_case(self, current_page_html):
		main_problem = FindSingleTag(html=current_page_html, tag="div",class_name="post__content").get_single_tags()
		problem_text = FindSingleTag(html=main_problem, tag="input", class_name="moderation-conent").get_single_tags()
		chief_complaint = str(problem_text["value"])
		return chief_complaint

	def get_last_page(self, current_page_html):
		_tag = FindSingleTag(html=current_page_html, tag="select", class_name="reply-pagination").get_single_tags()
		if _tag:
			options = FindAllTags(html=_tag, tag="option").get_without_class()
			last_page = options[-1]["value"]
			page = int(last_page)
			return page
		return 0

	def no_of_reply(self, curent_page_html):
		no_of_reply = self.get_last_page(curent_page_html)
		return no_of_reply

	def fetch_reply_page_links(self, current_url, current_page_html):
		_temp = []
		for page in range(self.get_last_page(current_page_html)):
			reply_url = current_url + f"?order=oldest&page={page}"
			_temp.append(reply_url)
		return _temp

	def divs(self, reply_url):
		reply_html = FetchHtml(url=reply_url).fetcher()
		div_= FindSingleTag(html=reply_html, tag="div", class_name="reply").get_single_tags()
		return div_

	def reply_counts(self, div_):
		if div_:
			No_of_comments = FindSingleTag(html=div_, tag="h2", class_name="reply__title u-h4").get_single_tags()
			No_of_comment = None
			if No_of_comments:
				No_of_comment = No_of_comments.text
			return No_of_comment
	
	def get_articles(self, div_):
		lists_of = []
		get_articles = FindAllTags(html=div_, tag="article", class_name="post post__root").get_all_tags()
		for art in get_articles:
			comment_thread = ""
			try:
				reply_author = FindAllTags(html=art, tag="a", class_name="author__name").get_all_tags()
				reciept_author = FindAllTags(html=art, tag="a", class_name="author__recipient").get_all_tags()
			except Exception as e:
				print(e)
				reply_author = "None"
				reciept_author = "None"
				pass

			reply_list = FindAllTags(html=art, tag="input",class_name="moderation-conent").get_all_tags()
			if reply_list:
				for a, b, c  in zip(reply_author, reciept_author, reply_list):
					a = a.text
					b = b.text
					reply = c["value"]
					comment_thread += f"{a}={b}|{reply} --> "
			lists_of.append(comment_thread)

		return lists_of

	def run_appliction(self):
		link_data = self.db.query(LinkConfig).filter_by(status="No").all()
		print(len(link_data))
		for row in link_data:
			current_title = row.title
			current_url = row.link 
			print()
			print("wait..")
			print()
			print("fetching tags")
			current_html_page = self.get_tags(current_title, current_url)
			print("author data..")
			author = self.get_author(current_html_page)
			print("case data...")
			case = self.get_main_case(current_html_page)
			data = Main_Data( sub_heading=current_title,\
											main_problem=case,\
											author_name=author)
			self.db.add(data)
			self.db.commit()
			case_id = data.id
			url_list = self.fetch_reply_page_links(current_url, current_html_page)
			print(url_list)
			for url in url_list:
				div_ = self.divs(url)
				counts = self.reply_counts(div_)
				reply_data = self.get_articles(div_)
				print(f"=================+{reply_data}+==================")
				thread = reply_data[0].split("-->")
				main_head = thread[0]
				foo = main_head.split("|")
				print(foo)
				if len(foo) >= 2:
					reply = foo[1]
					author, recipient = foo[0].split("=")[0], foo[0].split("=")[1]
					reply_obj = Reply_Data(
										case_id=case_id,\
										author=author,\
										recipient=recipient,  
										reply=reply, 
										)
					self.db.add(reply_obj)
					self.db.commit()
					reply_id = reply_obj.id
					print(f"==========={len(thread)}========")
					if len(thread) >= 2:
						for index in range(1,len(thread)):
							if thread[index] or thread[index] != " ":
								print(thread[index])
								print(len(thread[index]))
								foo1 = thread[index].split("|")
								print(foo1)
								if len(foo1) >= 2:
									
									reply = foo1[1]
									author, recipient = foo1[0].split("=")[0], foo1[0].split("=")[1]

									thread_data = Reply_thread(reply_id=reply_id,
															author=author,
															recipient=recipient, 
															reply=reply, 
																	)
									self.db.add(thread_data)
									self.db.commit()
	
			obj = self.db.query(LinkConfig).filter_by(link=current_url).first()
			obj.status = "yes"
			self.db.add(obj)
			self.db.commit()



if __name__ == "__main__":
	testing = GetProblem()
	print(testing.run_appliction())
	pass