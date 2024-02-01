from bs4 import BeautifulSoup

def find_specific_ul(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Navigate to the first div after the body tag
    first_div = soup.body.find('div') # Assuming it's the very first div after <body>
    
    # Search for the div with the specified class name
    target_div = first_div.find('div', class_="mx-auto max-w-ycdc-page")
    
    # Within that div, find the first section with the specified class name
    target_section = target_div.find('section', class_="relative isolate z-0 border-retro-sectionBorder sm:pr-[13px] ycdcPlus:pr-0 pt-6 lg:pt-9 pb-6 lg:pb-9")
    
    # Within that section, find the first div with the specified class name
    target_inner_div = target_section.find('div', class_="mt-4 lg:mt-6")
    
    # Finally, within this div, find the first ul tag
    target_ul = target_inner_div.find('ul')
    
    # Return the ul element, or None if not found
    return target_ul

# Use the function with your HTML content
# html_content = 'YOUR_HTML_CONTENT_HERE'
# ul_element = find_specific_ul(html_content)
# if ul_element:
#     print(ul_element)
# else:
#     print("UL element not found.")
