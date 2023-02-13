from random_user_agent.params import OperatingSystem
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName
import os


# RNG Webpage
URL = 'https://www.gigacalculator.com/calculators/random-number-generator.php'

# Generation of the user-agent strings (for distinct OS and browsers)
SOFTWARE_NAMES = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.EDGE.value, SoftwareName.OPERA.value, SoftwareName.SAFARI.value]
OPERATING_SYSTEMS = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.ANDROID.value, OperatingSystem.IOS.value, OperatingSystem.MACOS.value]   
USER_AGENT_ROTATOR = UserAgent(software_names=SOFTWARE_NAMES, operating_systems=OPERATING_SYSTEMS, limit=500)

MY_PATH = r'/home/julio/Downloads/Software'
if not os.path.isdir(MY_PATH + r'/SeleniumDrivers'):
    os.mkdir(MY_PATH + r'/SeleniumDrivers')

# Environment variable for the browsers' drivers
DRIVERS_DIR = MY_PATH + r'/SeleniumDrivers'
