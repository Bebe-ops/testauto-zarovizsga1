"""
## 1 Feladat: Keressük a téglalap kerületét
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a téglalap kerülete app-ot az (https://black-moss-0a0440e03.azurestaticapps.net/x234.html) oldalról.
Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a téglalap kerülete appban:
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert`
összehasonlításokat használj!

* Helyes kitöltés esete:
    * a: 99
    * b: 12
    * Eredmény: 222

* Nem számokkal történő kitöltés:
    * a: kiskutya
    * b: 12
    * Eredmény: NaN

* Üres kitöltés:
    * a: <üres>
    * b: <üres>
    * Eredmény: NaN
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")

    # elements
    a_input = driver.find_element_by_id("a")
    b_input = driver.find_element_by_id("b")
    btn = driver.find_element_by_id("submit")
    result_text = driver.find_element_by_xpath('//div[@id="results"]/p')
    result_span = driver.find_element_by_id("result")

    def fill_field(data_1, data_2):
        a_input.clear()
        b_input.clear()
        a_input.send_keys(data_1)
        b_input.send_keys(data_2)
        btn.click()

    # TC01 - Helyes kitöltés esete
    # test data
    a = 99
    b = 12
    result = 222

    fill_field(a, b)
    assert f'Eredmény:{result}' == result_text.text
    assert result == int(result_span.text)
    time.sleep(2)

    # TC02 - Nem számokkal történő kitöltés
    # test data
    a2 = "kiskutya"
    b2 = "12"
    string_result = "NaN"

    fill_field(a2, b2)
    assert f'Eredmény:{string_result}' == result_text.text
    assert string_result == result_span.text

    # TC03 - Üres kitöltés
    # test data
    a3 = ""
    b3 = ""
    empty_result = "NaN"

    fill_field(a3, b3)
    assert f'Eredmény:{empty_result}' == result_text.text
    assert empty_result == result_span.text
finally:
    driver.close()
