"""
## 5 Feladat: Kakukktojás - városok
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a Kakukktojás - városok app-ot az (https://black-moss-0a0440e03.azurestaticapps.net/rv4.html)
oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Kakukktojás - városok app tesztelését.
Az applikáció minden frissítésnél véletlenszerűen változik!
Feladatod, hogy megtaláld a hiányzó városnevet, kitöltsd a form-ban a mezőt és ellnörizd le, hogy eltaláltad-e.
A feladatnak több helyes megoldása is van (találgatós/ismétlős, pythonban kalkulálós), mindegy, hogy hogyan oldod meg,
csak találd meg az egy véletlen hiányzó város nevét

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")

    # test data
    # elements
    cities = driver.find_element_by_xpath("//textarea")
    random_cities = driver.find_elements_by_xpath('//ul[@id="randomCities"]/li')
    miss_city = driver.find_element_by_id('missingCity')
    submit_btn = driver.find_element_by_id('submit')

    cities_list = cities.text.replace('"', "").split(",")
    random_cities_list = []
    for _ in random_cities:
        random_cities_list.append(_.text)

    result = []
    for _ in cities_list:
        if _ not in random_cities_list:
            result.append(_)

    for _ in result:
        miss_city.clear()
        miss_city.send_keys(_)
        submit_btn.click()

    # próbálkoztam ezzel is
    diff = np.setdiff1d(cities_list, random_cities_list)
    print(diff)

finally:
    pass
    # driver.close()

