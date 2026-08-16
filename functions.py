from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def RunOsint(request, se):
    url = f"https://www.google.com/search?q={request}"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    if se:
        url = f'https://www.google.com/search?q="{request}"'

    driver.get(url)