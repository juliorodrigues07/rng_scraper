from selenium.webdriver.common.by import By
import scraping.constants as const
from selenium import webdriver
from os import environ


class RNGScrapper(webdriver.Firefox):

    def __init__(self, driver_path=r'/SeleniumDrivers', alive=False):

        self.driver_path = driver_path
        self.alive = alive

        # Adds new environment variable for the browsers' drivers
        environ['PATH'] += driver_path

        # Setting some window options
        fox_profile = webdriver.FirefoxOptions()
        fox_profile.add_argument("--headless")
        fox_profile.add_argument("--width=800")
        fox_profile.add_argument("--height=600")

        # Requests as a distinct user-agent on each request to avoid IP block
        fox_profile.set_preference('general.useragent.override', const.USER_AGENT_ROTATOR.get_random_user_agent())

        # Initiates the browser and awaits it's loading
        super(RNGScrapper, self).__init__()
        self.implicitly_wait(5)

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        # Killing (or not) the browser after scraping process is complete
        if not self.alive:
            self.quit()

    def initiate_browser(self):

        self.get(const.URL)

    def set_min_number(self, min=0):
        
        # Selects the form fields to fullfill
        min_field = self.find_element(By.ID, 'numbersfrom')

        # Clears any possible pre-filled data in field
        min_field.clear()

        # Inserts information in the field
        min_field.send_keys(min)

    def set_max_number(self, max=1):
        
        max_field = self.find_element(By.ID, 'numbersto')
        max_field.clear()
        max_field.send_keys(max)

    def set_how_many(self, n=1):
        
        qtt_field = self.find_element(By.ID, 'number')
        qtt_field.clear()
        qtt_field.send_keys(n)

    def submit_information(self):

        # Selects the information submit button (request)
        submit_button = self.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary btn-lg"]')
        submit_button.click()

        # For waiting the response containing the results (numbers)
        self.implicitly_wait(5)

    def extract_generated_numbers(self):
        
        # Gets values field block by ID
        result_field = self.find_element(By.ID, 'calcResult')

        # Gets values block by the unique HTML tag (th) present in this webpage
        value_block = result_field.find_element(By.TAG_NAME, 'th')

        # Obtains the block's content remvoving spaces
        str_numbers = value_block.get_attribute('innerHTML').strip()
        
        return str_numbers
