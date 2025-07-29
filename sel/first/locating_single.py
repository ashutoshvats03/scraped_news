from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
query = "laptop"
file=0

driver.get(f"https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_51b863d3-10d6-4288-b9cd-3a7dedaae335_2_X1NCR146KC29_MC.HJZ2651EEY8B&otracker=hp_rich_navigation_8_2.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_HJZ2651EEY8B&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=HJZ2651EEY8B")


outer_div = driver.find_element(By.XPATH, '(//div[contains(@class, "DOjaWF") and contains(@class, "gdgoEp")])[3]')
all_child_divs = outer_div.find_elements(By.CSS_SELECTOR, 'div.cPHDOP.col-12-12')

# Skip the first one
for div in all_child_divs:
    d=div.get_attribute('outerHTML')
    with open(f"sel/data/{query}_{file}.html", "w", encoding="utf-8") as f:
        f.write(d)
        file+=1
# name=KzDlHZ
# MRP yRaY8j ZYYwLA
# price Nx9bqj _4b5DiR
# dis UkUFwK
time.sleep(3) 
driver.close()

