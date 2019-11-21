"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.

Example code:
        if page_name == "main page":
            test_obj = Tutorial_Main_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name == "redirect":
            test_obj = Tutorial_Redirect_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
Pages implemented so far:
1. 
"""
from .zero_page import Zero_Page
from .landing_page import Landing_Page
from conf import base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=base_url_conf.base_url,trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()

        #Add your code for initializing each page over here
        #See example in the opening doc string of this file
        if page_name in ["zero","zero page"]:
            test_obj = Zero_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        elif page_name in ["landing","landing page","main","main page"]:
            test_obj = Landing_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)

        return test_obj

    get_page_object = staticmethod(get_page_object)