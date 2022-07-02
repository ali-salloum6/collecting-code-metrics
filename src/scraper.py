'''
a script to scape project keys from the sonarcloud recent projects page,
and append them to a text file called project_keys.txt
Note: the scraped keys might contain duplicates and need to be handled
and cleaned. 
'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# open a browser driver to view the sonarcloud projects
target_url = 'https://sonarcloud.io/explore/projects'
driver_path = "/home/ali/Downloads/chromedriver" # change to the path of your web driver
driver = webdriver.Chrome(driver_path)
driver.get(target_url)
driver.maximize_window()

project_keys = set() # a variable to store the keys of the projects
overall = 0 # the number of stored project keys

# for each iteration, scrape the six visible projects, then scroll down to view the next sex
# when reaching the end of the page click "Show More" to show the next 50 projects
for i in range(1600):
    print("Step #",i) 
    wait = WebDriverWait(driver, 1)
    time.sleep(1) # wait until page loads
    
    doc = BeautifulSoup(driver.page_source, features="lxml")
     # elements with the links to the projects:
    projects = doc.find_all("h2", class_='css-q652d4-H2 e1p7gp4w0')
    
    for project in projects: 
        link = project.find_all("a")[1]
         # discard the first 21 character as the key starts at the 22nd char
        project_keys.add(link['href'][21:])

    # every 10 iterations, save the scraped project keys to avoid losing progress if the program crashes
    if (i%10) == 0:
        with open(r'project_keys.txt', 'a') as fp:
            for key in project_keys:
                fp.write("%s\n" % key)
        overall = overall + len(project_keys)
        print("overall number of keys collected: ", overall)
        project_keys = set() # discard the already saved keys

    # every 5 iterations, click "Show More" to show the next 50 projects
    if (i%5) == 0 and i!=0:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"footer.spacer-top.note.text-center button.button.spacer-left"))).click()
            print(i,"Clicked Show More!")
        finally:
            continue

    # scroll down to show the view 6 projects in the page
    driver.execute_script("window.scrollTo(0, {})".format(str((i+1)*1200)))

# save the keys left in the set
with open(r'project_keys.txt', 'a') as fp:
    for key in project_keys:
        fp.write("%s\n" % key)
