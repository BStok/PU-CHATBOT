import requests
from bs4 import BeautifulSoup

url = 'https://uiet.puchd.ac.in/?page_id=44'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

Departments = soup.find_all('div', class_='entry-content')

for department in Departments:
    title = department.find('h2')
    if title:
        print(title.text.strip())
    else:
        print("No title found")
    
    content = department.find('div', class_='entry-content')
    if content:
        print(content.text.strip())
    else:
        print("No content found")
    
    print("\n" + "="*40 + "\n")