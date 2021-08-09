"""
## 4 Feladat: Email mező
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a Email mező app-ot az (https://black-moss-0a0440e03.azurestaticapps.net/mm43.html) oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a Email mező app tesztelését.
A cél az email validáció tesztelése:

* Helyes kitöltés esete:
    * email: teszt@elek.hu
    * Nincs validációs hibazüzenet

* Helytelen:
    * email: teszt@
    * Please enter a part following '@'. 'teszt@' is incomplete.

* Üres:
    * email: <üres>
    * b: <üres>
    * Please fill out this field.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")

    # elements
    email_field = driver.find_element_by_id("email")
    submit_btn = driver.find_element_by_id("submit")
    validation_msg_xp = '//div[@class="validation-error"]'

    # test data
    emails = ["teszt@elek.hu", "teszt@", ""]

    def fill_email(email):
        email_field.clear()
        email_field.send_keys(email)
        submit_btn.click()

    # TC01 - Helyes kitöltés esete:
    # email = "teszt@elek.hu"
    # Nincs validációs hibazüzenet

    fill_email(emails[0])
    assert len(driver.find_elements_by_xpath(validation_msg_xp)) == 0

    # TC02 - Helytelen:
    # email = "teszt@"
    expected_msg = "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

    fill_email(emails[1])
    assert driver.find_element_by_xpath(validation_msg_xp).text == f'Kérjük, adja meg a „@” utáni részt is. ' \
                                                                   f'A(z) „{emails[1]}” cím nem teljes.'

    # TC03 - Üres:
    # email = ""
    expected_empty_msg = "Kérjük, töltse ki ezt a mezőt."

    fill_email(emails[2])
    assert driver.find_element_by_xpath(validation_msg_xp).text == expected_empty_msg
finally:
    driver.close()
