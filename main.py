# Import modules
import requests
import re

# Define a function to get the HTML content of a website
def get_html(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        return ""

# Define a function to extract email addresses from a string
def extract_emails(text):
    # Use a regular expression to find all email patterns
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(pattern, text)
    return emails

# Define a list of websites to crawl
websites = ["Replace web adress /", "Replace web adress ", "Replace web adress "]

# Create an empty set to store unique email addresses
emails = set()

# Loop through each website and get the HTML content
for website in websites:
    html = get_html(website)
    # Extract email addresses from the HTML content and add them to the set
    emails.update(extract_emails(html))

# Print the number and list of email addresses found
print(f"Found {len(emails)} email addresses:")
for email in emails:
    print(email)