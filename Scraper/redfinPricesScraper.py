from selenium import webdriver
from selenium.webdriver.common.by import By

import csv
import time

crimeGradeData = 'C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\RedfinPricesData.csv'
header = ['Price', 'Address', 'Zipcode']
driver = webdriver.Chrome('./chromedriver')

with open('C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\CrimeGradeData.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    start = True
    zipcode = [row[0] for row in reader]
    def grabAll(grabZip, start = False):
        print("waiting")
        time.sleep(3)
        print("wait over")
        priceList = driver.find_elements(By.XPATH, "//td[@class = \"column column_3 col_price\"]")
        addressList = driver.find_elements(By.CSS_SELECTOR, 'a.address')
        for address, price in zip(addressList, priceList):
            print(str(address) + ', ' + str(price))
            newRow = [price.text, address.text, grabZip]
            print(price.text + address.text + str(grabZip))
            with open('C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\RedfinPricesData.csv', 'a', newline = '') as file:
                writer = csv.writer(file)
                if start:
                    writer.writerow(header)
                writer.writerow(newRow)

    for zipCode in range(len(zipcode)-1):
        if(zipCode == 0):
            start = True
        else:
            start = False
        driver.get('https://www.redfin.com/zipcode/'+ str(zipcode[zipCode]) +'/filter/include=sold-3mo')
        driver.find_element(By.XPATH, "//span[@data-rf-test-name='tableOption']").click()
        grabAll(zipcode[zipCode], start)
        driver.get('https://www.redfin.com/zipcode/'+ str(zipcode[zipCode]) +'/filter/include=sold-3mo/page-2')
        grabAll(zipcode[zipCode])