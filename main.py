from selenium import webdriver
import time
import datetime

# loading list of sites into array
listSites = []
with open('sites.txt', 'r') as sites:
    for site in sites: 
        listSites.append(site.strip())

for site in listSites:

    driver = webdriver.Chrome()
    driver.get(site)
    time.sleep(5)
    cookies = driver.get_cookies()
    print(cookies)

    for cookie in cookies:
        print(cookie)
        print(cookie['name'])

    driver.quit()

    # stripping illegal filename chars (: and /)
    site = site.replace("https://www.","")
    fileName = site.replace("http://www.","")
    fileName = fileName.replace("/","_") + ".txt"


    # write to file
    with open("savedCookies/" + fileName, 'w') as file:
        # check each cookie for 'expiry' key. converts from epoch to datetime
        for cookie in cookies:
            if 'expiry' in cookie:
                expiryDate = cookie['expiry']
                datetimeExpiry = datetime.datetime.fromtimestamp(expiryDate).strftime('%Y-%m-%d %H:%M:%S')
            else:
                datetimeExpiry = "NO_EXPIRY"
            file.write(f"{cookie['name']} : {datetimeExpiry}\n")


