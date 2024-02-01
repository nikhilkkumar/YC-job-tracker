import requests
from bs4 import BeautifulSoup
import gspread

#google spreadsheet setup
keys = 'yc-job-scraper-027dfd285b0d.json' #authentication
client = gspread.service_account(keys) #service account using keys to authenticate
sh = client.open("YC Startups and roles") #opening up spreadsheet

def scrape_job_data(url):
    response = requests.get(url) #webpage retrieval
    soup = BeautifulSoup(response.text, 'html.parser') #returns HTML code

    company_name = soup.find("h2").get_text() if soup.find("h2") else 'Not specified'
    role = soup.find("h1", class_="ycdc-section-title mb-2").get_text() if soup.find("h1", class_="ycdc-section-title mb-2") else 'Not specified'
    location_label = soup.find('strong', string='Location')
    location = location_label.find_next('span').text if location_label else 'Not specified'
    
    # Updated pay and equity scraping logic with "$" check
    pay_equity_div = soup.find('div', class_="ycdc-card max-w-2xl")
    if pay_equity_div:
        pay = 'Not specified'
        equity = 'Not specified'
        for string in pay_equity_div.stripped_strings:
            if "$" in string:
                pay = string
                break  # Assuming the first occurrence of "$" is always the pay
        for string in pay_equity_div.stripped_strings:
            if "%" in string:
                equity = string
                break  # Assuming the first occurrence of "%" is always the equity
    else:
        pay = 'Not specified'
        equity = 'Not specified'
    
    # Extracting the description
    description_div = soup.find('div', class_="space-y-1")
    description = description_div.find('p').text if description_div and description_div.find('p') else 'Not specified'
        
    return company_name, role, location, pay, equity, description

def update_spreadsheet(company_name, role, location, pay, equity, description):
    # Select the first sheet in the spreadsheet
    worksheet = sh.get_worksheet(0)
    
    # Find the next empty row in the spreadsheet to avoid overwriting existing data
    next_row = len(worksheet.get_all_values()) + 1
    
    # Define the data to be inserted
    row_data = [company_name, role, location, pay, equity, description]
    
    # Insert the data into the next row
    worksheet.insert_row(row_data, next_row)

# Example usage
company_name, role, location, pay, equity, description = scrape_job_data("https://www.ycombinator.com/companies/doola/jobs/ALoBCpT-cs-operations-lead-nyc")
update_spreadsheet(company_name, role, location, pay, equity, description)
