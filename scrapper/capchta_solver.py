from twocaptcha import TwoCaptcha
from config import api_key, sitekey, baseurl

def Capchta_Solver(api_key, site_key, url):
    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey=site_key,
            url=url
        )
    except Exception as e:
        print(e)

    else:
        return result 

