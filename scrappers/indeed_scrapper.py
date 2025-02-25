from random import randint, choice
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

# Class to represent a job scrapper for Indeed
class Indeed_Scrapper:
    def __init__(self):
        
        # Set base options for chrome driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--incognito')
        
        # Diable Selenium detection
        options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Create a randomized user agent
        user_agent = UserAgent()
        user_agent = user_agent.random
        options.add_argument(f'user-agent={user_agent}')
        
        self.browser = webdriver.Chrome(options=options)
        self.browser.get('https:www.indeed.com')