from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

class WebScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def scrape_website(self, url):
        if not self.driver:
            self.setup_driver()

        self.driver.get(url)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract main content
        main_content = self.extract_main_content(soup)

        # Length-aware extraction
        extracted_text = self.length_aware_extraction(main_content)

        data = {
            'url': url,
            'title': soup.title.string if soup.title else '',
            'meta_description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else '',
            'text_content': extracted_text,
            'links': [{'text': a.text, 'href': a['href']} for a in soup.find_all('a', href=True)],
            'images': [{'src': img['src'], 'alt': img.get('alt', '')} for img in soup.find_all('img', src=True)],
            'structured_data': []  # Initialize as an empty list
        }

        # Extract structured data if present
        structured_data = soup.find_all('script', type='application/ld+json')
        if structured_data:
            data['structured_data'] = [script.string for script in structured_data]

        return data

    def extract_main_content(self, soup):
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Look for common content containers
        content_tags = ['article', 'main', 'div', 'section']
        content = None
        for tag in content_tags:
            content = soup.find(tag, class_=re.compile('(content|article|post)'))
            if content:
                break

        if not content:
            content = soup.body

        # Extract text from paragraphs
        paragraphs = content.find_all('p')
        text = ' '.join(p.get_text().strip() for p in paragraphs)

        return text

    def simple_sentence_split(self, text):
        # Split on period followed by space and capital letter
        return re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

    def length_aware_extraction(self, text, max_chars=2000, max_sentences=10):
        sentences = self.simple_sentence_split(text)
        extracted_text = ""
        char_count = 0
        sentence_count = 0

        for sentence in sentences:
            if char_count + len(sentence) <= max_chars and sentence_count < max_sentences:
                extracted_text += sentence + " "
                char_count += len(sentence) + 1  # +1 for the space
                sentence_count += 1
            else:
                break

        return extracted_text.strip()

    def close(self):
        if self.driver:
            self.driver.quit()