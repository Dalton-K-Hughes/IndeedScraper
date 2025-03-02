import os
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        
        #Remove below lines, testing purposes only
        html_file = 'indeed.html'
        abs_path = os.path.abspath(html_file)
        file_url = f'file://{abs_path}'
        self.browser.get(file_url)
        #Remove above lines, testing purposed only
        
        #Uncomment below line for real site usage
        #self.browser.get('https://www.indeed.com')
    
    def exit(self):
        self.browser.quit()
        
    # #TODO: Create a functions that gets relavent filter options for job searches
    # def get_date_posted(self):
    #     try:
    #         date_posted = self.browser.find_element(By.XPATH, '//button[normalize-space()="Date posted"]')
    
    
    # Gets the element that allows users to search for specific keywords related to jobs
    def get_job_searchbox(self):
        try:
            searchbox = self.browser.find_element(By.XPATH, '//input[@name="q"]')
            return searchbox
        except NoSuchElementException:
            searchbox = WebDriverWait(self.browser, randint(5, 10)).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@name="q"]')))
            return searchbox
            
    # Gets the element that allows users to search for locations for jobs        
    def get_location_searchbox(self):
        try:
            searchbox = self.browser.find_element(By.XPATH, '//input[@name="l"]')
            return searchbox
        except NoSuchElementException:
            searchbox = WebDriverWait(self.browser, randint(5, 10)).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@name="l"]')))
            return searchbox