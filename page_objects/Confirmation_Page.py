"""
This module models the Checkout page
URL: /sunscreen
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators 

class Confirmation_Page(Base_Page):

    PAYMENT_SUCCESS=locators.PAYMENT_SUCCESS

    "This class models the sunscreen page"
    def start(self):
        "Go to this URL -- if needed"
        url = 'confirmation'
        self.open(url)
    
    def verify_payment(self):
        result_flag= False
        if self.PAYMENT_SUCCESS:
            result_flag= True
        return result_flag
