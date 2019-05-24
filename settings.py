import os

# base dir project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# drivers path
DRIVERS_DIR = os.path.join(BASE_DIR, 'drivers')
CHROME_DRIVER_PATH = os.path.join(DRIVERS_DIR, 'chromedriver')
