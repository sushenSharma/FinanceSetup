from Xpath_Folder import URL_Repo,Xpath_Repo,ChromeDriver_Path
from selenium.webdriver import  Chrome
import time


class UI_Operation:
    def __init__(self):
        print("hello")
        self.browser = Chrome(executable_path=ChromeDriver_Path.ChromeDriver().ChromeDriverPath)

    def Navigate_To_Url(self,url_path):
        self.browser.get(url_path)

    def Close_Browser(self):
        self.browser.close()


    def Click_On_Input_Field(self,Xpath_input):
        print("Going to Click,",Xpath_input)
        self.browser.find_element_by_xpath(Xpath_input).click()
        time.sleep(4)         #To adjust with Network Latency
        print("Clicked on ",Xpath_input)

    def Click_On_DropDown_Operation_And_Select_Value(self,Xpath_DropDown_Button,Xpath_DropDown_Option):
        self.browser.find_element_by_xpath(Xpath_DropDown_Button).click()
        time.sleep(2)     #To adjust with Network Latency
        self.browser.find_element_by_xpath(Xpath_DropDown_Option).click()
        time.sleep(2)
        print("clicked on Drop down")

    def Type_Text_in_Input_Field(self,Xpath_input,Text_To_Enter):
        self.browser.find_element_by_xpath(Xpath_input).send_keys(Text_To_Enter);






