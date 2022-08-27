import requests
from config import baseurl
from bs4 import BeautifulSoup
import time
import datetime
from tqdm import tqdm
import logging
import csv
import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "controller.settings")
django.setup()

from api.models import main_data, ReplyData, ReplyThread, LinkConfig


class FetchHtml():

	def __init__(self, url=None):
		
		self.url = url
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

	def fetcher(self):
		response = requests.get(url=self.url, headers=headers)
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
		self.main_capturing_list = ["PTSD - Post Traumatic Stress Disorder",
									"Anxiety Disorders",
									"Depression",
									"Eating Disorders",
									"Sleep Problems",
									"Alcohol Consumption"]

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

	def links(self, html_obj, title):
		output = {}
		for _temp in self.get_links(html_obj):
			self.var += 1
			heading = FindSingleTag(html=_temp, tag="a").get_without_class().text
			anchor_tag = FindSingleTag(html=_temp, tag="a").get_without_class()
			t = anchor_tag["href"] 
			
			logging.info(f"{self.var} --> {baseurl + t}") 
			
			output[f"{heading}-{self.var}"] = baseurl + anchor_tag["href"]
			link_obj = LinkConfig(title=title,
									heading=heading, 
									link=baseurl + anchor_tag["href"], 
									main_status="No",
									reply_status="No")
			link_obj.save()
		return output 

	def fetch_links(self):
		for title, url in self.get_title_links_urls().items():
			for links in url:
				logging.error(f"----> {links}")
				_html = FetchHtml(url=links).fetcher() 
				self.links(_html, title)
	

class GetProblem():


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

	def run_appliction(self):
		link_data = LinkConfig.objects.filter(main_status="No").all()
		print(len(link_data))
		for row in link_data:
			current_title = row.title
			current_heading = row.heading
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

			data = main_data(title=current_title,\
											sub_heading=current_heading,\
											main_problem=case,\
											author_name=author)
			data.save()

			row.main_status = "yes"
			row.save()


class ReplyFunc():

	def get_id(self, ids):
		obj = main_data.objects.filter(id=ids).first()
		if obj:
			return obj

	def get_html(self, url=None):
		print("waiting for html..")
		_html = FetchHtml(url=url).fetcher()
		logging.info("feching html")
		return _html

	def reply_page_no(self, _html):
		select_tag = FindSingleTag(html=_html, tag="select", class_name="submit reply__control reply-pagination").get_single_tags()
		if select_tag:
			options = FindAllTags(html=select_tag, tag="option").get_without_class()
			if len(options) > 0:
				last_page = options[-1]["value"]
				page = int(last_page)
				return page
		return 0

	def reply_page_links(self, _html, current_url):
		_temp = []
		for page in range(self.reply_page_no(_html)):
			reply_url = current_url + f"?order=oldest&page={page}"
			_temp.append(reply_url)
		return _temp
		
	def get_unorder_list(self, _html):
		lists = FindSingleTag(html=_html, tag="ul", class_name="comments").get_single_tags()
		if lists:
			all_lists = FindAllTags(html=lists, tag="li", class_name="comment").get_all_tags()
			return all_lists
		return None

	def get_author(self, _html):
		author_tag = FindSingleTag(html=_html, tag="a", class_name="author__name").get_single_tags()
		if author_tag:
			author = author_tag.text
			return author
		return None

	def get_recipient(self, _html):
		recipient_tag = FindSingleTag(html=_html, tag="a", class_name="author__recipient").get_single_tags()
		if recipient_tag:
			recipient = recipient_tag.text
			return recipient
		return None

	def get_unorder_list_second(self, _html):
		lists = FindSingleTag(html=_html, tag="ul", class_name="comments comments--nested").get_single_tags()
		if lists:
			all_lists = FindAllTags(html=lists, tag="li", class_name="comment comment--nested").get_all_tags()
			return all_lists	
		return []

	def get_reply(self, _html):
		input_tag = FindSingleTag(html=_html, tag="input", class_name="moderation-conent").get_single_tags()
		if input_tag:
			reply = input_tag["value"]
			return reply
		return None
	
	def run(self):
		link_data = LinkConfig.objects.all()
		for obj in link_data:
			print(f"link -----> {obj.link}")
			logging.info("fetching reply page")
			current_url = obj.link
			current_heading = obj.heading
			ids = self.get_id(obj.id)
			_html = self.get_html(url=current_url)
			list_of_link = self.reply_page_links(_html, current_url)
			for link in list_of_link:
				reply_page_html = self.get_html(url=link)
				for li in self.get_unorder_list(reply_page_html):
					author = self.get_author(li)
					recipient = self.get_recipient(li)
					reply = self.get_reply(li)
					logging.info("fetching reply data")
					if author and recipient and reply:
						foo = ReplyData(case_id=ids,author=author,recipient=recipient,reply=reply)
						foo.save()
					obj.reply_status = "yes"
					obj.save() 
					for sec_li in self.get_unorder_list_second(li):
						author = self.get_author(sec_li)
						print(f"author ----> {author}")
						recipient = self.get_recipient(sec_li)
						print(f"recipient ----> {recipient}")
						reply = self.get_reply(sec_li)
						logging.info("fetching reply thread data")
						if author and recipient and reply:
							threadobj = ReplyThread(reply_id=foo,author=author,recipient=recipient,reply=reply)
							threadobj.save()

if __name__ == "__main__":
	
	# first = FetchMainPage()
	# first.linklist()
	# sec = FetchCasesLinks()
	# sec.fetch_links()
	# thr = GetProblem()
	# thr.run_appliction()
	frt = ReplyFunc()
	frt.run()
	