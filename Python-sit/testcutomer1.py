from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

class Testcustomer1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\webdriver\chromedriver.exe")

    def test_input1(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canonc")
        age.send_keys("2")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone1.png')
        
        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        

    def test_input2(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("Johnj")
        last.send_keys("canoncanoncano")
        age.send_keys("149")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone2.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: Johnj", result)
        

    def test_input3(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("Johnjohnjohnjo")
        last.send_keys("canoncanoncanon")
        age.send_keys("150")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone3.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: Johnjohnjohnjo", result)
        

    def test_input4(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("Johnjohnjohnjo")
        last.send_keys("canoncan")
        age.send_keys("75")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone4.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: Johnjohnjohnjo", result)
        

    def test_input5(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohnjohnjoh")
        last.send_keys("canoncan")
        age.send_keys("75")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone5.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohnjohnjoh", result)
        

    def test_input6(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("john")
        last.send_keys("canoncan")
        age.send_keys("75")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone6.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: john", result)
        
        

    def test_input8(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("cano")
        age.send_keys("75")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone8.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        

   
        

    def test_input10(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canoncan")
        age.send_keys("0")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone10.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        

    def test_input11(self):
        self.driver.get("http://127.0.0.1/customerphp/customer.php")
        
        name = self.driver.find_element(By.ID, "firstName")
        last = self.driver.find_element(By.ID, "lastName")
        age = self.driver.find_element(By.ID, "age")
        drp_title = Select(self.driver.find_element(By.ID, "title"))
        drp_title.select_by_index(0)
        
        name.send_keys("johnjohn")
        last.send_keys("canoncan")
        age.send_keys("151")

        submit = self.driver.find_element(By.ID, "submit")
        submit.click()

        self.driver.save_screenshot('img/testjhone11.png')

        result = self.driver.find_element(By.ID, "firstName").text
        self.assertEqual("First Name: johnjohn", result)
        

if __name__ == "__main__":
    unittest.main()
