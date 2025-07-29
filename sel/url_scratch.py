from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to suppress logs and updating the driver to the latest version
# This is useful to avoid unnecessary logs and ensure compatibility with the latest Chrome version.
# You can adjust the log level as needed.
# For example, you can set it to 3 to suppress INFO and DEBUG logs.
# 0: ALL, 1: DEBUG, 2: INFO, 3: WARN, 4: ERROR, 5: FATAL

options = Options()
options.add_argument("--log-level=3")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

file=0
while(True):
    driver = webdriver.Chrome()
    driver.get(f"https://www.indiatoday.in/india")

    url_outer_div = driver.find_element(By.XPATH, '(//div[contains(@class, "story__grid")])')

    print(type(url_outer_div))
    articles=url_outer_div.find_elements(By.TAG_NAME, 'article')
    print(f"Found {len(articles)} articles , {type(articles)}")
    hrefs=[]

    for article in articles:
        # find all <a> tags in the article
        a_tags = article.find_elements(By.TAG_NAME, 'a')
        for a in a_tags:
            href = a.get_attribute('href')
            if href:
                hrefs.append(href)

    print("Found hrefs:"+str(len(hrefs)))
    print("--------------------------------------------------------------------")
    
    for i in range(len(hrefs)):
        try:
            print(f"{i+1}: {hrefs[i]} \n")
            driver.get(hrefs[i])
            print(hrefs[i] +"\n")
            WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "jsx-ace90f4eca22afc7") and contains(@class, "jsx-73334835") and contains(@class, "lhs__section")]'))
            )

            content_divs = driver.find_elements(By.XPATH, '//div[contains(@class, "jsx-ace90f4eca22afc7") and contains(@class, "jsx-73334835") and contains(@class, "lhs__section")]')
            
            for div in content_divs:
                d=div.get_attribute('outerHTML')
                with open(f"sel/data/total_{file}.html", "w", encoding="utf-8") as f:
                    f.write(d)
                    file += 1
        except Exception as e:
            print("---------------------------------------------------------------------")
            print(f"Error processing {hrefs[i]}: {e}+\n")
            print("Skipping to next article...\n")
            continue

    time.sleep(20) 
    print("Finished processing all articles. Waiting for 20 seconds before next iteration...\n")
    #

time.sleep(5) 
driver.close()

