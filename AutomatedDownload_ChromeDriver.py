"""
Scipt to download the chromeDriver automatically. Needs the current google chrome version as input (shows in the webbrowser under help/about google chrome)

Things to remember. The google profile is not connected to the driver, you can just use the path there to get the options argument 
to the current chrome driver, which will make it import passwords, cookies that has been used previously.   
"""

import requests
import json
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import zipfile

"""Start section where functions are defined, used for downloading libraries and data, as well as syncing with the sharepoint"""
def chromePathInfo(employee):
    """
    Returns the path to the chrome profile and local user path, based on the name of user. The chrome profile is used for downstream sharepoint function. This 
    could probably also be achieved by using a Selenium-profile (which is simpler/more easily overviewed). 

    Parameters:
    employee (str): string with the name of the employee, which needs to match one of the exsisting if statements ()
    """
    if employee == "Martin Andersson-Li":
        chromeProfilePath = "C:/Users/MartinAndersson/AppData/Local/Google/Chrome/User Data/Profile 1"
        myUserPath = "MartinAndersson"
    if employee == "Patrick Gant":
        chromeProfilePath = "C:/Users/PatrickGant/AppData/Local/Google/Chrome/User Data/Profile 2"
        myUserPath = "PatrickGant"
    if employee == "Pavlos Aslanis":
        chromeProfilePath = "C:/Users/PavlosAslanis/AppData/Local/Google/Chrome/User Data/Profile 1"
        myUserPath = "PavlosAslanis"
    return chromeProfilePath, myUserPath

myName = "Martin Andersson-Li" #Input to chromePathInfo, Assumes that your name with corresponding information has been added to the function.

# URL to fetch the JSON data
json_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"

# Fetch the JSON data
response = requests.get(json_url)
data = response.json()

chrome_version = "127.0.6533.72"
platform = "win64"  # Example platform, change as needed

# Parse the JSON to find the correct download URL
for version_info in data['channels']['Stable']['downloads']['chromedriver']:
    if version_info['platform'] == platform:
        download_url = version_info['url']
        break

wd = os.path.join('C:\\Users\\MartinAndersson\\.wdm\drivers\\chromedriver\\win64', chrome_version)
os.chdir(wd)

response = requests.get(download_url)
download_path = os.path.join(os.getcwd(), 'chromedriver.zip')

with open(download_path, 'wb') as file:
    file.write(response.content)

print(f"ChromeDriver downloaded to {download_path}")

# Extract the zip file
with zipfile.ZipFile(download_path, 'r') as zip_ref:
    zip_ref.extractall()

# Path to the extracted chromedriver
chromedriver_path = os.path.join(wd, 'chromedriver-win64', 'chromedriver.exe')

# Set up Selenium with the downloaded ChromeDriver
myName = "Martin Andersson-Li"
chromeProfilePath, myUserPath = chromePathInfo(myName)

chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={chromeProfilePath}")# if you want to run headless

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Test the driver
driver.get("http://www.google.com")
print(driver.title)
driver.quit()