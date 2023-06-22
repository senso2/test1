import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from tkinter import simpledialog
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.remote.remote_connection import LOGGER
import fileinput
sum_akk = 0
success_count = 0
error_count = 0
positions = [(0, 0), (800, 0), (800, 600), (0, 600)]
def process_account(lines1):
    try:
        words = lines1.strip().split()
        user_agent = UserAgent()
        fake_user_agent = user_agent.random
        chrome_options = Options()
        chrome_options.add_extension('3.crx')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--window-size=600,600")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver_path = "chromedriver"
        for position in positions:
            chrome_options.add_argument(f"--window-position={position[0]},{position[1]}")
        chrome_options.add_argument(f'user-agent={fake_user_agent}')
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
        wait = WebDriverWait(driver, 10)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("https://mail.cx/ru/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "title")))
        title = driver.title
        if "data;" in title:
                driver.quit()
        driver.execute_script("window.open('about:blank','_blank');")
        time.sleep(1)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input.bg-gray-200')))
        text  = element.get_attribute('value')
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/div/div[2]/button[2]'))).click()
        for i, word in enumerate(words):  
            element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/main/div[2]/form/div/div[2]/div[{i+1}]/input')))
            element.send_keys(word)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/button'))).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/button[2]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/div[1]/div[2]/input'))).send_keys('qwerty123')
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/div[1]/div[2]/div/div/input'))).send_keys('qwerty123')
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/div[2]/span/input'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/button'))).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/button'))).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/main/div[2]/form/button'))).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            const newProto = navigator.__proto__
            delete newProto.webdriver
            navigator.__proto__ = newProto
            """
        })
        driver.get("https://galxe.com/trustwallet/campaign/GCpdSUNb1X")
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[2])
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div/button[2]'))).click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div/div[2]/div/button[2]'))).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/main/div/div/div/div/div[1]/div[2]/div[5]/div[2]/div/span/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/button/span')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/main/div/div/div/div/div[1]/div[2]/div[5]/div[2]/div/span/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/button/span'))).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/div[2]/input'))).send_keys(text)
        time.sleep(0.5)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/div[2]/button'))).click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Please confirm your email on Galxe')]"))).click()
        time.sleep(0.5)
        element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[3]/div/table/tbody/tr[3]/td/div/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody[1]/tr[5]/td/h1')))
        text1  = element.text
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[4]/div[2]/input'))).send_keys(text1)
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#app > div.v-dialog__content.v-dialog__content--active > div > div > div > div.nev-verify-btn.d-flex > div:nth-child(1) > button'))).click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/main/div/div/div/div/div[1]/div[2]/div[5]/div[2]/div/span/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/button'))).click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/main/div/div/div/div/div[1]/div[2]/div[5]/div[2]/div/span/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/button'))).click()
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[2]/main/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div/div/button'))).click()
        time.sleep(2)
        with open('готовые_акки.txt', 'a') as file:
            file.write(lines1 + '\n')
        global success_count
        success_count += 1
        driver.quit()
    except:
        with open('Error.txt', 'a') as file:
            file.write(lines1 + '\n')
        global error_count
        error_count += 1
        driver.quit()
    global sum_akk
    sum_akk += 1
    print(f'\nАкаунтов сделано - {sum_akk}\nУдачных попыток: {success_count}\nНеудачных попыток: {error_count}') 

    
    


def main():
    with open('words.txt', 'r') as file:
        lines1 = file.readlines()
    num_cycles = int(simpledialog.askstring("Ввод значения", "Количество акаунтов:"))
    num_threads = int(simpledialog.askstring("Ввод значения", "Количество потоков:"))

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_cycles):
            value1 = lines1[i].strip()
            future = executor.submit(process_account, value1)  # Fix the function call
            futures.append(future)
        for future in futures:
            future.result()
    with open('words.txt', 'w') as file:
        for line in lines1[num_cycles:]:
            file.write(line)

if __name__ == '__main__':
    main()
