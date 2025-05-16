import time
import random

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Змінна для вибору режиму: True - headless, False - звичайний
headless_mode =  False # Змінити на False, якщо потрібно бачити браузер

# Змінна для ввімкнення/вимкнення збереження скріншота
save_screenshot = True
screenshot_prefix = "screen "
screenshot_format = ".png"

# Ініціалізація опцій Chrome
chrome_options = Options()
if headless_mode:
    chrome_options.add_argument("--headless=new")

# Ініціалізація WebDriver для Chrome з урахуванням опцій
driver = webdriver.Chrome(options=chrome_options)

# Відкриття вікна на весь екран
driver.maximize_window()

# Відкриття сторінки
url = "https://demoqa.com/text-box"
driver.get(url)
print(f"Відкрито сторінку: {url}")

# Імітація скролінгу вниз
print("Скролінг вниз...")
driver.execute_script("window.scrollBy(0, 350);")
time.sleep(random.uniform(1, 3))

# Знаходження елементів форми
full_name_field = driver.find_element(By.ID, "userName")
email_field = driver.find_element(By.ID, "userEmail")
current_address_field = driver.find_element(By.ID, "currentAddress")
permanent_address_field = driver.find_element(By.ID, "permanentAddress")
submit_button = driver.find_element(By.ID, "submit")

# Дані для заповнення форми
full_name_data = "James Bond"
email_data = "007MI6@example.com"
current_address_data = "30 Wellington Square, Chelsea"
permanent_address_data = "85 Albert Embankment, Vauxhall, Lambeth"

# Імітація введення тексту з затримками
def imitate_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3)) # Випадкова затримка між символами

print("Заповнення поля 'Full Name'...")
imitate_typing(full_name_field, full_name_data)
print("Заповнення поля 'Email'...")
imitate_typing(email_field, email_data)
print("Заповнення поля 'Current Address'...")
imitate_typing(current_address_field, current_address_data)
print("Заповнення поля 'Permanent Address'...")
imitate_typing(permanent_address_field, permanent_address_data)

# Збереження скріншота з автоматичною нумерацією
if save_screenshot:
    now = datetime.now()
    timestamp = now.strftime("%d_%m_%Y %H_%M_%S")
    screenshot_filename = f"{screenshot_prefix}{timestamp}{screenshot_format}"
    driver.save_screenshot(screenshot_filename)
    print(f"Збережено скріншот: {screenshot_filename}")

# Імітація руху миші та кліку на кнопку "Submit"
actions = ActionChains(driver)
actions.move_to_element(submit_button).pause(random.uniform(0.5, 1.5)).click().perform()
print("Натиснуто кнопку 'Submit'")
print("Форма відправленна")
time.sleep(1) # Даємо час на відображення результату

# Імітація скролінгу вгору
print("Скролінг вгору...")
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(random.uniform(1, 3))

# Закриття браузера
driver.quit()
print("Браузер закрито.")
