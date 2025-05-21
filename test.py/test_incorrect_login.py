import pytest
from selenium.webdriver.common.by import By



class TestNegativeLogin:
    @pytest.mark.negative_login
    @pytest.mark.parametrize("username, password, error_message", [("incorrect_username", "Password123", "Your username is invalid!"), ("student", "incorrect_password", "Your password is invalid!")])
    
    def test_negative_login(self, driver, username, password, error_message):

        driver.get("https://practicetestautomation.com/practice-test-login/")
        user_locater = driver.find_element(By.ID, 'username')
        user_locater.send_keys(username)

        password_locater = driver.find_element(By.NAME, 'password')
        password_locater.send_keys(password)

        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        
        incorrect_msg = driver.find_element(By.ID, "error")
        assert incorrect_msg.text == error_message, "the error msg is not matching"