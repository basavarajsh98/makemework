#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Main page
TEMPERATURE_FIELD = "id,temperature"
BUY_BUTTON = "xpath,//button[contains(text(),'Buy %s')]"

#Product page
PAGE_HEADING = "xpath,//h2[text()='%s']"
PRODUCTS_LIST = "xpath,//div[contains(@class,'col-4')]"
ADD_PRODUCT_BUTTON = "xpath,//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"
CART_QUANTITY_TEXT = "id,cart"
CART_BUTTON = "xpath,//button[@onclick='goToCart()']"

#Cart page
CART_TITLE = "xpath,//h2[text()='Checkout']"
CART_ROW = "xpath,//tbody/descendant::tr"
CART_ROW_COLUMN = "xpath,//tbody/descendant::tr[%d]/descendant::td"
CART_TOTAL = "id,total"
PAY_WITH_CARD = "xpath,//span[contains(text(),'Pay with Card')]"


#Payment page
FRAME="class,stripe_checkout_app"
EMAIL = "xpath,//input[@placeholder='Email']"
CREDIT_CARD = "xpath,//input[@placeholder='Card number']"
VALID_TILL = "xpath,//input[@placeholder='MM / YY']"
CVC = "xpath,//input[@placeholder='CVC']"
ZIPCODE = "xpath,//input[@placeholder='ZIP Code']"
REMEMBER = "xpath,//div[@class='Checkbox-tick']"
MOBILE="xpath,//input[@inputmode='tel']"
PAY_BUTTON = "xpath,//button[@type='submit']"

#Checkout page
PAYMENT_SUCCESS="xpath,//h2[contains(.,'PAYMENT SUCCESS')]"
