import requests
from bs4 import BeautifulSoup
from app import app, db
from models import Staff
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

BASE_URL = 'https://www.universiteitleiden.nl'
STAFF_URL = 'https://www.universiteitleiden.nl/en/science/computer-science/staff#tab-7'


def scrape_and_populate():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(STAFF_URL)
    time.sleep(5)  # Wait for JS to load
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find('section', {'id': 'tabpanel-all staffmembers'})
    if not section:
        print('Staff section not found!')
        return
    staff_list = section.find_all('li')
    for li in staff_list:
        a = li.find('a', href=True)
        if not a:
            continue
        profile_path = a['href']
        profile_url = BASE_URL + profile_path if profile_path.startswith('/') else profile_path
        name_tag = a.find('strong')
        role_tag = a.find('span', class_='meta')
        img_tag = a.find('img')
        if not (name_tag and role_tag and img_tag):
            continue
        name = name_tag.text.strip()
        role = role_tag.text.strip()
        # Image URL logic
        img_src = img_tag.get('data-zoom-src') or img_tag.get('src')
        if img_src.startswith('/'):
            image_url = BASE_URL + img_src
        else:
            image_url = img_src
        # Remove /d50x50 from the end for high quality image
        if image_url.endswith('/d50x50'):
            image_url = image_url[:-7]  # Remove last 8 characters
            print(image_url)
        # Remove duplicate if exists
        if not Staff.query.filter_by(name=name).first():
            staff = Staff(name=name, role=role, profile_url=profile_url, image_url=image_url)
            db.session.add(staff)
    db.session.commit()
    print('Database populated.')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        scrape_and_populate()
