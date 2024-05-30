import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def navigate_to_appointment_page(driver):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'plz_field')))
        postal_code_input = driver.find_element(By.ID, 'plz_field')
        postal_code_input.send_keys('67655')
        submit_button = driver.find_element(By.ID, 'first_next_btn')
        submit_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'forward-service')))
        option_button = driver.find_element(By.ID, 'forward-service')
        option_button.click()
    except Exception as e:
        print(f"Error navigating to appointment page: {e}")

def check_appointments(driver):
    try:
        appointment_elements = driver.find_elements(By.CLASS_NAME, 'smart-date-headline')
        for appointment in appointment_elements:
            if "June" in appointment.text:
                print(f"Appointment found in June: {appointment.text}")
                return True
    except Exception as e:
        print(f"Error checking appointments: {e}")
    return False

if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'URL'

    refresh_interval = 900

    driver.execute_script("window.open('');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])

    navigate_to_appointment_page(driver)

    try:
        while True:
            if check_appointments(driver):
                print("Appointment available in June! Check the website.")
                winsound.Beep(1000, 500)
                
            else:
                print("No appointments found in June. Refreshing...")
                driver.refresh()
                time.sleep(refresh_interval)
    except KeyboardInterrupt:
        print("Stopping the script.")
    
