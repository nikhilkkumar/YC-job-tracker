import requests
from bs4 import BeautifulSoup
import gspread

#google spreadsheet setup
keys = 'yc-job-scraper-027dfd285b0d.json' #authentication
client = gspread.service_account(keys) #service account using keys to authenticate
sh = client.open("YC Startups and roles") #opening up spreadsheet

def scrape_job_data(url):
    response = requests.get(url) #webpage retrival
    soup = BeautifulSoup(response.text, 'html.parser') #returns HTML code

    company_name = soup.find("h2").get_text()
    role = soup.find("h1",class_="ycdc-section-title mb-2").get_text()
    
    return role

print(scrape_job_data("https://www.ycombinator.com/companies/coris/jobs/2j8IBtf-bizops"))