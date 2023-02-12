from random_user_agent.params import OperatingSystem
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName
from selenium.webdriver.common.by import By
from Cryptodome.Random import random
from selenium import webdriver
from time import sleep
import os


# Total numbers to generate, their interval and the generating webpage
total = 10000000
min = pow(10, 11)
max = pow(10, 12) - 1
rng_url = 'https://www.gigacalculator.com/calculators/random-number-generator.php'

# Generation of the user-agent strings (for distinct OS and browsers)
software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.EDGE.value, SoftwareName.OPERA.value, SoftwareName.SAFARI.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.ANDROID.value, OperatingSystem.IOS.value, OperatingSystem.MACOS.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=500)

my_path = r'/home/julio/Downloads/Software'
if not os.path.isdir(my_path + r'/SeleniumDrivers'):
    os.mkdir(my_path + r'/SeleniumDrivers')

# Added new environment variable for the browsers' drivers
drivers_dir = my_path + r'/SeleniumDrivers'
os.environ['PATH'] += drivers_dir


def initialize_browser():

    fox_profile = webdriver.FirefoxOptions()
    fox_profile.add_argument("--headless")
    fox_profile.add_argument("--width=800")
    fox_profile.add_argument("--height=600")

    # Requests as a distinct user-agent on each request to avoid IP block
    fox_profile.set_preference('general.useragent.override', user_agent_rotator.get_random_user_agent())
    my_browser = webdriver.Firefox()

    # Requests the page and awaits it's loading
    my_browser.get(rng_url)
    my_browser.implicitly_wait(5)

    return my_browser


def auto_generation(my_browser):

    # Selects the form fields to fullfill
    min_field = my_browser.find_element(By.ID, 'numbersfrom')
    max_field = my_browser.find_element(By.ID, 'numbersto')
    qtt_field = my_browser.find_element(By.ID, 'number')

    # Selects the information submit button (request)
    submit_button = my_browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary btn-lg"]')

    # Clears pre-filled data in fields
    min_field.clear()
    max_field.clear()
    qtt_field.clear()

    # Inserting information in the fields
    min_field.send_keys(min)
    max_field.send_keys(max)

    # Amount of numbers to be generated is defined randomly on each request (website limit -> 1000), again to avoid IP block
    n = random.randint(1, 1000)
    qtt_field.send_keys(n)

    # Awaits for the complete fullfill of the fields for then execute the request and receive it's response
    my_browser.implicitly_wait(2)
    submit_button.click()

    # Obtains the text containing the generated numbers in the request's response (tag HTML <th>)
    calc_row = my_browser.find_element(By.TAG_NAME, 'th').text

    # Converts every number in the list to integer (str -> int)
    str_numbers = calc_row.split(', ')
    numbers = list(map(int, str_numbers))
    return numbers


def randomness_evaluation():
    
    print('Initializing...\n')
    all_numbers = list()

    # Start browser
    my_browser = initialize_browser()

    # Until enough number are generated
    while len(all_numbers) < total:

        # Fill in the webpage fields, gets the generated numbers and add them to the list
        numbers = auto_generation(my_browser)
        all_numbers += numbers
        
        del(numbers)
        progress = (len(all_numbers) / total) * 100.0
        print(f'{round(progress, 2)}% concluded...')

        # Waiting time defined randomly between each request to avoid IP block
        timing = random.randint(2, 4)
        sleep(timing)

    # Kill browser
    my_browser.close()

    # Result
    print('\nFinalized!\n')
    size = len(all_numbers)
    uniques = len(set(all_numbers))
    print(f'{size - uniques} repeats in {size} generated numbers!')


if __name__ == '__main__':
    randomness_evaluation()
