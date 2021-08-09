"""
## 3 Feladat: Összeadó
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
A program töltse be a összeadó app-ot az (https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html) oldalról.
Feladatod, hogy automatizáld selenium webdriverrel a összeadó app tesztelését.
Az applikáció minden frissítésnél véletlenszerűen változik!
A feladatod, hogy a random számokkal működő matematikai applikációt ellenőrizd. A teszted ki kell, hogy olvassa a két
operandust (számot) és az operátort (műveleti jelet). Ennek megfelelően kell elvégezned a kalkulációt Pythonban.
A kalkuláció gombra kattintva mutatja meg az applikáció, hogy mi a művelet eredménye szerinte.
Hasonlítsd össze az applikáció által kínált megoldást és a Python által kalkulált eredményt.
Ennek a kettőnek egyeznie kell.
Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest) viszont fontos, hogy `assert`
összehasonlításokat használj!
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")

    # elements
    num1 = driver.find_element_by_id("num1")
    num2 = driver.find_element_by_id("num2")
    op = driver.find_element_by_id("op")
    btn = driver.find_element_by_id("submit")
    result = driver.find_element_by_id("result")


    def operation(num_1, num_2):
        if op.text == "+":
            results = num_1 + num_2
            return results
        elif op.text == "-":
            results = num_1 - num_2
            return results
        elif op.text == "*":
            results = num_1 * num_2
            return results
        elif op.text == "/":
            results = num_1 / num_2
            return results

    btn.click()
    assert int(result.text) == operation(int(num1.text), int(num2.text))
finally:
    driver.close()
