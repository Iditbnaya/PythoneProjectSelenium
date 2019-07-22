#pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# open file with url
my_file = open("c:/temp/buyme.txt", 'r', encoding='utf-8')
# # Call Chrome Driver
#
driver = webdriver.Chrome(executable_path="C:\\Users\\Idit\\PycharmProjects\\pythoneProjectIditbnaya\\chromedriver.exe")#

# # open Buyme Website using a file
string = my_file.readline()
print(string)
driver.get(string)
#
# # wait for elements
driver.implicitly_wait(50)
# # Press on button "כניסה הרשמה"
#     #first moving נגישות
driver.find_element_by_css_selector("#NagishLiMoveTR").click()
driver.implicitly_wait(50)
driver.find_element_by_css_selector(".nav-bar.buttons > li:nth-child(3) > a > span:nth-child(2)").click()
driver.find_element_by_class_name("text-btn").click()
# #
# # # # Enter Detail's in registration Form
# # # # First name
driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys("idit")
# # # # Email address
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("devopscouree910@bnaya.com")
# # # # Input Password
driver.find_element_by_id("valPass").send_keys("1Password@!")
# # # # Confirm Passwword
driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("1Password@!")
# # # # Press on radio button "אני מסכים"
driver.find_element_by_css_selector(".ember-checkbox").send_keys(Keys.SPACE)
#  # # Press button "הרשמה"
driver.find_element_by_xpath("//button[@type='submit' and @class='ui-btn orange large']").click()

## Upload the page again twice in order it to work with part B
driver.implicitly_wait(50)
driver.get(string)
driver.implicitly_wait(50)
driver.get(string)
# # #### End Of Part #1 ####
## Part B ##

##select price from list
##Create list for all fields
driver.implicitly_wait(50)
List = driver.find_elements_by_class_name("chosen-single")
print(len(List))
driver.implicitly_wait(10)
List[0].click()
#driver.find_element_by_xpath("//*[@id='ember700_chosen']/div/ul/li[3]").click()
driver.find_element_by_xpath("//ul[@class='chosen-results']/li[2]").click()

##Select erea
List[1].click()
driver.find_element_by_xpath("//ul[@class='chosen-results']/li[2]").click()
##select Category
List[2].click()
driver.find_element_by_xpath("//ul[@class='chosen-results']/li[2]").click()
##click on batton תמצא לי מתנה
driver.find_element_by_xpath("//*[@class='ui-btn search ember-view']").click()
driver.implicitly_wait(100)
###EndofPartB#######



## Part C ##

##Pick a business
driver.find_element_by_id('ember1078').click()
##Type a price
driver.find_element_by_xpath("//input[@placeholder='מה הסכום?']").send_keys('1600')
driver.find_element_by_xpath("//input[@placeholder='מה הסכום?']").send_keys(Keys.ENTER)
###end of part C

### Part D ####

# Press on radio button "למישהו אחר"
driver.find_element_by_xpath("//*[@id='ember1176']/label[1]").click()
# Enter receiver name
driver.find_element_by_xpath("//*[@id='ember1208']").send_keys('ADI')
driver.find_element_by_xpath("//*[@id='ember1210']").send_keys('IDIT')
driver.find_element_by_xpath("//*[@id='ember1212_chosen']/a").click()
# Choose מתנה לעובדת
driver.find_element_by_xpath("//ul[@class='chosen-results']/li[14]").click()
time.sleep(1)
driver.implicitly_wait(10)


card = driver.find_element_by_xpath("//*[@id='ember1232']/textarea")

card.click()
card.clear()
card.send_keys("מתנה לעובדת המצטיינת שתמיד תקשקשי בזנב ותהיי מאושרת :)")
driver.implicitly_wait(10)
## Upload A picture
driver.find_element_by_id("ember1241").send_keys('c://temp//pic.png')
##press on מיד אחרי התשלום
driver.find_element_by_class_name("send-now").click()
##press on SMS
driver.find_element_by_class_name("icon-sms").click()

##write giver phone and receiver phone
listphone= driver.find_elements_by_xpath("//input[@placeholder='ספרות בלבד, בלי מקף']")
print(len(listphone))
listphone[0].send_keys('0543166046')
listphone[1].send_keys('0507060097')

##click save
driver.find_element_by_xpath("//*[@id='ember1169']/div[4]/div/div[4]/div[2]/button[2]").click()
##click Submit
driver.find_element_by_xpath("//*[@id='ember1169']/div[5]/button").click()


####End Of Project  :) :) ####
########



