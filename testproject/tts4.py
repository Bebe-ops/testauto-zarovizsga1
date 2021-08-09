"""
## 2 Feladat: Pénzfeldobás
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a pénzfeldobás app-ot az (https://black-moss-0a0440e03.azurestaticapps.net/tts4.html) oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a pénzfeldobás app tesztelését.
Az alkalmazás akkor működik helyesen ha 100 gombnyomásból legalább 30 fej. Ezt kell ellenőrizned.
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert`
összehasonlításokat használj!

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")

    def locator(my_id):
        element = driver.find_element_by_id(my_id)
        return element

    # elements
    btn_id = "submit"
    results_xp = '//*[@id="results"]/li'

    for index, value in enumerate(range(1, 101)):
        locator(btn_id).click()

    time.sleep(2)

    results_list = driver.find_elements_by_xpath(results_xp)
    head_list = []
    for _ in results_list:
        if _.text == "fej":
            head_list.append(_.text)

    assert len(results_list) == 100
    assert len(head_list) >= 30
finally:
    driver.close()
