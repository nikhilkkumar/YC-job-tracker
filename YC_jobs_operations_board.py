from bs4 import BeautifulSoup
import requests

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

def extract_job_links(url):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Find all job links within the unordered list
    job_links = soup.find_all('ul', class_='space-y-2 overflow-hidden')

    # Extract job titles and links
    #jobs = {link.get_text(): url + link['href'] for link in job_links}

    return job_links

# Example usage
url = 'https://www.ycombinator.com/jobs/role/operations'
# jobs = extract_job_links(url)
# for title, link in jobs.items():
#     print(f"{title}: {link}")

print(extract_job_links(url))