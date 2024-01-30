from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://www.rootdata.com/Fundraising"

# Headless option so chrome won't have to open up each run - qy
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
chrome_driver = webdriver.Chrome(options=options)
chrome_driver.get(url)

# Preparing lists to create dataframe afterwards
name_list = []
fund_list = []
amount_list = []
valuation_list = []
date_list = []
investor_list = []

projects = chrome_driver.find_elements(By.TAG_NAME, 'tr')

# Giving page time to load
time.sleep(8)

# Start from index 1 becuase of col titles. projects[1:] to scrap all projs in page - qy
for n in projects[1:6]:

    # Col 1: Project Names
    projname = n.find_elements(By.XPATH, './td[1]')
    if len(projname) != 0:
        name_list.append(projname[0].text)
    else:
        name_list.append("-")

    # Col 2: Funding Round
    fundround = n.find_elements(By.XPATH, './td[2]')
    if len(fundround) != 0:
        fund_list.append(fundround[0].text)
    else:
        fund_list.append("-")

    # Col 3: Amount Raised
    amount = n.find_elements(By.XPATH, './td[3]')
    if len(amount) != 0:
        amount_list.append(amount[0].text)
    else:
        amount_list.append("-")

    # Col 4: Valuation
    valuation = n.find_elements(By.XPATH, './td[4]')
    if len(valuation) != 0:
        valuation_list.append(valuation[0].text)
    else:
        valuation_list.append("-")

    # Col 5: Date
    date = n.find_elements(By.XPATH, './td[5]')
    if len(date) != 0:
        date_list.append(date[0].text)
    else:
        date_list.append("-")

    # Col 6: Investors
    investors = n.find_elements(By.XPATH, './td[6]')
    if len(investors) != 0:
        investor_list.append(investors[0].text)
    else:
        investor_list.append("-")

print(name_list)
print(fund_list)
print(amount_list)
print(valuation_list)
print(date_list)
print(investor_list)

# Prepare Dataframe

# "\n" new line causes CSV to ignore the delimited characters afterwards, so I replace with blankspace - qy
investor_list = [item.replace('\n', ',') for item in investor_list]

data = {'Project Name': name_list, 'Funding Round': fund_list, 'Amount Raised': amount_list,
        'Valuation': valuation_list, 'Date': date_list, 'Investors': investor_list}
df = pd.DataFrame(data)

# Export dataframe to Excel
df.to_csv('fundraising_records.csv', index=False)
