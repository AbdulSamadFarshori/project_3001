from bs4 import BeautifulSoup
import requests
import cfscrape
import cloudscraper

api_key = "e0e2dbb3f5485a3922197f1854c4ce65"
sitekey = "03196e24-ce02-40fc-aa86-4d6130e1c97a"
baseurl = "https://www.mentalhealthforum.net"

scraper = cloudscraper.create_scraper(delay=10, browser = {'browser': 'chrome',
        										'platform': 'linux',
        										'desktop': True},
        										interpreter="nodejs",
        										 captcha={'provider': '2captcha',
        										 'api_key': api_key
  														})

response = scraper.get(baseurl)


"https://cloudflare.hcaptcha.com/checkcaptcha/03196e24-ce02-40fc-aa86-4d6130e1c97a/W0_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjoiaUhyeFYzUFI5Yk1yOGpoRkVGZFAxTTFrNmVONUFtZUwzcWtSUG8vYlFyN3FvSzNxY24yUjRLT0tHSnVwV1kvdU10NU1ya2hTeXdOeVN0S2JzbkRmQktXZU5RZU53akpMbFVhYVQ4b085VHJUOVl1YXI5cjVwanFUd0QvM2cyNVZsLy9QeTRmUVBJanBETTJJV2VPVmF4SHpYK05aNGJ6c3ZPNlZFdlQ3YTExRGlKamdRTFNhODZab2RwTC9acWMxNDJJTktTazhhbmFjN1R4V1BiTUpGQks0VU9jeVkyeExWb0RBS2lPejB1SEJRckdmcU8wKytlZGhnOGhZNnlRTTFRc1BqTjQ0VFlNRjJ3VkoycFhQS04wSzh1eFd0RUNlNlg5YkI4OURzK0hnZTRUcnFILzdZQzNBOTU0WVdaL3J0ejZJeDdOY3hNTnl0NytuMmhOQ3VBS2RIYnkrTmQ3VnZ3aXVBYVJhdnZ0ZjkvNCtjN2VIRUM4ZmlyMXZRK2I1QkZOdllOR25zU1NxN2JmMUYxYVZ6d2dLa3Y4cDVQbk1OUTJYNXN0UU5yZVJPbzhLNHVrT1Z4WEJSekU4aUJOMmhSNkFoNTFFOXplVU1WMHZESHRsdjc0VWdXR2RDVTdRVjdKVzRyTzNXUGFJQjRpMVhKdHVHWGJ4ZEJ3NllLRFRjTTlyNUZVaFR5L2Zkb3MwNnh6ZnE4ZzZZWUxlWWpJV0JUOVZDTVZGbU9yNkdycDVLZEhnd0dURjF5Uzg4NStzV0RaMk9UTFRiMEdoYXQ0SEVlTUZiblhKNUJ1QnhjV3IvUkE1ZFc5UjJHTGVSeXd0UlZvQjlVcithWXFwNEtoRSthMmpmQm54NkIwRitFTFdQazFYeDNodXpOVnk3SG0rZkd3czZjR1lVVEw4dGh0aUFJdEIwMllLdjhJQ1JVOEpteVlTMGpramU4NTEzRmkwWU1jbkx3TmdGeVR3ZkVXL3Z1blVCWWM1Q1l0N29NdU5oR09ZK0srYXh4bHhHbE8vUiswS3ZiVDVYQ2UvWkhMaS9vUDFlMUVKM0tVL0NUSnVNL0g5S2ZkNnVYbnl3NkxQUUh0K0htRHp4c2kxVTVrRHhjSVFoYzFpai9XSFNmZzNVZnJHRTdNTm9IZkJKQUJaY1V3dXhVTVlDYXoyaUdHTi9FVTl0WVBSOWd3dHduVGhQVGZtQURrUW15ODlkYkZXS0Y3YU1zVFZWd0lkUDJNd1hsdk94ZHhWeW04Zkl6bW9JZnc2V29BQ05Bb0RCeHBQWXNrQzRVWEx2QnZLZkNPekhhZkZabmRmMXc2NDFjQnFpSENFaEUxcGJIRXdwVHBWUzNVcFMzR3NGUlNtbTVSUVlxR3VkQWVhWGJBPUNnVjlWZ2dZSHVBZUxGbjgiLCJleHAiOjE2NTkzNzgwODV9.nxWsWSc_q_iYIv61jFMwDChHGJJVplakdq5MWXnkeMA"

	
print(response.text)
tokens, user_agent = cloudscraper.get_tokens(baseurl)
print(tokens)
