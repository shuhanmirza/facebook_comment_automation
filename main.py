from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import json 
import time
import random
import string
import os
import requests

def automate_facebook_comment(comment_count=1000):
    # Opening env.json file 
    f = open('env.json',) 
    
    # returns JSON object as a dictionary 
    credentials = json.load(f) 

    # Closing file 
    f.close()   

    username = credentials['username']
    password = credentials['password']
    target_username = credentials['target_username']


    firefox_options = Options()
    firefox_options.add_argument('--dns-prefetch-disable')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--lang=en-US')
    browser = webdriver.Firefox()


    browser.get('https://www.facebook.com/')
    signup_elem = browser.find_element_by_id('email')
    signup_elem.send_keys(username)

    login_elem = browser.find_element_by_id('pass')
    login_elem.send_keys(password)

    ins = browser.find_elements_by_tag_name('input')
    for x in ins:
        if x.get_attribute('value') == 'Log In':
            x.click() # here logged in
            break

    #then key here move to mobile version as that doesn't support javascript
    browser.get('https://m.facebook.com/'+target_username+'?v=timeline') 


    # find last post (occurance of comment)
    as_el = browser.find_elements_by_tag_name('a')
    for a in as_el:
        print(a.text)
        if 'omment' in a.text.strip():
            a.click()
            break
    time.sleep(10)

    # it will go for 1000 comments
    i = comment_count
    while i > 0:
        # do actual comment
        ins = browser.find_element_by_id('composerInput')

        cmnt = getRandomQuote()
        
        ins.send_keys(cmnt)
        # submit input

        ins = browser.find_elements_by_tag_name('input')
        for x in ins:
            if 'omment' in x.get_attribute('value'):
                x.click()
                break

        #random waiting 
        r = random.randrange(2,5)
        time.sleep(r)
        
        i = i - 1

def getRandomQuote():
    params = {
        'method':'getQuote',
        'lang':'en',
        'format':'json'
    }
    response = requests.get('http://api.forismatic.com/api/1.0/',params)
    jsonText =json.loads(response.text)
    return f'{jsonText["quoteText"]} - {jsonText["quoteAuthor"]}'

if __name__ == "__main__":
    automate_facebook_comment(1000)