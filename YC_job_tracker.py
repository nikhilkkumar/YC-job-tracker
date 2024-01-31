import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('your_credentials_file.json', scope)
client = gspread.authorize(creds)
sheet = client.open('your_spreadsheet_name').sheet1

def scrape_job_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data using BeautifulSoup based on the HTML structure of the Y Combinator job board
    company_name = # extract company name
    role = # extract role
    location = # extract location
    pay = # extract pay
    equity = # extract equity
    description = # extract description

    return [company_name, role, location, pay, equity, description]

def update_sheet(data):
    # Append data to the Google Sheet
    sheet.append_row(data)

# Example usage
job_url = 'https://www.ycombinator.com/companies/coris/jobs/2j8IBtf-bizops'
job_data = scrape_job_data(job_url)
update_sheet(job_data)
