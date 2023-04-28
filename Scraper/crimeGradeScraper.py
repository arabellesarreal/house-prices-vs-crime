from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
import time

crimeGradeData = 'C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\CrimeGradeData.csv'
header = ['Zipcode', 'Overall_Crime_Grade', 'Violent_Crime_Grade', 'Property_Crime_Grade', 'Other_Crime_Grade']

with open('C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\zip_code_database - Sheet3.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    uors = [row[1] for row in reader]

with open('C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\zip_code_database - Sheet3.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    zipData = [row[0] for row in reader]

    #print(zipData)
    #print(uors)
    zipcodeList = zipData
    uorsList = uors

    grade = ["F", "E-", "E", "E+", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]

    driver = webdriver.Chrome('./chromedriver')

    start = True

    for zipcode in range(len(zipcodeList)-1):
        print("waiting")
        time.sleep(5)
        print("wait over")
        if uorsList[zipcode] != "UNIQUE":
            try:
                driver.get('https://crimegrade.org/safest-places-in-'+ str(zipcodeList[zipcode]) +'/')
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/p[1]")
            except selenium.common.exceptions.NoSuchElementException:
                print("Zipcode: " + zipcodeList[zipcode] + "not found")
            else:
                wait = WebDriverWait(driver, 10)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                overCG = driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/p[1]").text
                violCG = driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div/span").text
                propCG = driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/table/tbody/tr[2]/td[2]/div/span").text
                otherCG = driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/table/tbody/tr[3]/td[2]/div/span").text
                newRow = [zipcodeList[zipcode], overCG, violCG, propCG, otherCG]
                for convert in range(4):
                    newRow[convert+1] = grade.index(newRow[convert+1])
                with open('C:\\Users\\Ara\\Desktop\\Data Analysis Capstone\\Scraper\\CrimeGradeData.csv', 'a', newline = '') as file:
                    writer = csv.writer(file)
                    if start:
                        writer.writerow(header)
                        start = False
                    writer.writerow(newRow)