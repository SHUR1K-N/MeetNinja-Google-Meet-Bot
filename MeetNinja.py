from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import colorama; from termcolor import colored
import time; from datetime import datetime
import pause; import os; import re

colorama.init()

CHROMEDRIVER = "chromedriver.exe"

##################################################################
#                        Meets                 Yr  M D  Hr min sec
MEETS = {"https://meet.google.com/meetURL1": "2020 9 16 14 14 0",
         "https://meet.google.com/meetURL2": "2020 9 16 14 14 0",
         "https://meet.google.com/meetURL3": "2020 9 16 14 16 0",
         }
DURATION = 60 # Duration of each Meet in minutes
USERNAME = "emailaddress@gmail.com"
PASSWORD = "passw0rd"
##################################################################

# All interactive field / button paths
usernameFieldPath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
nextButtonPath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
passwordFieldPath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
xButtonPath = "#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.B2Jb7d.Up8vH.hFEqNb.J9Nfi.iWO5td > div.R6Lfte.es33Kc.TNczib.X1clqd > div.bZWIgd > div > span > span > svg"
joinButtonPath = "/html/body/div[1]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span"
endButtonPath = "/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[2]/div"

BANNER1 = colored('''
                     ███▄ ▄███▓▓█████ ▓█████▄▄▄█████▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                    ▓██▒▀█▀ ██▒▓█   ▀ ▓█   ▀▓  ██▒ ▓▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ▓██    ▓██░▒███   ▒███  ▒ ▓██░ ▒░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ▒██    ▒██ ▒▓█  ▄ ▒▓█  ▄░ ▓██▓ ░ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ▒██▒   ░██▒░▒████▒░▒████▒ ▒██▒ ░ ▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                    ░ ▒░   ░  ░░░ ▒░ ░░░ ▒░ ░ ▒ ░░   ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                    ░  ░      ░ ░ ░  ░ ░ ░  ░   ░    ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                    ░      ░      ░      ░    ░         ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                           ░      ░  ░   ░  ░                 ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''                                         MeetNinja: The Google Meet Bot''', 'red')
BANNER3 = colored('''                                        --------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3)


def timeStamp():
    timeNow = datetime.now()
    timeString = str(timeNow)
    timeRegEx = re.findall(r"([0-9]+:[0-9]+:[0-9]+)", timeString)
    return(timeRegEx[0])


def initBrowser():
    print("\nInitializing browser...", end="")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-infobars")
    chromeOptions.add_argument("--window-size=800,800")
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    chromeOptions.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2,
                                                    "profile.default_content_setting_values.media_stream_camera": 2,
                                                    "profile.default_content_setting_values.notifications": 2
                                                    })
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=chromeOptions)
    print(colored(" Success!", "green"))
    return(driver)


def login():
    print("Logging into Google account...", end="")
    driver.get('https://accounts.google.com/signin')

    username = driver.find_element_by_xpath(usernameFieldPath)
    username.send_keys(USERNAME)

    nextButton = driver.find_element_by_xpath(nextButtonPath)
    nextButton.click()
    time.sleep(3)

    password = driver.find_element_by_xpath(passwordFieldPath)
    password.send_keys(PASSWORD)

    nextButton = driver.find_element_by_xpath(nextButtonPath)
    nextButton.click()
    time.sleep(3)
    print(colored(" Success!", "green"))


def attendMeet():
    print(f"\n\nNavigating to Google Meet #{meetIndex}...", end="")
    driver.get(URL)
    print(colored(" Success!", "green"))
    print(f"Entering Google Meet #{meetIndex}...", end="")
    time.sleep(3)

    try:
        xButton = driver.find_element_by_css_selector(xButtonPath)
        xButton.click()
        time.sleep(1)
    except:
        pass

    joinButton = driver.find_element_by_xpath(joinButtonPath)
    joinButton.click()
    print(colored(" Success!", "green"))
    time.sleep(1)
    print(colored(f"Now attending Google Meet #{meetIndex} @{timeStamp()}", "green"), end="")


def endMeet():
    endButton = driver.find_element_by_xpath(endButtonPath)
    endButton.click()
    print(colored(f"\nSuccessfully ended Google Meet #{meetIndex} @{timeStamp()}", "red"), end="")


def genericError():
    # clrscr()
    print(colored(" Failed!", "red"), end="")
    print("\n\nPossible fixes:\n")
    print("1. Check your inputs and run MeetNinja again (make sure there are no leading zeros in the Meet start times)")
    print("2. Make sure the developer browser is always open and visible (on top) while MeetNinja is working")
    print("3. Make sure \"chromedriver.exe\" is of the latest stable build (https://chromedriver.chromium.org/)")
    print("4. Make sure the small \"time.sleep\" delays in the functions are comfortable for your internet speed")
    print("5. Make sure your internet connection is stable throughout the process")
    print("\nPress Enter to exit.")
    input()
    try:
        driver.quit()
    except:
        pass


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()

    try:
        DURATION *= 60
        driver = initBrowser()
        print("Waiting until Meet start time...", end="")
        for meetIndex, (URL, startTime) in enumerate(MEETS.items(), start=1):
            startTime = list(map(int, startTime.split()))
            pause.until(datetime(*startTime))
            if (meetIndex <= 1):
                print(colored(" Started!", "green"))
                login()
            attendMeet()
            time.sleep(DURATION)
            endMeet()
        print("\n\nAll Meets completed successfully.")
        print("Press Enter to exit.")
        input()
        driver.quit()

    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
        driver.quit()
    except:
        genericError()
