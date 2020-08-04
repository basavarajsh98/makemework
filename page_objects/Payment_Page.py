"""
This module models the payment page on weather shopper
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators
import random

class Payment_Page(Base_Page):

    EMAIL = locators.EMAIL
    CREDIT_CARD = locators.CREDIT_CARD
    VALID_TILL = locators.VALID_TILL
    CVC = locators.CVC
    ZIPCODE = locators.ZIPCODE
    PAY_BUTTON = locators.PAY_BUTTON
    REMEMBER=locators.REMEMBER
    MOBILE=locators.MOBILE

    def start(self):
        "move to payment frame"
        self.switch_frame("iframe")

    def verify_email(self, email):
        result_flag=False
        if ('@' in email) & ('.' in email) & ~(email.startswith("@", 0)):
            result_flag = True
        self.conditional_write(result_flag,
            positive="%s is a valid email-id"%email,
            negative="%s is an invalid email-id"%email)
        return result_flag

    def generate_email(self):
        number=random.randrange(0,100,1)
        email=f"Internship_day_{number}@qxf2.com"
        return email

    def click_pay_button(self):
        "Click on the pay button"
        result_flag = self.click_element(self.PAY_BUTTON)
        if result_flag:
            self.switch_page("checkout")
        self.conditional_write(result_flag,
        positive="Clicked on the pay button. Redirecting to confiramtion page",
        negative="Could not click on the pay button. Failed to redirect to confiramtion page")
        return result_flag

    def pay_details(self,credit_card,valid_till,cvc,zipc,remember,mobile):
        email=self.generate_email()
        self.set_text(self.EMAIL, email)
        result_flag=self.verify_email(email)
        self.set_text(self.CREDIT_CARD, credit_card)
        self.set_text(self.VALID_TILL, valid_till)
        self.set_text(self.CVC, cvc)
        self.set_text(self.ZIPCODE, zipc)
        if remember.lower() in ["yes", "y"]:
            self.select_checkbox(self.REMEMBER)
            self.set_text(self.MOBILE, mobile)
        result_flag&=self.click_pay_button()
        result_flag&=self.verify_payment()
        return result_flag

    

    

    
    
