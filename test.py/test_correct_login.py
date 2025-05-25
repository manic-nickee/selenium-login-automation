import time
import pytest

from selenium.webdriver.common.by import By


class TestPositveScanario:

    @pytest.mark.correct_login
    def test_positive_login(self, driver):

        driver.get("https://practicetestautomation.com/practice-test-login/")
        
        user_locater = driver.find_element(By.ID, 'username')
        user_locater.send_keys('student')
        
        password_locater = driver.find_element(By.NAME, 'password')
        password_locater.send_keys("Password123")
        
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(3)
        
        curren_url =driver.current_url
        assert curren_url == "https://practicetestautomation.com/logged-in-successfully/"
        
        text_locater = driver.find_element(By.TAG_NAME, "h1")
        assert text_locater.text == "Logged In Successfully"
        
        
        logout_locater = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_locater.is_displayed()
