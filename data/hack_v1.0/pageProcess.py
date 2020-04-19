from selenium import webdriver
from time import sleep
import facialFeatureAnanlysis as ffa


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome("../ChromeDrivers/chromedriver_linux64/chromedriver")
        self.driver.get("https://tinder.com/?lang=en")


    def login(self, Email, Password):
        close_pop_up = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button')
        close_pop_up.click()
        login_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_button.click()
        show_more_opt = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        show_more_opt.click()
        login_by_fb_but = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        login_by_fb_but.click()
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(Email)
        passwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwd.send_keys(Password)
        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()

        self.driver.switch_to_window(base_window)

    def alternateLogin(self, Email, Password):
        closeButon = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        closeButon.click()
        loginButton = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        loginButton.click()
        fb_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_button.click()
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(Email)
        passwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwd.send_keys(Password)
        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()
        self.driver.switch_to_window(base_window)

    def initTinder(self):
        allow_loc = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_loc.click()
        disable_nots = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        disable_nots.click()
        sleep(5)
        close_passport = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        close_passport.click()

    def sendLike(self):
        rsBut = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        rsBut.click()

    def sendRej(self):
        lsBut = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        lsBut.click()

    def closeHomeScreenPU(self):
        closeBut = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        closeBut.click()

    def getImageDiv(self):

        photoDiv = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]')
        return(photoDiv)


    def nextImg(self):
        photoDiv = self.getImageDiv()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(photoDiv, int(photoDiv.size['width']*0.75), int(photoDiv.size['height']/2))
        action.click()
        action.perform()
        sleep(0.5)

    def prevImg(self):
        photoDiv = self.getImageDiv()
        action = webdriver.common.action_chains.ActionChains(self.driver)
        action.move_to_element_with_offset(photoDiv, int(photoDiv.size['width']*0.25), int(photoDiv.size['height']/2))
        action.click()
        action.perform()


    def getGoldenRatioVariance(self):
        self.driver.save_screenshot('temp/screenshot.png')
        gray = ffa.convertToGray(ffa.getImg('temp/screenshot.png'))
        faces = ffa.detector(gray)

        if(ffa.isOnlyOneFace(faces)):
            ver_ratio, hor_ratio = ffa.onGetGoldenProportions(ffa.getLandmarks(gray, faces[0]))
            return ((ver_ratio, hor_ratio))

        return(None)

    def isOver(self):
        try:
            overButton = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            overButton.click()
            return(True)
        except Exception as e:
            return(False)
