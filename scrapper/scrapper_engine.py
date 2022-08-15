import requests
from bs4 import BeautifulSoup
# from capchta_solver import Capchta_Solver 
from config import sitekey, baseurl, api_key
import time
import datetime
from tqdm import tqdm
import logging
import csv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from db import Main_Data, Reply_Data, Config, engine

Session = sessionmaker(bind=engine)

class scrapper(object):

	def __init__(self):
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

		self.main_capturing_list = ["Depression"]
		
		self.starting_url = "https://patient.info/forums/categories/mental-health-25"
		
		self.db = Session()


	def get_html(self, url=None):
		if url:
			print()
			print("wait processing...")
			headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
			response = requests.get(url, headers=headers)
			html = BeautifulSoup(response.text, "html.parser")
			print()
			print("ready to scrape the data..")
			return html
		
	def get_anchor_tag_link_address(self, tag, class_name, html):
		lists_of_link = {}
		list_of_anchor_tag = html.find_all(tag, class_ = class_name)
		for link in list_of_anchor_tag:
			mental_health_title = link.find("a").text
			if mental_health_title in self.main_capturing_list:
				a = link.find("a")
				h = a["href"]
				url = baseurl + h
				lists_of_link[mental_health_title] = url
		
		print()
		print("ready to scrape the data...")
		return lists_of_link

	def get_anchor_tags(self, tag, class_name, html):
		
		lists_of_link = {}
		list_of_anchor_tag = html.find_all(tag, class_ = class_name)
		for link in list_of_anchor_tag:
			mental_health_title = link.find("a").text			
			a = link.find("a")
			h = a["href"]
			url = baseurl + h
			lists_of_link[mental_health_title] = url
		
		print()
		print("ready to scrape the data...")
		return lists_of_link

	def get_author(self, tag, class_name, html):
		author_name = html.find(tag, class_=class_name)
		return author_name

	def last_page_no(self, tag, class_name, html):
		
		pages = html.find(tag, class_=class_name)
		if pages:
			options = pages.find_all("option")
			last_page = options[len(options)-1]["value"]
			page = int(last_page)
			return page
		return 0
	
	def get_main_problem(self, tag, class_name, html):
		main_problem = html.find(tag, class_=class_name)
		return main_problem	

	def comment_author_and_recipient(self, html):
		author = html.find_all("a", class_="author__name")
		recipient_a = html.find_all("a", class_="author__recipient")
		recipient = None
		if recipient_a:
			recipient = recipient_a[0].text
		return author[0].text, recipient


	def comment(self, tag, class_name, html):
		list_of_comment_value = html.find_all(tag, class_=class_name)
		return list_of_comment_value

	def get_div(self, tag, class_name, html):
		li_lists = html.find(tag, class_=class_name)
		return li_lists

	
	def scrapping_engine(self):
		get_config_page_no = self.db.query(Config).filter_by(id=1).first()
		if get_config_page_no is None:
			starting_page = Config(page_no=0)
			self.db.add(starting_page)
			self.db.commit()
		get_page_no_db =  self.db.query(Config).filter_by(id=1).first()
		print(get_page_no_db.page_no)
		try:
			stop_condition = 200
			condition = False
			# starting page section 
			html = self.get_html(url=self.starting_url)
			url_list = self.get_anchor_tag_link_address("h3", "title", html)

			# main title section
			for title, page_url in url_list.items():
				if condition:
					break
				print()
				print(f"fetching --> {page_url}")
				new_html = self.get_html(url=page_url)
				last_page = self.last_page_no("select", "submit reply__control reply-pagination", new_html)
				# problem list section

				for page in range(get_page_no_db.page_no, last_page+1):
					get_page_no_db.page_no = page
					self.db.commit()
					print("page No ", get_page_no_db.page_no)
					# stop loop
					if page == stop_condition:
						condition = True
						break

					working_url = page_url + f"?page={page}"
					print()
					print(f"fetching data of {title} --> {working_url}")
					current_working_html = self.get_html(url=working_url)
					new_list_of_urls = self.get_anchor_tags("h3", "post__title", current_working_html)
					# main problem section
					for current_title, current_page in new_list_of_urls.items():
						chief_complaint = ""
						current_title = str(current_title)
						print(f"fetching data of {title} --> {working_url} --> {current_page}")
						curent_page_html = self.get_html(url=current_page)
						main_problem = self.get_main_problem("div","post__content", curent_page_html)
						
						problem_text = main_problem.find("input", class_="moderation-conent")
						chief_complaint = str(problem_text["value"])
						author = self.get_author("a","author__name",curent_page_html).text
						author = str(author)
						print()
						print(f"data -->{author}:{chief_complaint}")
			
						# Reply section
						no_of_reply = self.last_page_no("select", "reply-pagination", curent_page_html)
						data = Main_Data(heading=title, sub_heading=current_title,\
											main_problem=chief_complaint,\
											author_name=author)

						self.db.add(data)
						self.db.commit()

						c_id = data.id
						print("id--------> ",c_id)
						for reply_page in range(0, no_of_reply+1):
							reply_url = current_page + f"?order=oldest&page={reply_page}"
							reply_html = self.get_html(url=reply_url)

							div_= self.get_div("div", "reply", reply_html)
							if div_:
								No_of_comments = div_.find("h2", class_="reply__title u-h4")
								No_of_comment = None
								if No_of_comments:
									No_of_comment = No_of_comments.text
								get_articles = div_.find_all("article", class_="post post__root")
								# individual comment section

								for art in get_articles:
									comment_thread = ""
									reply_list = self.comment("input","moderation-conent",art)
									
									if reply_list:
										for thread in reply_list:
											reply = thread["value"]
											comment_thread += f"{reply} --> " 
											print()
											print(f"getting ---->reply data")
											print()
									
									 
										rep = Reply_Data( case_id = c_id, 
													reply=comment_thread, 
													no_of_reply=No_of_comment
															)
										self.db.add(rep)
										self.db.commit()
		except Exception as e:
			print(e)
			
		return "completed !!"

if __name__ == "__main__":
	testing = scrapper()
	print(testing.scrapping_engine())